#!/usr/bin/env python3
"""Repository data-hygiene validator for Polaris Academy.

Standard library only. No network, no LLM, no external dependencies. Read-only.

This is a **guardrail, not a complete secret/PII scanner.** It catches obvious
mistakes — a missing or empty essential file, an invalid dataset, a record marked
`contains_pii: true`, or a high-confidence leaked credential — and it *warns* about
lower-confidence patterns (emails, document numbers, phone-like strings) that a human
should review. It deliberately does not claim to find every leak.

Severities:
  * FAIL  -> exits non-zero. High confidence that something is wrong.
  * WARN  -> printed for human review, does not fail the build.

Run from anywhere:  python3 scripts/validate.py
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, os.pardir))

# Files that must exist and not be empty.
ESSENTIAL_FILES = [
    "README.md",
    "START_HERE.md",
    "LICENSE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "DATA_POLICY.md",
    "formations/applied-ai-engineering/README.md",
    "starters/ai-incident-support-assistant/README.md",
    "starters/ai-incident-support-assistant/data/synthetic-incidents.jsonl",
]

TEXT_SUFFIXES = {".md", ".py", ".jsonl", ".json", ".csv", ".yml", ".yaml", ".txt"}

# Files allowed to contain example patterns when describing the rules themselves.
# Excluded from the content scan so the validator does not flag its own regexes or
# the docs that teach which patterns are forbidden.
CONTENT_SCAN_EXCLUDE = {
    "scripts/validate.py",
    "tests/test_validate.py",
}

# High-confidence credentials. Found (and not a placeholder) => FAIL.
SECRET_PATTERNS = {
    "openai-style key": re.compile(r"sk-[A-Za-z0-9_]{16,}"),
    "github token (classic)": re.compile(r"ghp_[A-Za-z0-9]{36}"),
    "github token (fine-grained)": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "aws access key id": re.compile(r"AKIA[0-9A-Z]{16}"),
    "private key block": re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
}

# Lower-confidence personal data. Found (and not a placeholder) => WARN.
PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "cpf (formatted)": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    "cnpj (formatted)": re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
    "cpf/cnpj (unformatted)": re.compile(r"\b\d{11}\b|\b\d{14}\b"),
    "br phone": re.compile(r"\b(?:\+55\s?)?\(?\d{2}\)?\s?9?\d{4}[-\s]?\d{4}\b"),
}

_CARD_CANDIDATE = re.compile(r"\b(?:\d[ -]?){13,19}\b")

_PLACEHOLDER_MARKERS = (
    "example", "do_not_use", "donotuse", "do-not-use", "placeholder",
    "redacted", "fake", "dummy", "sample", "changeme", "your_", "xxxx", "notreal",
)


_RESERVED_EMAIL_DOMAINS = (".test", ".example", ".invalid", ".localhost")


def is_secret_placeholder(match):
    return any(marker in match.lower() for marker in _PLACEHOLDER_MARKERS)


def is_pii_placeholder(match):
    """Decide placeholder status from the matched VALUE only (and reserved domains).

    Deliberately ignores other words on the line, so a line like
    "sample customer email: alice@gmail.com" still flags the real-looking address.
    """
    value = match.lower()
    if any(marker in value for marker in _PLACEHOLDER_MARKERS):
        return True
    digits = re.sub(r"\D", "", match)
    if digits and len(set(digits)) == 1:  # all-same digit, e.g. 000... / 111...
        return True
    if "@" in value:
        domain = value.split("@")[-1]
        if "example" in domain or domain.endswith(_RESERVED_EMAIL_DOMAINS):
            return True
    return False


def luhn_ok(digits):
    total, parity = 0, len(digits) % 2
    for i, ch in enumerate(digits):
        d = int(ch)
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def find_real_secrets(text):
    """Return (name, match) for credential patterns that are NOT placeholders."""
    out = []
    for name, pattern in SECRET_PATTERNS.items():
        for m in pattern.finditer(text):
            if not is_secret_placeholder(m.group(0)):
                out.append((name, m.group(0)))
    return out


def find_pii(text):
    """Return (name, match, line) for personal-data patterns that are NOT placeholders."""
    out = []
    lines = text.splitlines()
    for name, pattern in PII_PATTERNS.items():
        for m in pattern.finditer(text):
            line = lines[text.count("\n", 0, m.start())] if lines else ""
            if not is_pii_placeholder(m.group(0)):
                out.append((name, m.group(0), line.strip()))
    for m in _CARD_CANDIDATE.finditer(text):
        digits = re.sub(r"\D", "", m.group(0))
        if 13 <= len(digits) <= 19 and luhn_ok(digits) and len(set(digits)) > 1:
            line = lines[text.count("\n", 0, m.start())] if lines else ""
            if not is_pii_placeholder(m.group(0)):
                out.append(("credit-card-like (luhn)", m.group(0), line.strip()))
    return out


def iter_text_files():
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, REPO_ROOT)
            if rel in CONTENT_SCAN_EXCLUDE:
                continue
            if name == "Makefile" or os.path.splitext(name)[1].lower() in TEXT_SUFFIXES:
                yield rel, full


def read_text(path):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return handle.read()


def check_essential(failures):
    for rel in ESSENTIAL_FILES:
        path = os.path.join(REPO_ROOT, rel)
        if not os.path.isfile(path):
            failures.append(f"essential file missing: {rel}")
        elif not read_text(path).strip():
            failures.append(f"essential file is empty: {rel}")


_MISSING = object()


def scan_dataset_text(rel, text):
    """Validate one JSONL dataset. Returns (failures, warnings) — pure and testable.

    Every JSON object record must explicitly declare `contains_pii: false` (the
    boolean). Missing, true, null, or non-boolean values fail — that is the machine
    enforcement of the Data Policy.
    """
    failures, warnings = [], []
    records = 0
    for line_no, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as error:
            failures.append(f"{rel}:{line_no}: invalid JSON ({error})")
            continue
        records += 1
        if isinstance(record, dict):
            value = record.get("contains_pii", _MISSING)
            if value is not False:
                shown = "missing" if value is _MISSING else repr(value)
                failures.append(
                    f"{rel}:{line_no}: contains_pii must be the boolean false (found: {shown})"
                )
        else:
            warnings.append(
                f"{rel}:{line_no}: record is not a JSON object; cannot verify contains_pii — review"
            )
    if records and "synthetic" not in rel.lower():
        warnings.append(
            f"{rel}: dataset path does not contain 'synthetic' — consider naming it so"
        )
    return failures, warnings


def check_datasets(failures, warnings):
    for rel, full in iter_text_files():
        if not rel.endswith(".jsonl"):
            continue
        f, w = scan_dataset_text(rel, read_text(full))
        failures.extend(f)
        warnings.extend(w)


def pii_is_fatal(rel):
    """Real-looking PII must never be committed to datasets or learning content.

    FAIL there; only WARN in policy/docs that legitimately discuss PII shapes.
    """
    if rel.endswith((".jsonl", ".json", ".csv")):
        return True
    if rel.endswith((".md", ".txt")) and rel.startswith(("starters/", "formations/")):
        return True
    return False


def scan_patterns(failures, warnings):
    for rel, full in iter_text_files():
        text = read_text(full)
        for name, match in find_real_secrets(text):
            failures.append(f"{rel}: possible real secret ({name}): {match[:12]}…")
        pii = find_pii(text)
        if not pii:
            continue
        sink = failures if pii_is_fatal(rel) else warnings
        verb = "must be synthetic/placeholder" if sink is failures else "review"
        for name, match, line in pii:
            sink.append(f"{rel}: possible {name}: {match} — {verb} (line: {line[:60]})")


# Phrases that may encourage pasting real data. Warn-only and negation-aware, scoped
# to lab/starter content (the security docs legitimately list these terms).
_ENCOURAGE_PATTERNS = [
    re.compile(r"paste\s+(?:your\s+)?(?:real|production|actual|internal|company)", re.I),
    re.compile(r"use\s+(?:your\s+)?(?:real|production|actual|internal|company)\s+\w*\s*"
               r"(?:data|logs?|tickets?|customers?|credentials?|secrets?)", re.I),
    re.compile(r"copy\s+(?:your\s+)?(?:real|production|internal|company)", re.I),
]
_NEGATORS = re.compile(r"\b(?:do not|don't|never|avoid|without|no|not|synthetic|fake|fictional|example)\b", re.I)
_PASTE_SCAN_DIRS = ("formations/", "starters/")


def check_paste_instructions(warnings):
    for rel, full in iter_text_files():
        if not rel.endswith(".md") or not rel.startswith(_PASTE_SCAN_DIRS):
            continue
        for line_no, line in enumerate(read_text(full).splitlines(), start=1):
            if _NEGATORS.search(line):
                continue
            if any(pattern.search(line) for pattern in _ENCOURAGE_PATTERNS):
                warnings.append(
                    f"{rel}:{line_no}: may encourage using real data — review: {line.strip()[:70]}"
                )


def main():
    failures, warnings = [], []
    check_essential(failures)
    check_datasets(failures, warnings)
    scan_patterns(failures, warnings)
    check_paste_instructions(warnings)

    if warnings:
        print("WARNINGS (human review — not a build failure):")
        for w in warnings:
            print(f"  - {w}")
        print("")

    if failures:
        print("VALIDATION FAILED:")
        for f in failures:
            print(f"  - {f}")
        print("")
        print("This validator is a guardrail, not a complete scanner. Fix the items above.")
        return 1

    print("Validation passed: essential files present, datasets valid, no high-confidence secrets.")
    print("Note: this is a guardrail, not a complete PII/secret scanner — keep reviewing PRs by hand.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
