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


class TestLuhn(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(v.luhn_ok("4111111111111111"))

    def test_invalid(self):
        self.assertFalse(v.luhn_ok("4111111111111112"))


class TestDataset(unittest.TestCase):
    def test_contains_pii_true_fails(self):
        failures, _ = v.scan_dataset_text(
            "data/synthetic-incidents.jsonl", '{"id": "X", "contains_pii": true}\n'
        )
        self.assertTrue(failures)

    def test_invalid_json_fails(self):
        failures, _ = v.scan_dataset_text("data/x.jsonl", "{not json}\n")
        self.assertTrue(failures)

    def test_clean_synthetic_record_passes(self):
        failures, warnings = v.scan_dataset_text(
            "data/synthetic-incidents.jsonl", '{"id": "X", "contains_pii": false}\n'
        )
        self.assertEqual(failures, [])
        self.assertEqual(warnings, [])

    def test_non_synthetic_path_without_flags_warns(self):
        failures, warnings = v.scan_dataset_text("data/records.jsonl", '{"id": "X"}\n')
        self.assertEqual(failures, [])
        self.assertTrue(warnings)


if __name__ == "__main__":
    unittest.main(verbosity=2)
