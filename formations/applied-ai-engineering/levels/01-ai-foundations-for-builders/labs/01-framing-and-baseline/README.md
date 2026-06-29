# Lab 01 — Framing & Baseline do AI Incident Assistant

> **Status: draft v0.1.** This is the **first real guided lab** of Level 1 — the
> point where the formation stops describing and starts being *done*.
>
> **Estimated time: 30–45 minutes.**

## Objective

Prove that you can take a messy-looking problem (an incident/support assistant) and,
**before touching any AI**, produce: a clear problem framing, a baseline that needs
no AI, a simple success metric, and an honest privacy note — all backed by
reproducible evidence.

## What you will do

- Run the starter and confirm its synthetic dataset is valid.
- Read the synthetic incidents and understand the data.
- Fill in `problem-framing.md`, `privacy-note.md` and `progress.md`.
- Define a **baseline without AI** and a **simple metric**.
- Capture concrete evidence (the `make check` output + your filled artifacts).

## What you will NOT do

- ❌ No LLM. ❌ No RAG. ❌ No Agent.
- ❌ No external API, no cloud, no Docker, no framework, no new dependencies.
- ❌ No real data of any kind.

> **This lab uses no AI — on purpose.** Trying to wire an LLM here is the headline
> anti-pattern of Level 1. The skill being trained is *defining success before
> building*. Before AI comes problem clarity; before RAG comes understanding the
> data; before an Agent comes a workflow; before production comes a baseline and a
> way to measure it.

## Prerequisites

- Basic terminal/Git and the ability to run commands.
- Python 3 available (`python3`). The starter uses **only the standard library**.
- No prior AI/ML experience needed.

## Main commands

```bash
cd starters/ai-incident-support-assistant
make setup
make test
make check
```

## Final artifacts

By the end you will have:

- `problem-framing.md` — filled in (problem, persona, workflow, metric, baseline).
- `privacy-note.md` — filled in (synthetic confirmation + what must never be sent).
- `progress.md` — updated with commands run and what you learned.
- The `make check` output as evidence.
- A short written **baseline without AI** and a short written **success metric**.

## Where to go next

1. Follow the step-by-step: [instructions.md](./instructions.md).
2. Check what "done" means: [expected-artifacts.md](./expected-artifacts.md).
3. Grade yourself honestly: [self-assessment.md](./self-assessment.md).
4. Self/peer review: [review-checklist.md](./review-checklist.md).
5. Calibrate against worked examples:
   [weak](./examples/weak-submission.md) ·
   [good](./examples/good-submission.md) ·
   [excellent](./examples/excellent-submission.md).

Stuck? See the Level 1 [troubleshooting](../../troubleshooting.md). Community is
support, not dependency — the lab is designed to be doable alone.
