#!/usr/bin/env python3
"""Tests for scripts/check_evidence.py.

Standard library only (unittest + tempfile). No pytest, no network, no external
dependencies. Run directly:

    python3 tests/test_check_evidence.py

These tests never touch the real starter files: they load the checker module, point
its module-level paths at a temporary directory, and restore them afterwards.
"""

import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.normpath(os.path.join(HERE, os.pardir, "scripts", "check_evidence.py"))


def load_checker():
    spec = importlib.util.spec_from_file_location("check_evidence", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ce = load_checker()


class TestStudentContent(unittest.TestCase):
    def assertFilled(self, text):
        self.assertTrue(ce.is_filled(ce.student_content_lines(text)))

    def assertNotFilled(self, text):
        self.assertFalse(ce.is_filled(ce.student_content_lines(text)))

    def test_headings_quotes_comments_are_not_content(self):
        self.assertNotFilled("# Heading\n\n> instruction\n<!-- a prompt here -->")

    def test_blank_template_like_fails(self):
        template = (
            "# Problem framing\n"
            "> Fill this in before building.\n"
            "## Problem statement\n"
            "<!-- What is hard, for whom? -->\n"
            "## Success metric\n"
            "<!-- One measurable metric. -->\n"
        )
        self.assertNotFilled(template)

    def test_real_answer_passes(self):
        self.assertFilled("## Problem statement\nOn-call engineers waste time on triage.")

    def test_pure_checkbox_does_not_count(self):
        self.assertNotFilled("## Data safety check\n- [ ] I used only synthetic data")

    def test_empty_table_row_does_not_count(self):
        self.assertNotFilled("| Rule | Signal | Output |\n| --- | --- | --- |\n| 1 |  |  |")

    def test_filled_table_row_counts(self):
        self.assertFilled("| Rule | Signal | Output |\n| --- | --- | --- |\n| 1 | DLQ | requeue |")

    def test_prompt_label_lines_do_not_count(self):
        self.assertNotFilled("Metric chosen:\nWhat should the baseline decide?")

    def test_generic_placeholder_does_not_count(self):
        for token in ("TODO", "TODO later", "tbd", "n/a", "later", "fill later"):
            with self.subTest(token=token):
                self.assertNotFilled(token)


class TestCheckDataset(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self._orig = ce.DATASET
        self.addCleanup(lambda: setattr(ce, "DATASET", self._orig))
        ce.DATASET = os.path.join(self.tmp.name, "synthetic-incidents.jsonl")

    def write(self, text):
        with open(ce.DATASET, "w", encoding="utf-8") as handle:
            handle.write(text)

    def test_missing_dataset_fails(self):
        self.assertIsNotNone(ce.check_dataset())

    def test_invalid_json_fails(self):
        self.write('{"id": "INC-1"}\nthis is not json\n')
        self.assertIsNotNone(ce.check_dataset())

    def test_too_few_records_fails(self):
        self.write("\n".join('{"id": "INC-%d"}' % i for i in range(3)) + "\n")
        self.assertIsNotNone(ce.check_dataset())

    def test_enough_records_passes(self):
        self.write("\n".join('{"id": "INC-%d"}' % i for i in range(ce.MIN_RECORDS)) + "\n")
        self.assertIsNone(ce.check_dataset())


class TestCheckArtifact(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self._orig = ce.STARTER_ROOT
        self.addCleanup(lambda: setattr(ce, "STARTER_ROOT", self._orig))
        ce.STARTER_ROOT = self.tmp.name

    def write(self, name, text):
        with open(os.path.join(self.tmp.name, name), "w", encoding="utf-8") as handle:
            handle.write(text)

    def test_missing_file_reports_problem(self):
        self.assertIsNotNone(ce.check_artifact("problem-framing.md"))

    def test_empty_file_reports_problem(self):
        self.write("problem-framing.md", "   \n\n")
        self.assertIsNotNone(ce.check_artifact("problem-framing.md"))

    def test_template_only_reports_problem(self):
        self.write(
            "problem-framing.md",
            "# Problem framing\n## Problem statement\n<!-- describe it -->\n",
        )
        self.assertIsNotNone(ce.check_artifact("problem-framing.md"))

    def test_real_content_passes(self):
        self.write(
            "problem-framing.md",
            "# Problem framing\n## Problem statement\nOn-call engineers cannot triage fast.\n",
        )
        self.assertIsNone(ce.check_artifact("problem-framing.md"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
