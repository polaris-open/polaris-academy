# AI Incident Support Assistant — starter

> **Status: draft v0.1.** A minimal starter to prove your first 30 minutes.

This is the starter for the
[Applied AI Engineering formation](../../formations/applied-ai-engineering/README.md),
**Level 1 — AI Foundations for Builders**.

## What this is

A tiny, honest starting point built around a **synthetic** incident dataset for a
fictional travel / booking / e-commerce support scenario. It exists so you can
begin **without** setting up an LLM, a cloud account or a paid API.

- **Synthetic data only.** No real logs, no customer data, no PII. See
  [`data/synthetic-incidents.jsonl`](data/synthetic-incidents.jsonl).
- **No LLM yet.** Level 1 is about framing and baselines, not models.
- **Standard library only.** No `pip install`, no virtualenv, no Docker, no
  framework.

## What it is for

It gives you a valid dataset and a test so that, in Level 1, you can focus on
**framing the problem, choosing a metric, and defining a baseline without AI** —
not on plumbing.

## Requirements

- Python 3 (`python3` or `python` on your PATH).
- `make` (ships with the Xcode Command Line Tools on macOS; install via your package
  manager on Linux).

## How to run

```bash
make setup   # checks your Python install and prints next steps
make test    # validates the synthetic dataset
make check   # runs the test and confirms success
```

If `make` is unavailable, you can run the test directly:

```bash
python3 tests/test_dataset.py
```

## What you should fill in

As you work through Level 1, fill in these files (the templates live in the
formation's [templates folder](../../formations/applied-ai-engineering/templates/)):

- [`problem-framing.md`](problem-framing.md) — the problem, success metric and
  baseline without AI. *(Lab 01)*
- [`privacy-note.md`](privacy-note.md) — confirm the data is synthetic and list what
  must never be sent to a model. *(Lab 01)*
- [`progress.md`](progress.md) — what you ran and what you learned. *(Lab 01)*
- [`dataset-notes.md`](dataset-notes.md) — what you saw in the dataset. *(Lab 02)*
- [`manual-baseline.md`](manual-baseline.md) — your deterministic baseline. *(Lab 02)*

## Checking your evidence

After you work through Lab 01 and Lab 02, run:

```bash
make evidence
```

This checks whether the minimum Level 1 evidence files are present and contain basic
signals of work. **It does not grade quality.** It only catches missing or obviously
incomplete evidence (e.g. a file you have not filled in yet). Use the lab rubrics,
self-assessment and examples to evaluate quality.

> On a fresh clone the artifact files are still templates, so `make evidence` will
> report them as not filled in — that is expected until you do the labs.

## What NOT to do

- Do not add an LLM, RAG, an Agent or a framework here.
- Do not add external APIs, Docker or cloud.
- Do not replace the synthetic dataset with real data of any kind.

> Demos are not production. This starter is deliberately minimal — its job is to get
> you started honestly, not to look impressive.
