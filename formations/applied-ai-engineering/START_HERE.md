# Start here — Applied AI Engineering

> **Status: draft v0.1.** Self-paced first. You can do all of this alone.

This is the entry point for the **Applied AI Engineering** formation. It tells you
how to begin with Level 1 and the starter, what to read first, what to run first,
and what to deliver as your first evidence.

## How to start with Level 1

Level 1 is **AI Foundations for Builders**. It is conceptual and data-focused:
problem framing, metrics, data, basic Responsible AI and privacy. **There is no
LLM, no chatbot, no RAG and no Agent in Level 1.** The discipline it installs is:
*define success before you build.*

Go to
[levels/01-ai-foundations-for-builders/README.md](levels/01-ai-foundations-for-builders/README.md)
and follow its lab guide.

## How to use the starter

The starter is the
[AI Incident Support Assistant](../../starters/ai-incident-support-assistant/README.md).
It uses **only synthetic data**, has **no LLM**, and runs with the Python standard
library. It exists to prove your first 30 minutes.

```bash
cd starters/ai-incident-support-assistant
make setup
make test
make check
```

## What to read first

1. This file.
2. [Level 1 README](levels/01-ai-foundations-for-builders/README.md).
3. The Level 1 [lab guide](levels/01-ai-foundations-for-builders/lab-guide.md).
4. The starter's [README](../../starters/ai-incident-support-assistant/README.md).

## What to run first

```bash
make setup   # checks your Python and prints what to do
make test    # validates the synthetic dataset
make check   # runs the test and confirms success
```

If something breaks, read the Level 1
[troubleshooting](levels/01-ai-foundations-for-builders/troubleshooting.md).

## What to deliver as your first evidence

Fill in, in your own copy of the starter:

- [`problem-framing.md`](../../starters/ai-incident-support-assistant/problem-framing.md)
- [`privacy-note.md`](../../starters/ai-incident-support-assistant/privacy-note.md)
- [`progress.md`](../../starters/ai-incident-support-assistant/progress.md)

Your first evidence is: **setup/tests green + `problem-framing.md` and
`privacy-note.md` started + `progress.md` showing what you ran.**

## What NOT to do yet

- **Do not start with RAG.**
- **Do not start with Agents.**
- **Do not start with a framework.**
- **Do not use real data.** Synthetic data only.
- **Do not send sensitive data to LLMs.** (In Level 1 you do not call an LLM at
  all.)

> Why: Level 1 is about framing and baselines. Jumping to an LLM, RAG or a
> framework before you can define success and a baseline without AI is the most
> common way to waste the formation.
