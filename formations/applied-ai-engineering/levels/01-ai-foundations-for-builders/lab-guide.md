# Lab — Framing & Baseline do Incident Assistant

> **Status: draft v0.1.** Level 1, first lab.

## Goal

Define the **problem, success, metric, a baseline without AI, and the privacy
risks** for the *AI Incident & Support Assistant* — using only the synthetic
dataset.

**You do not implement an LLM in this lab. No RAG. No Agent.** The whole point is to
prove you can frame a problem and reason about a baseline *before* reaching for a
model.

## Before you start

```bash
cd starters/ai-incident-support-assistant
make setup
make test
```

You should see the dataset validation pass. Open
[`data/synthetic-incidents.jsonl`](../../../../starters/ai-incident-support-assistant/data/synthetic-incidents.jsonl)
and read a few incidents. This is **synthetic data only** — no real logs, no
customer data, no PII.

## Steps

### 1. Understand the data (10 min)

- Read every incident in the dataset. Each line is one JSON incident with fields
  like `title`, `service`, `severity`, `scenario`, `symptoms`,
  `expected_next_action` and `contains_pii`.
- Note the distribution of `severity`. Which services appear? What kinds of
  `expected_next_action` show up?
- Write 3 observations in your `progress.md`.

### 2. Frame the problem (10 min)

Open your copy of [`problem-framing.md`](../../../../starters/ai-incident-support-assistant/problem-framing.md)
and fill in:

- **Problem statement** — what is actually hard for the on-call/support person?
- **User/persona** — who is helped?
- **Current workflow** and **pain**.
- **Desired outcome** — what does success look like for the *user*, not the model.

### 3. Choose a success metric (5 min)

- Pick one metric you could actually measure (e.g. "% of incidents where the
  suggested next action matches `expected_next_action`").
- Justify it by the **cost of being wrong**. Why this metric and not raw accuracy?

### 4. Define a baseline WITHOUT AI (10 min)

- Describe a simple rule-based or lookup approach that needs **no LLM** (e.g. map
  `service` + `severity` to a default next action; keyword match on `symptoms`).
- Estimate, honestly, how far that baseline gets you. This is the bar any future AI
  has to beat.
- Record it in `problem-framing.md` under **Baseline without AI**.

### 5. Write the privacy note (5 min)

Open your copy of [`privacy-note.md`](../../../../starters/ai-incident-support-assistant/privacy-note.md)
and fill in:

- which dataset you used,
- confirmation that it is **synthetic**,
- a PII check and a sensitive-data check,
- **what must never be sent to a model**.

### 6. Answer the honest question

In one short paragraph in `problem-framing.md`: **does this need AI at all?** Where
might a simple rule beat an LLM? Where might AI genuinely help?

## First evidence (what to deliver)

- `problem-framing.md` filled in (incl. metric + baseline without AI).
- `privacy-note.md` filled in.
- `progress.md` showing the commands you ran and what you learned.
- Tests green (`make test` / `make check`).

## What NOT to do

- Do not call an LLM. Do not add RAG. Do not add an Agent.
- Do not add a framework or external API.
- Do not use real data of any kind.

When you are done, self-assess with [rubric.md](rubric.md).
