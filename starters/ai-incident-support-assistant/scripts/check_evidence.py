#!/usr/bin/env python3
"""Check that the minimum Level 1 evidence files are present and actually filled in.

Standard library only. No network, no LLM, no external dependencies. Read-only: this
script never modifies any file. Run it from the starter (or via `make evidence`) at
any time to see what is still missing.

What this is — and is NOT:
  * It is a conservative presence/completeness lint. It detects *obvious* gaps:
    a missing file, an empty file, or a file that still looks like the untouched
    template.
  * It does NOT grade quality and it does NOT understand your answers. A green result
    means "you filled the files in", not "your framing/baseline/metric is good".
    Use the lab rubrics, self-assessment and examples for that.

Design note (why it is not a keyword search): checking for words like "baseline" or
"metric" would pass on the *blank* templates, because those words are already in the
headings and prompts. Instead, this script strips the template scaffolding (headings,
blockquotes, HTML-comment prompts, empty table rows, checkboxes, label-only lines)
and asks a simpler, honest question: is there any content here that the learner
actually wrote?
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STARTER_ROOT = os.path.normpath(os.path.join(HERE, os.pardir))
DATASET = os.path.join(STARTER_ROOT, "data", "synthetic-incidents.jsonl")
MIN_RECORDS = 5

# Artifact file -> which lab it belongs to (for grouped, didactic output).
ARTIFACTS = [
    ("problem-framing.md", "Lab 01"),
    ("privacy-note.md", "Lab 01"),
    ("progress.md", "Lab 01"),
    ("dataset-notes.md", "Lab 02"),
    ("manual-baseline.md", "Lab 02"),
]

_SEPARATOR_ROW = re.compile(r"^\|[\s:\-|]+\|$")
_THEMATIC_BREAK = re.compile(r"^[-*_]{3,}$")
_CHECKBOX = re.compile(r"^[-*]\s*\[[ xX]\]")
_BARE_MARKER = re.compile(r"^([-*]|\d+\.)$")
_WORDS = re.compile(r"\w+")


def student_content_lines(text):
    """Return the lines that look like content the learner wrote.

    Everything that is part of the shipped template — headings, blockquotes,
    HTML-comment prompts, code fences, table headers/separators, empty table rows,
    checkboxes, bare list markers, and label/prompt lines ending in ':' or '?' — is
    removed. Whatever remains is treated as the learner's own input.
    """
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)  # drop comment prompts
    lines = text.splitlines()
    content = []
    in_code = False

    for index, raw in enumerate(lines):
        line = raw.strip()

        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not line:
            continue
        if line.startswith("#") or line.startswith(">"):
            continue
        if _THEMATIC_BREAK.match(line):
            continue

        if line.startswith("|"):
            if _SEPARATOR_ROW.match(line):
                continue
            next_line = lines[index + 1].strip() if index + 1 < len(lines) else ""
            if _SEPARATOR_ROW.match(next_line):
                continue  # this is a header row
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells and all(cells):
                content.append(line)  # a fully-filled data row counts as content
            continue

        if _CHECKBOX.match(line) or _BARE_MARKER.match(line):
            continue
        if line.endswith(":") or line.endswith("?"):
            continue  # label / prompt line

        content.append(line)

    return content


def is_filled(content_lines):
    """At least one substantive line (>= 2 words) means the learner wrote something."""
    return any(len(_WORDS.findall(line)) >= 2 for line in content_lines)


def check_artifact(filename):
    path = os.path.join(STARTER_ROOT, filename)
    if not os.path.isfile(path):
        return "missing file"
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    if not text.strip():
        return "file is empty"
    if not is_filled(student_content_lines(text)):
        return "still looks like the untouched template (no answers written yet)"
    return None


def check_dataset():
    if not os.path.isfile(DATASET):
        return f"missing file ({os.path.relpath(DATASET, os.getcwd())})"
    records = 0
    with open(DATASET, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                if isinstance(json.loads(line), dict):
                    records += 1
            except json.JSONDecodeError:
                return "contains an invalid JSON line (run 'make test' for details)"
    if records < MIN_RECORDS:
        return f"has {records} record(s); expected at least {MIN_RECORDS}"
    return None


def main():
    problems = []

    dataset_problem = check_dataset()
    if dataset_problem:
        problems.append(("data/synthetic-incidents.jsonl", "dataset", dataset_problem))

    for filename, lab in ARTIFACTS:
        problem = check_artifact(filename)
        if problem:
            problems.append((filename, lab, problem))

    if not problems:
        print("Evidence check passed: minimum Level 1 evidence is present.")
        print("This does not grade quality. Use the rubrics and examples for self-assessment.")
        return 0

    print("Evidence check failed. Missing or weak evidence:")
    for filename, group, detail in problems:
        print(f"- {filename} ({group}): {detail}")
    print("")
    print("Fill in the artifacts for Lab 01 and Lab 02, then run 'make evidence' again.")
    print("This only checks presence, not quality — keep using the rubrics and examples.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
