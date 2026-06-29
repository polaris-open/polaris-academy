# Formação Polaris em Applied AI Engineering

**Applied AI Engineering Formation**

> *Do fundamento crítico à construção de aplicações de IA avaliáveis, seguras e
> defensáveis.*
> *(From critical foundations to building AI applications that are evaluable,
> secure and defensible.)*

> **Status: draft v0.1.** This is the architecture of the formation, validated by
> a first cohort and self-taught learners before it becomes v1. It is **not** the
> complete course.

## What this formation is

A **project-based, self-paced** path that takes someone with an engineering base
to **build, evaluate and operate real AI applications** (LLM apps, RAG, tool
calling) — with measurement, cost, security and governance. You learn by building
**one system that grows**: the *AI Incident & Support Assistant*.

## What this formation is not

- Not "specialist in 30 days". It does not promise a job or a title.
- Not an ML researcher track (it gives a base and points to the path, but that is
  not the focus).
- Not a course where you start by wiring a framework. You start by **framing a
  problem and defining a baseline without AI**.

## The central thesis

```text
AI Engineering is Software Engineering with probabilistic models in the middle.
```

AI engineering does not re-teach generic engineering — it **re-applies**
fundamentals (tests, observability, security, APIs, persistence) to probabilistic
systems. Tests become **evals**; logs become **LLM tracing with cost/token**; error
handling includes **hallucination and abstention**; security includes **prompt
injection** (external content is **data, not command**).

A few distinctions this formation refuses to blur:

- **RAG is not a layer.** It is an architecture over LLMs.
- **Semantic search is not RAG.**
- **Tool calling is not Agent.** Controlled tool calling is the default; autonomy is
  a justified exception.
- **Production is not demo.** "It worked once" is never "it is ready".
- **Specialist is a direction of maturity, not a title promise.**

## Structure

The core is three named levels, then a capstone:

1. **[Level 1 — AI Foundations for Builders](levels/01-ai-foundations-for-builders/README.md)**
   — layers of AI, problem framing, metrics, data, basic Responsible AI. **No LLM,
   no RAG, no Agent.**
2. **[Level 2 — AI Builder](levels/02-ai-builder/README.md)** — *planned.*
3. **[Level 3 — AI Application Engineer](levels/03-ai-application-engineer/README.md)**
   — *planned.*
4. **[Applied AI Engineering Capstone](capstone/README.md)** — *planned.*

## Links

- **Canonical document (architecture, not the course):**
  [canonical/formacao-polaris-applied-ai-engineering-v0.1.md](canonical/formacao-polaris-applied-ai-engineering-v0.1.md)
  — see [canonical/README.md](canonical/README.md) for what it is and is not.
- **Starter you run first:**
  [starters/ai-incident-support-assistant/README.md](../../starters/ai-incident-support-assistant/README.md)
- **Formation entry point:** [START_HERE.md](START_HERE.md)

## How to start

Read [START_HERE.md](START_HERE.md) for this formation, then begin Level 1 with the
[starter](../../starters/ai-incident-support-assistant/README.md):

```bash
make setup
make test
make check
```
