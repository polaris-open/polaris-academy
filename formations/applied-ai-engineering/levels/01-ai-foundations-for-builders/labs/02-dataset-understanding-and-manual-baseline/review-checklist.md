# Lab 02 — Review checklist

Use this for **self-review** or **peer/mentor review**. It is a yes/no pass over the
work. Anything in *Blocking issues* fails the lab until fixed.

## Checklist

- [ ] Did the learner inspect the actual synthetic dataset?
- [ ] Are the notes grounded in dataset evidence (not assumptions)?
- [ ] Is the baseline deterministic?
- [ ] Are the rules understandable?
- [ ] Is the metric simple and relevant?
- [ ] Are the limitations honest?
- [ ] Did the learner avoid overclaiming?
- [ ] Did the learner avoid LLM/RAG/Agent?
- [ ] Are no real data / secrets / PII included?
- [ ] Would the next lab be able to compare an AI approach against this baseline?

## Blocking issues

If any of these is true, the lab does **not** pass until corrected:

- ❌ Use of real data (logs, customer, corporate).
- ❌ Any secret or PII included.
- ❌ Baseline is not deterministic (rules cannot be followed by hand).
- ❌ No metric at all.
- ❌ Used an LLM/RAG/Agent.
- ❌ Notes are not grounded in the dataset (no evidence the data was inspected).

> Blocking issues are the honesty gate of self-study. A high score does not override
> a blocking issue.
