# Expected Artifacts

By the end of this lab, you should have:

- `dataset-notes.md`
- `manual-baseline.md`
- updated `progress.md`
- evidence that the dataset was inspected
- a deterministic manual baseline
- one simple metric
- documented baseline limitations
- an explanation of why AI is not needed yet

## Expected final state

After this lab, the starter directory looks like this (your edited files plus the
shipped scripts and data):

```text
starters/ai-incident-support-assistant/
├── dataset-notes.md        # filled in
├── manual-baseline.md      # filled in
├── progress.md             # updated
├── scripts/
│   ├── inspect_dataset.py
│   └── manual_baseline.py
└── data/
    └── synthetic-incidents.jsonl
```

## What "done" means (minimum / good / 10-10 for Level 1)

> 10/10 here means "excellent for Level 1" — not production, not a specialist badge.

### `dataset-notes.md`
- **Minimum:** record count + field list, grounded in the actual dataset.
- **Good:** plus useful-for-triage fields, recurring patterns, and easy vs ambiguous cases.
- **10/10:** plus a clear statement of what the dataset can and cannot support.

### `manual-baseline.md`
- **Minimum:** at least 3 deterministic rules with signal and output.
- **Good:** 3–5 rules, a human-review rule, one metric, and honest weaknesses.
- **10/10:** plus a sharp "why not AI yet" argument and questions prepared for Lab 03.

### Metric
- **Minimum:** one metric is named.
- **Good:** it is measurable on this dataset.
- **10/10:** you explain what it does **and does not** capture.

### Evidence
- **Minimum:** you ran `make inspect-dataset` (or equivalent).
- **Good:** the output is reflected in `dataset-notes.md` / `progress.md`.
- **10/10:** another learner could reproduce your steps from your notes.
