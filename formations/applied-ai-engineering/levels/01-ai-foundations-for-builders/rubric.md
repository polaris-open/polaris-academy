# Rubric — Level 1 lab (Framing & Baseline)

> **Status: draft v0.1.** Self-assessment is **formative** at Level 1. Use it
> honestly: compare your work against the descriptions below, not against "I felt
> good about it".

Three bars: **Minimum**, **Good**, **10/10**. To advance, aim for at least
**Good**. A 10/10 is the calibration target, not a gate.

## Criteria

### 1. Problem framing

| Level | What it looks like |
|---|---|
| **Minimum** | A problem statement exists and names a user and a desired outcome. |
| **Good** | Problem, persona, current workflow, pain and desired outcome are clear and specific to the incident dataset. |
| **10/10** | Plus a short, honest argument about *whether this needs AI at all*, with at least one place a simple rule could beat an LLM. |

### 2. Baseline without AI

| Level | What it looks like |
|---|---|
| **Minimum** | A non-AI approach is mentioned. |
| **Good** | The baseline is concrete (a rule/lookup someone could implement) and you estimate how far it gets. |
| **10/10** | The baseline is the explicit bar future AI must beat, and you state when it would be enough on its own. |

### 3. Metric

| Level | What it looks like |
|---|---|
| **Minimum** | A metric is named. |
| **Good** | The metric is measurable on this dataset and justified by the cost of being wrong (not just "accuracy"). |
| **10/10** | You explain a failure mode the metric would and would not catch, and why you chose it over an alternative. |

### 4. Privacy note

| Level | What it looks like |
|---|---|
| **Minimum** | The note confirms the data is synthetic. |
| **Good** | PII check + sensitive-data check done; lists what must not be sent to a model. |
| **10/10** | Plus provider considerations and a clear rule for handling any future non-synthetic data (don't). |

### 5. README / progress clarity

| Level | What it looks like |
|---|---|
| **Minimum** | `progress.md` lists what you ran. |
| **Good** | A third person could reproduce your steps from the README and `progress.md`. |
| **10/10** | Difficulties and decisions are recorded honestly (useful later as input to a debugging diary). |

## Blocker

You are **not** ready to advance if there is **no defined baseline** or **no
justified metric**. Those two are the heart of Level 1.

## Self-assessment

In your `progress.md`, write one line per criterion: which bar you think you hit and
why. Honesty here is the whole exercise — there is no grader at Level 1.
