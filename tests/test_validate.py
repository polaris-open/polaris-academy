#!/usr/bin/env python3
"""Tests for scripts/validate.py.

Standard library only (unittest). No network, no external dependencies. Run with:

    python3 tests/test_validate.py

Confirms the validator FAILS on simulated secrets / PII and ACCEPTS clearly
synthetic placeholders.
"""

import importlib.util
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.normpath(os.path.join(HERE, os.pardir, "scripts", "validate.py"))


def load():
    spec = importlib.util.spec_from_file_location("validate", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load()


class TestSecrets(unittest.TestCase):
    def test_detects_real_github_token(self):
        text = "token = ghp_" + "a" * 36
        self.assertTrue(v.find_real_secrets(text))

    def test_detects_real_aws_key(self):
        self.assertTrue(v.find_real_secrets("AKIA1234567890ABCDEF"))

    def test_detects_private_key_block(self):
        self.assertTrue(v.find_real_secrets("-----BEGIN RSA PRIVATE KEY-----"))

    def test_ignores_placeholder_openai_key(self):
        self.assertEqual(v.find_real_secrets("sk-EXAMPLE_DO_NOT_USE_abcdef"), [])

    def test_ignores_aws_canonical_example(self):
        # AWS's documented example key literally contains EXAMPLE.
        self.assertEqual(v.find_real_secrets("AKIAIOSFODNN7EXAMPLE"), [])


class TestPII(unittest.TestCase):
    def test_flags_realistic_email(self):
        self.assertTrue(v.find_pii("contact alice.smith@gmail.com please"))

    def test_ignores_example_email(self):
        self.assertEqual(v.find_pii("contact user@example.test please"), [])

    def test_ignores_all_zero_cpf(self):
        self.assertEqual(v.find_pii("CPF 000.000.000-00"), [])

    def test_flags_formatted_cpf_like(self):
        self.assertTrue(v.find_pii("CPF 123.456.789-09"))

    def test_line_word_does_not_suppress_real_email(self):
        # "sample" in the line must NOT mark the real address as a placeholder.
        self.assertTrue(v.find_pii("sample customer email: alice@gmail.com"))


class TestLuhn(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(v.luhn_ok("4111111111111111"))

    def test_invalid(self):
        self.assertFalse(v.luhn_ok("4111111111111112"))


class TestDataset(unittest.TestCase):
    SYNTH = "data/synthetic-incidents.jsonl"

    def test_contains_pii_true_fails(self):
        failures, _ = v.scan_dataset_text(self.SYNTH, '{"id": "X", "contains_pii": true}\n')
        self.assertTrue(failures)

    def test_contains_pii_missing_fails(self):
        failures, _ = v.scan_dataset_text(self.SYNTH, '{"id": "X"}\n')
        self.assertTrue(failures)

    def test_contains_pii_null_fails(self):
        failures, _ = v.scan_dataset_text(self.SYNTH, '{"id": "X", "contains_pii": null}\n')
        self.assertTrue(failures)

    def test_contains_pii_non_boolean_fails(self):
        failures, _ = v.scan_dataset_text(self.SYNTH, '{"id": "X", "contains_pii": "false"}\n')
        self.assertTrue(failures)

    def test_invalid_json_fails(self):
        failures, _ = v.scan_dataset_text("data/x.jsonl", "{not json}\n")
        self.assertTrue(failures)

    def test_clean_record_passes(self):
        failures, warnings = v.scan_dataset_text(self.SYNTH, '{"id": "X", "contains_pii": false}\n')
        self.assertEqual(failures, [])
        self.assertEqual(warnings, [])

    def test_non_synthetic_path_warns_but_does_not_fail(self):
        failures, warnings = v.scan_dataset_text("data/records.jsonl", '{"id": "X", "contains_pii": false}\n')
        self.assertEqual(failures, [])
        self.assertTrue(warnings)


class TestPIITier(unittest.TestCase):
    def test_pii_fatal_in_dataset(self):
        self.assertTrue(v.pii_is_fatal("starters/x/data/synthetic-incidents.jsonl"))

    def test_pii_fatal_in_lab_markdown(self):
        self.assertTrue(v.pii_is_fatal(
            "formations/applied-ai-engineering/levels/01-ai-foundations-for-builders/"
            "labs/01-framing-and-baseline/examples/good-submission.md"
        ))

    def test_pii_fatal_in_starter_markdown(self):
        self.assertTrue(v.pii_is_fatal("starters/ai-incident-support-assistant/README.md"))

    def test_pii_warn_in_policy_docs(self):
        self.assertFalse(v.pii_is_fatal("DATA_POLICY.md"))
        self.assertFalse(v.pii_is_fatal("README.md"))
        self.assertFalse(v.pii_is_fatal("docs/lab-authoring-security.md"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
