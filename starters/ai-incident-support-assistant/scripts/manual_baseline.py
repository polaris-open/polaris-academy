#!/usr/bin/env python3
"""A WEAK, deterministic manual baseline over the synthetic incident dataset.

Standard library only. No network, no LLM, no machine learning, no probabilities.
Read-only: this script never modifies any file.

This is NOT a model and NOT artificial intelligence. It is a handful of explicit
keyword rules written in plain Python. It exists for one reason: to give a future AI
approach something concrete to beat. It makes **no accuracy promise** — it will be
wrong on cases it does not cover, which is exactly the point.

The rules below are deliberately simple and illustrative. They are *one possible*
baseline. In the lab you design your own rules first (in `manual-baseline.md`), then
compare. Do not treat this file as "the answer".
"""

import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.normpath(os.path.join(HERE, os.pardir, "data", "synthetic-incidents.jsonl"))


def text_of(record):
    """Join the human-readable fields into one lowercased string for keyword rules."""
    parts = [str(record.get("title", "")), str(record.get("scenario", ""))]
    symptoms = record.get("symptoms", [])
    if isinstance(symptoms, list):
        parts.extend(str(s) for s in symptoms)
    return " ".join(parts).lower()


def classify(record):
    """Return (category, needs_human_review) using explicit, deterministic rules."""
    text = text_of(record)
    severity = str(record.get("severity", "")).lower()

    # Rule 1: anything critical always goes to a human, regardless of category.
    needs_human_review = severity == "critical"

    # Rule 2: coarse category by keyword. First match wins (order is explicit).
    if "dlq" in text or "dead letter" in text or "dead-letter" in text:
        category = "queue/reprocessing"
    elif any(k in text for k in ("timeout", "latency", "p99", "504", "503", "502")):
        category = "latency/dependency"
    elif "cache" in text or "stale" in text:
        category = "cache/staleness"
    elif "retry" in text:
        category = "retry/overload"
    elif any(k in text for k in ("payment", "refund", "invoice", "currency", "exchange rate")):
        category = "billing/payment"
        needs_human_review = True  # money-related: always review
    else:
        category = "uncategorized"
        needs_human_review = True  # unknown: do not guess, send to a human

    return category, needs_human_review


def main():
    if not os.path.isfile(DATASET):
        print(f"WARNING: dataset file not found at {DATASET}")
        return

    categories = Counter()
    review = 0
    total = 0
    with open(DATASET, "r", encoding="utf-8") as handle:
        for raw in handle:
            line = raw.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            total += 1
            category, needs_review = classify(record)
            categories[category] += 1
            if needs_review:
                review += 1

    print("Manual baseline (WEAK, deterministic, rule-based — NOT AI):")
    print(f"  Records classified: {total}")
    print("  By category:")
    for category, n in categories.most_common():
        print(f"    - {category}: {n}")
    print(f"  Needs human review: {review} / {total}")
    print("\nReminder: this baseline is intentionally weak. It has no accuracy guarantee")
    print("and will miss cases. Its job is to be a measurable bar for later AI work.")


if __name__ == "__main__":
    main()
