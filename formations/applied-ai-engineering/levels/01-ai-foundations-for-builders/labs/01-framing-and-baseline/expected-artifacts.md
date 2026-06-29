# Lab 01 — Expected artifacts

These are the artifacts you must produce. For each one: what it is for, what it must
contain, and what *minimum*, *good* and *10/10* look like **at Level 1**.

> 10/10 here means "excellent for Level 1" — not "production-ready". Demos are not
> production.

## 1. `problem-framing.md`

- **Purpose:** force clarity about the problem before any solution.
- **Must contain:** problem statement, user/persona, current workflow, pain,
  desired outcome.
- **Minimum:** a problem statement and a named user.
- **Good:** all fields filled, specific to the incident dataset.
- **10/10:** plus an explicit "does this even need AI?" paragraph naming where a
  simple rule could win.

## 2. `privacy-note.md`

- **Purpose:** make "synthetic data only" a checked fact, not a vibe.
- **Must contain:** dataset used, synthetic confirmation, PII check, sensitive-data
  check, what must never be sent to a model.
- **Minimum:** confirms the data is synthetic.
- **Good:** PII + sensitive-data checks done; lists what must not leave the machine.
- **10/10:** plus provider considerations and a rule for any future non-synthetic
  data (don't use it).

## 3. `progress.md`

- **Purpose:** make progress visible without a grader.
- **Must contain:** commands run, observations about the data, difficulties, next
  steps.
- **Minimum:** lists the commands you ran.
- **Good:** a third person could reproduce your steps.
- **10/10:** records decisions and difficulties honestly (useful later as a
  debugging-diary seed).

## 4. `make check` output

- **Purpose:** reproducible evidence the starter runs on your machine.
- **Must contain:** the success line from `make check`.
- **Minimum:** the command ran.
- **Good:** output captured in `progress.md`.
- **10/10:** you can explain what the check actually validates.

## 5. Baseline without AI

- **Purpose:** the bar any future AI must beat.
- **Must contain:** which baseline (keyword search, routing table, FAQ, checklist,
  rule by service+severity) and how far it gets.
- **Minimum:** a baseline is named.
- **Good:** it is concrete enough that someone could implement it.
- **10/10:** you state when the baseline alone would be enough — and when it would
  not.

## 6. Success metric

- **Purpose:** define what "better" means, measurably.
- **Must contain:** one metric and why it fits the cost of being wrong.
- **Minimum:** a metric is named.
- **Good:** it is observable on this dataset.
- **10/10:** you name a failure mode the metric would and would not catch.

## 7. Risks and limits

- **Purpose:** show honesty about what this is not.
- **Must contain:** privacy risks, data gaps, and the limits of your baseline.
- **Minimum:** at least one risk is named.
- **Good:** privacy + data-gap risks listed.
- **10/10:** you connect risks to decisions (e.g. why you would not send field X to
  a model later).
