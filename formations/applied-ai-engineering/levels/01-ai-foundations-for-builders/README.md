# Level 1 — AI Foundations for Builders

> **Status: draft v0.1.** First materials. More to come.

The conceptual and data foundation for anyone who will build with AI. **No LLM, no
chatbot, no RAG, no Agent.** This level installs the central discipline: **define
success before you build.**

## Guided labs

The real teaching material of Level 1. Do them in order — each is hands-on, no AI
required:

1. [Lab 01 — Framing & Baseline do AI Incident Assistant](./labs/01-framing-and-baseline/README.md)
   — frame the problem, a baseline without AI, a metric and a privacy note. ~30–45 min.
2. [Lab 02 — Dataset Understanding & Manual Baseline](./labs/02-dataset-understanding-and-manual-baseline/README.md)
   — inspect the synthetic dataset and design a deterministic manual baseline before using AI. ~45–60 min.
3. [Lab 03 — Implementing and Evaluating a Deterministic Baseline](./labs/03-deterministic-baseline/README.md)
   — *planned.* Turn the manual baseline into executable deterministic rules with a simple evaluation loop. Still no AI.

The sections below frame *why*; the labs are *how* you actually do it.

## Objective

Move from "AI is magic" to "I can frame a problem, choose a metric, define a
baseline without AI, and recognize leakage and PII".

## What you will build

The **v0** of the mother project (*AI Incident & Support Assistant*) — but without
any AI. Concretely, you produce:

- a clear **problem framing** (ideal outcome × model goal × success metric +
  **baseline without AI**),
- a minimal exploration of the synthetic dataset,
- a **privacy note**.

You answer one honest question with your own example: **"does this even need AI?"**

## Prerequisites

- Basic engineering fundamentals (Git, terminal, running commands).
- Basic Python (enough to read and run a small standard-library script).
- No prior AI/ML experience required.

> See the [canonical document](../../canonical/formacao-polaris-applied-ai-engineering-v0.1.md), Section 9, for the full level definition.

## Artifacts you produce

You fill these in inside the starter (you edit the starter's own copies; reusable
templates for the Lab 01 ones also live in [../../templates/](../../templates/)):

**Lab 01:**

- [`problem-framing.md`](../../../../starters/ai-incident-support-assistant/problem-framing.md)
  — the problem, success metric and baseline without AI.
- [`privacy-note.md`](../../../../starters/ai-incident-support-assistant/privacy-note.md)
  — that the data is synthetic and what must never be sent to a model.
- [`progress.md`](../../../../starters/ai-incident-support-assistant/progress.md)
  — what you ran and what you learned.

**Lab 02:**

- [`dataset-notes.md`](../../../../starters/ai-incident-support-assistant/dataset-notes.md)
  — what you saw in the dataset (fields, patterns, hard cases).
- [`manual-baseline.md`](../../../../starters/ai-incident-support-assistant/manual-baseline.md)
  — your 3–5 rule deterministic baseline and a metric.
- plus an update to `progress.md`.

All five are what `make evidence` checks for (presence, not quality) and what the
[Progress Contract](progress-contract.md) lists as the minimum to advance.

## How to use the starter

Use the
[AI Incident Support Assistant starter](../../../../starters/ai-incident-support-assistant/README.md).
It gives you a valid synthetic dataset and tests so you can focus on framing, not
plumbing.

```bash
cd starters/ai-incident-support-assistant
make setup    # checks Python, prints what to do
make test     # validates the synthetic dataset
make check    # runs the test and confirms success
```

## Basic commands

| Command | What it does |
|---|---|
| `make setup` | Checks your Python install and prints next steps. |
| `make test` | Runs the dataset validation test. |
| `make check` | Runs the test and prints a clear success message. |
| `make help` | Lists available commands. |

## Evidence checkpoint

Two different checks, two different jobs:

- `make check` proves the **starter works** (dataset valid) — your fast first success.
- `make evidence` proves the **minimum artifacts are present** — it does **not** grade
  quality and does **not** replace self-assessment.

To consider Level 1 *ready to advance*, you should have:

- Lab 01 done and Lab 02 done;
- `make evidence` passing;
- your rubric self-assessment at least at **"Good"** on the main criteria.

The full, explicit bar is in the
[Level 1 Progress Contract](progress-contract.md).

## Next

1. Do the first guided lab: [Lab 01 — Framing & Baseline](labs/01-framing-and-baseline/README.md).
2. Then [Lab 02 — Dataset Understanding & Manual Baseline](labs/02-dataset-understanding-and-manual-baseline/README.md).
3. Self-assess against the [rubric.md](rubric.md) and the [Progress Contract](progress-contract.md).
4. Stuck? [troubleshooting.md](troubleshooting.md).
