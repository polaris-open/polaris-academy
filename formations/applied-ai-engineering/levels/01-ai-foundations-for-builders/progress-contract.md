# Level 1 Progress Contract

> **Status: draft v0.1.**

This document defines the **minimum** for considering Level 1 *ready to advance*. It
is a **self-paced progress contract** — a checklist you hold yourself to.

It is **not** a certification, **not** a grade, and **not** a guarantee of mastery.
`make evidence` can confirm that artifacts exist; only **you** (and the rubrics,
self-assessment and examples) can judge whether the work is actually good.

## Minimum to move forward

You can consider Level 1 done when:

- `make setup` passes;
- `make test` passes;
- `make check` passes;
- Lab 01 is complete;
- Lab 02 is complete;
- `make evidence` passes;
- `problem-framing.md` states a problem, a baseline without AI, and a metric;
- `privacy-note.md` confirms the data is synthetic and states the privacy rules;
- `dataset-notes.md` shows real understanding of the dataset (fields, patterns);
- `manual-baseline.md` has 3–5 deterministic rules and one metric;
- `progress.md` records commands run, decisions, and difficulties.

> Note: `make evidence` checks **presence**, not quality. The last five items above
> are yours to judge honestly with the lab rubrics and the worked examples.

## Blockers

Do **not** advance if:

- there is no baseline;
- there is no metric;
- you did not actually look at the dataset;
- you used an LLM/RAG/Agent in Level 1;
- you used real data of any kind;
- you cannot explain what `make check` validates;
- you cannot explain the limits of your baseline.

A blocker fails the checkpoint regardless of how complete everything else looks.

## Recommended next step

After you pass this contract, the planned next step is:

```text
Lab 03 — Implementing and Evaluating a Deterministic Baseline
```

Lab 03 is **planned, not yet available**. It will turn your manual baseline into
executable deterministic rules with a simple evaluation loop — still no LLM, no RAG,
no Agent.
