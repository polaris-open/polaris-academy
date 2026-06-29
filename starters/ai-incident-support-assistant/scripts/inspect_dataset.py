#!/usr/bin/env python3
"""Inspect the synthetic incident dataset.

Standard library only. No network, no LLM, no external services. Read-only: this
script never modifies any file.

It prints a small, honest summary so you can understand the data before building
anything:
  * dataset path and record count
  * the top-level fields that appear
  * simple counts for categorical (string/bool) fields
  * the most common values of list fields (e.g. symptoms)
  * a few sample IDs

It is tolerant of the real dataset: it does not assume specific field names and
warns (without crashing) on a missing file or an invalid JSON line.
"""

import json
import os
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.normpath(os.path.join(HERE, os.pardir, "data", "synthetic-incidents.jsonl"))

# A string/bool field is summarized as categorical only if its values are short and
# repeat. Free text (titles, scenarios) and all-unique identifiers are skipped on
# purpose, and just listed by name so nothing is hidden.
MAX_DISTINCT_FOR_CATEGORICAL = 12
MAX_VALUE_LEN_FOR_CATEGORICAL = 40
TOP_LIST_VALUES = 5


def is_categorical(values):
    if not values or not all(isinstance(v, (str, bool)) for v in values):
        return False
    if any(isinstance(v, str) and len(v) > MAX_VALUE_LEN_FOR_CATEGORICAL for v in values):
        return False  # free text
    distinct = set(values)
    if len(distinct) > MAX_DISTINCT_FOR_CATEGORICAL:
        return False
    if len(distinct) == len(values) and len(values) > 6:
        return False  # looks like an identifier / all unique
    return True


def load_records(path):
    records = []
    if not os.path.isfile(path):
        print(f"WARNING: dataset file not found at {path}")
        return records
    with open(path, "r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                print(f"WARNING: line {line_no} is not valid JSON ({error}); skipping")
    return records


def ordered_fields(records):
    fields = OrderedDict()
    for record in records:
        if isinstance(record, dict):
            for key in record:
                fields[key] = True
    return list(fields)


def main():
    rel = os.path.relpath(DATASET, os.getcwd())
    print(f"Dataset: {rel}")

    records = load_records(DATASET)
    print(f"Records: {len(records)}")
    if not records:
        print("No records to inspect. Run 'make test' first, or check the dataset path.")
        return

    fields = ordered_fields(records)
    print("Fields: " + ", ".join(fields))

    summarized = set()

    print("\nCategorical summaries (short, repeating string/bool fields):")
    any_categorical = False
    for field in fields:
        values = [r.get(field) for r in records if isinstance(r, dict) and field in r]
        if is_categorical(values):
            any_categorical = True
            summarized.add(field)
            counts = Counter(values)
            rendered = ", ".join(f"{val}={n}" for val, n in counts.most_common())
            print(f"  - {field}: {rendered}")
    if not any_categorical:
        print("  (none detected)")

    print(f"\nMost common values in list fields (top {TOP_LIST_VALUES}):")
    any_list = False
    for field in fields:
        values = [r.get(field) for r in records if isinstance(r, dict) and field in r]
        list_values = [v for v in values if isinstance(v, list)]
        if list_values:
            any_list = True
            summarized.add(field)
            flat = Counter(item for sub in list_values for item in sub if isinstance(item, str))
            top = "; ".join(f"{item} ({n})" for item, n in flat.most_common(TOP_LIST_VALUES))
            print(f"  - {field}: {top if top else '(empty)'}")
    if not any_list:
        print("  (none detected)")

    not_summarized = [f for f in fields if f not in summarized]
    if not_summarized:
        print("\nFree-text / identifier fields (not summarized): " + ", ".join(not_summarized))

    if records and isinstance(records[0], dict) and "id" in records[0]:
        sample = [str(r.get("id")) for r in records[:5] if isinstance(r, dict)]
        print("\nSample IDs: " + ", ".join(sample))


if __name__ == "__main__":
    main()
