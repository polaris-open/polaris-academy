# Lab 01 — Review checklist

Use this for **self-review** or **peer review**. It is a yes/no pass over the work.
Anything in *Blocking issues* fails the lab until fixed, regardless of the rest.

## Checklist

- [ ] Is the problem clear?
- [ ] Is there a user / persona?
- [ ] Is the current workflow described?
- [ ] Is the baseline without AI plausible?
- [ ] Does the metric measure something observable?
- [ ] Does the privacy note block real data?
- [ ] Did the student avoid LLM / RAG / Agent in this lab?
- [ ] Is the evidence reproducible?
- [ ] Did `make check` pass?
- [ ] Was `progress.md` updated?

## Blocking issues

If any of these is true, the lab does **not** pass until corrected:

- ❌ Use of real data (logs, customer, corporate).
- ❌ Any secret or PII included.
- ❌ Solution starts with **RAG** without a baseline.
- ❌ Solution starts with an **Agent** without a workflow.
- ❌ No metric at all.
- ❌ The starter was not run.
- ❌ No evidence produced.

> Blocking issues are the honesty gate of self-study. A high score does not override
> a blocking issue.
