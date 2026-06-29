# Lab 02 — Instructions

> Step-by-step. Plan ~45–60 minutes. No AI, no external services, synthetic data
> only.

## Step 0 — Start from Lab 01 outputs

Before starting, make sure you completed [Lab 01](../01-framing-and-baseline/README.md).

You should already have:

- problem framing;
- privacy note;
- progress notes;
- a first conceptual baseline idea.

## Step 1 — Enter the starter

Run from the **repo root**:

```bash
cd starters/ai-incident-support-assistant
```

## Step 2 — Run the starter checks

```bash
make setup
make test
make check
```

## Step 3 — Inspect the dataset

Use the read-only inspection script:

```bash
make inspect-dataset
# equivalent to: python3 scripts/inspect_dataset.py
```

It prints the record count, the fields, simple counts for categorical fields
(e.g. `severity`), the most common values in list fields (e.g. `symptoms`), and a
few sample IDs.

If you prefer to look by hand, these standard tools also work:

```bash
wc -l data/synthetic-incidents.jsonl              # how many records
head -n 1 data/synthetic-incidents.jsonl          # look at one record
head -n 1 data/synthetic-incidents.jsonl | python3 -m json.tool   # pretty-print it
```

## Step 4 — Fill `dataset-notes.md`

Open `dataset-notes.md` and answer:

- What file did you inspect?
- How many records are there?
- What fields appear in each record?
- Which fields seem useful for triage?
- What recurring scenarios exist?
- Which examples are easy?
- Which examples are ambiguous?
- What should never be inferred from this dataset?

Ground every answer in what you actually saw — not in what you assume a real
incident dataset would contain.

## Step 5 — Design a manual baseline

Open `manual-baseline.md`. Your baseline must be **deterministic, simple and
explainable** — rules a person could follow by hand. Examples of acceptable rules
(adapt them to the *actual* synthetic dataset, do not copy blindly):

- if the symptoms or scenario mention "DLQ" / "dead letter", classify as a
  queue/reprocessing issue;
- if they mention a timeout or high latency (e.g. "p99", "504"), classify as a
  latency/dependency issue;
- if they mention a stale cache, classify as a cache/staleness issue;
- if they mention payment, refund, invoice or currency, require human review;
- if `severity` is `critical`, require human review regardless of category.

Write **3–5 rules**. For each, record the signal, the output, and *why the rule
exists*.

## Step 6 — Define a metric

Pick **one** simple metric, for example:

- coverage (share of records your rules classify at all);
- manual accuracy on a small sample you label by hand;
- number of cases requiring human review;
- false-confidence count (rules that would fire on the wrong case);
- percentage of records with a clear, single matching rule.

Explain why the metric is useful **and** why it is insufficient on its own.

## Step 7 — Compare baseline vs the AI temptation

In `manual-baseline.md`, write why using an LLM/RAG/Agent *now* would be premature.
The expected reasoning:

- we do not yet fully understand the dataset;
- without this baseline there is nothing for AI to beat;
- there is not yet a metric to judge "better";
- a simpler rule may already solve part of the problem;
- AI should improve over a known baseline, not replace thinking.

## Step 8 — (Optional) compare with the reference baseline

After you have written your own rules, you may run a deliberately weak reference:

```bash
make manual-baseline
```

It is **not** the answer — it is one possible weak baseline, useful only for
comparison. Note where your rules and its rules differ.

## Step 9 — Update progress

Update `progress.md` with:

- commands run;
- what you learned about the dataset;
- the baseline you chose;
- limitations found;
- next questions.

## Common mistakes

- ❌ "I looked at the dataset and it seems fine" (no evidence, no specifics).
- ❌ Vague rules that cannot be followed deterministically.
- ❌ No metric.
- ❌ Reaching for an LLM/RAG/Agent before a baseline exists.
- ❌ No honest list of limitations.
- ❌ Using or inventing real data.
