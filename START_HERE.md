# Start here

> **Status: draft v0.1.** Find your line, do the next 30 minutes, publish your
> first evidence.

This repo is **self-paced first**. Nothing below requires a human to unblock you.
Pick the row that sounds like you.

The first command never depends on a future version of the project. The only
commands you need to start exist in the starter today:

```bash
make setup
make test
make check
```

| I am / I want… | Next 30 minutes | First file | First command | First evidence | Main risk |
|---|---|---|---|---|---|
| **Just want to use AI better** | Read the formation intro; sketch one prompt workflow | [formations/applied-ai-engineering/README.md](formations/applied-ai-engineering/README.md) | — (no code) | One documented prompt workflow (a note/doc) | Thinking you are "building" |
| **Dev who wants to build with AI** | Do **Lab 01**: frame the problem + a baseline without AI | [Lab 01 — Framing & Baseline](formations/applied-ai-engineering/levels/01-ai-foundations-for-builders/labs/01-framing-and-baseline/README.md) | `make setup` → `make test` | Setup green + `problem-framing.md` + `progress.md` started | Treating an LLM as "just another API" and skipping evals |
| **Technical beginner** | Install your environment; first run of the starter | [starters/ai-incident-support-assistant/README.md](starters/ai-incident-support-assistant/README.md) | `make setup` → `make check` | First repo with README + tests green | Tutorial hell; skipping the baseline |
| **Data analyst / data scientist** | Run the starter tests; map what to skip | [formations/applied-ai-engineering/templates/problem-framing.md](formations/applied-ai-engineering/templates/problem-framing.md) | `make setup` → `make test` | `progress.md` + a plan (skip classic ML) | Underestimating that the gap is engineering, not ML |
| **Staff / principal** | Review the Level 1 framing; pick one decision to record | [formations/applied-ai-engineering/templates/adr-template.md](formations/applied-ai-engineering/templates/adr-template.md) | `make setup` | A draft ADR | Skipping hands-on and losing cost/failure intuition |
| **Product / business** | Read the layers + problem framing; write one trade-off memo | [formations/applied-ai-engineering/templates/problem-framing.md](formations/applied-ai-engineering/templates/problem-framing.md) | — (no code) | A "do we even need AI?" trade-off memo | Leading without understanding evals |
| **I want to do the Capstone** | Review Levels 1–3; open the starter | [formations/applied-ai-engineering/capstone/README.md](formations/applied-ai-engineering/capstone/README.md) | `make setup` → `make test` | `progress.md` + the Level 1 checklist | A happy-path demo with no failures or limits |

> **Rule of the first step:** for anyone starting to build, the first command is
> `make setup` / `make test` / `make check` — **not** `make demo`. Demos only make
> sense in later versions of the project, and **demos are not production**.

## Next steps

The concrete first thing to **do** is the first guided lab:

- **[Lab 01 — Framing & Baseline do AI Incident Assistant](formations/applied-ai-engineering/levels/01-ai-foundations-for-builders/labs/01-framing-and-baseline/README.md)** — ~30–45 min, no AI.

For the bigger picture:

1. Open the [Applied AI Engineering formation](formations/applied-ai-engineering/README.md).
2. Read its own [START_HERE.md](formations/applied-ai-engineering/START_HERE.md).
3. Start [Level 1 — AI Foundations for Builders](formations/applied-ai-engineering/levels/01-ai-foundations-for-builders/README.md).
