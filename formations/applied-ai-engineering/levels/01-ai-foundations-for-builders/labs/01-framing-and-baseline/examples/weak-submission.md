# Example — weak submission

> A deliberately **weak** Lab 01 submission, followed by why it is weak. Use it to
> recognize the failure pattern in your own work.

## The submission

**Problem:** Use AI to solve incidents automatically.

**Solution:** Build an Agent that reads incidents and fixes them. Later add RAG over
all our docs and maybe fine-tune a model.

**Metric:** Make incident handling better / faster.

**Privacy:** We'll plug in our real production logs so it's realistic.

**Baseline:** —

**Evidence:** —

## Why this is weak

- **Solution before problem.** It jumps to "an Agent" and "RAG" before defining what
  is actually hard or for whom. There is **no persona** and **no workflow**.
- **No baseline.** Nothing to beat, so "better" is meaningless.
- **Vague metric.** "Better / faster" is not observable — you cannot measure it.
- **Privacy failure (blocking).** "Real production logs" violates *synthetic data
  only*. This alone fails the lab.
- **Starts with Agent/RAG (blocking).** Exactly the Level 1 anti-pattern.
- **No evidence.** The starter was never run; there is nothing reproducible.

**Verdict:** redo. This is a wish, not a framing.
