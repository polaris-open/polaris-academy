# Example — good submission

> A **good** Lab 01 submission, followed by why it is good. Solid Level 1 work.

## The submission

**Problem:** When a booking incident comes in (e.g. payment authorized but ticket
not issued), the on-call engineer spends several minutes figuring out which service
is involved and what the first action should be.

**Persona:** On-call engineer during a support rotation, not an AI specialist.

**Current workflow:** Reads the alert, opens a few dashboards, searches a runbook
wiki, guesses the owning service, then asks in chat.

**Desired outcome:** Faster, more consistent "first next action" for an incident.

**Baseline without AI:** A routing table by `service` + `severity` that maps to a
default next action (e.g. `ticketing-service` + `high` → "check the DLQ and replay
the issuance message"). Covers the common cases; misses unusual combinations.

**Metric:** Correct first-suggestion rate — does the suggested next action match
`expected_next_action`? Chosen because a wrong first action wastes the most time.

**Privacy note:** Dataset is `synthetic-incidents.jsonl`, confirmed synthetic
(`contains_pii: false` on every row). No real logs. Nothing would be sent to a model
in this lab.

**Limitations:** The routing table is brittle for new services; the dataset is small
and may not represent real traffic.

**Evidence:** `make check` output captured in `progress.md`; `problem-framing.md` and
`privacy-note.md` filled in.

## Why this is good

- **Clear problem and persona**, grounded in the actual dataset.
- **A real baseline** that someone could implement — and an honest note on where it
  breaks.
- **An observable metric** tied to the cost of being wrong.
- **A correct privacy note** that blocks real data.
- **Limitations acknowledged** — no overclaiming.

**Verdict:** good. To reach excellent, it would add an explicit "why AI is not needed
yet" argument and a sharper note on what the metric would miss.
