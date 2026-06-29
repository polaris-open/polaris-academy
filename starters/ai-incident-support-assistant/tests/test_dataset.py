#!/usr/bin/env python3
"""Validate the synthetic incident dataset.

Standard library only. No external dependencies, no LLM, no network.

Checks:
  * the dataset file exists
  * every line is valid JSON
  * every incident has the required fields
  * contains_pii is False for every incident
  * id is not empty
  * severity is one of: low, medium, high, critical
  * there are at least 5 incidents
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, os.pardir, "data", "synthetic-incidents.jsonl")

REQUIRED_FIELDS = [
    "id",
    "title",
    "service",
    "severity",
    "scenario",
    "symptoms",
    "expected_next_action",
    "contains_pii",
]
VALID_SEVERITIES = {"low", "medium", "high", "critical"}
MIN_INCIDENTS = 5


def fail(message):
    print("FAIL: " + message)
    sys.exit(1)


def main():
    if not os.path.isfile(DATA_PATH):
        fail("dataset file not found at %s" % os.path.abspath(DATA_PATH))

    incidents = []
    with open(DATA_PATH, "r", encoding="utf-8") as handle:
        for line_number, raw in enumerate(handle, start=1):
            line = raw.strip()
            if not line:
                continue  # tolerate blank lines
            try:
                record = json.loads(line)
            except json.JSONDecodeError as error:
                fail("line %d is not valid JSON: %s" % (line_number, error))

            if not isinstance(record, dict):
                fail("line %d is not a JSON object" % line_number)

            for field in REQUIRED_FIELDS:
                if field not in record:
                    fail("line %d is missing required field '%s'" % (line_number, field))

            if record["contains_pii"] is not False:
                fail("line %d has contains_pii that is not false" % line_number)

            if not str(record["id"]).strip():
                fail("line %d has an empty id" % line_number)

            if record["severity"] not in VALID_SEVERITIES:
                fail(
                    "line %d has invalid severity '%s' (allowed: %s)"
                    % (line_number, record["severity"], ", ".join(sorted(VALID_SEVERITIES)))
                )

            incidents.append(record)

    if len(incidents) < MIN_INCIDENTS:
        fail("expected at least %d incidents, found %d" % (MIN_INCIDENTS, len(incidents)))

    print("OK: %d synthetic incidents validated, all fields present, no PII." % len(incidents))


if __name__ == "__main__":
    main()
