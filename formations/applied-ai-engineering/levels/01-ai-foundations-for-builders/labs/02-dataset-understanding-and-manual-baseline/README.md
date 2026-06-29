# Lab 02 — Dataset Understanding & Manual Baseline

> **Status: draft v0.1.** The second guided lab of Level 1.
>
> **Estimated time: 45–60 minutes.** **Prerequisite: [Lab 01](../01-framing-and-baseline/README.md).**

**Before using AI, prove that you understand the data and can define a simple
baseline.**

## What you will NOT do

- ❌ No LLM. ❌ No RAG. ❌ No embeddings. ❌ No Agent.
- ❌ No external API, no provider (OpenAI/Anthropic/Ollama/…), no cloud, no Docker.
- ❌ No framework (LangChain/LlamaIndex/…), no new dependencies.
- ❌ No real data of any kind — synthetic dataset only.

> **Still no AI — on purpose.** Lab 01 framed the problem. This lab makes you *look
> at the actual data* and write a deterministic baseline by hand. An AI approach
> only earns its place later, by beating a baseline you can measure. Understanding
> the data and a measurable baseline come **first**.

## What you will learn

- Inspect a synthetic JSONL dataset.
- Identify the useful fields.
- Describe recurring patterns.
- Find ambiguous or hard cases.
- Design deterministic manual rules.
- Define simple success metrics.
- Explain when AI might help and when it is unnecessary.

## Prerequisites

- You completed **Lab 01** (problem framing, privacy note, first conceptual baseline).
- Python 3 available (`python3`). The starter uses **only the standard library**.

## Main commands

Run from the **repo root** (the directory where you cloned this repo):

```bash
cd starters/ai-incident-support-assistant
make setup
make test
make check
make inspect-dataset
```

`make inspect-dataset` runs `scripts/inspect_dataset.py` (read-only). After you have
designed your own rules, you can compare against a deliberately weak reference:

```bash
make manual-baseline
```

## Where do I write my answers?

Edit these files inside the starter — not the templates:

- `starters/ai-incident-support-assistant/dataset-notes.md`
- `starters/ai-incident-support-assistant/manual-baseline.md`
- `starters/ai-incident-support-assistant/progress.md`

The templates under `formations/applied-ai-engineering/templates/` are reusable
references. For this lab, edit the starter files directly.

## Final artifacts

By the end you should have:

- `dataset-notes.md` — filled in;
- `manual-baseline.md` — filled in;
- `progress.md` — updated with commands run and what you learned;
- the output of inspecting the dataset (`make inspect-dataset`);
- a **manual baseline with 3–5 simple rules**;
- one **simple success metric**;
- a list of the **baseline's limitations**;
- a short explanation of **why LLM/RAG/Agent is not needed yet**.

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
