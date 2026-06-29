# Level 1 — AI Foundations for Builders

> **Status: draft v0.1.** First materials. More to come.

The conceptual and data foundation for anyone who will build with AI. **No LLM, no
chatbot, no RAG, no Agent.** This level installs the central discipline: **define
success before you build.**

## First guided lab

This is the **first real teaching material** of Level 1 — a hands-on lab you can
finish in 30–45 minutes, no AI required. Start here:

[Lab 01 — Framing & Baseline do AI Incident Assistant](./labs/01-framing-and-baseline/README.md)

The sections below frame *why*; the lab is *how* you actually do it.

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

You fill in these files (templates live in
[../../templates/](../../templates/), and the starter ships copies you edit):

- [`problem-framing.md`](../../templates/problem-framing.md) — the problem, success
  metric and baseline without AI.
- [`privacy-note.md`](../../templates/privacy-note.md) — what the data is, that it
  is synthetic, and what must never be sent to a model.
- [`progress.md`](../../templates/progress.md) — what you ran and what you learned.

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

## Next

1. Do the first guided lab: [Lab 01 — Framing & Baseline](labs/01-framing-and-baseline/README.md).
2. Self-assess against the [rubric.md](rubric.md).
3. Stuck? [troubleshooting.md](troubleshooting.md).
