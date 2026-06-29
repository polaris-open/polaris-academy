# Lab 01 — Instructions

> Step-by-step. Plan ~30–45 minutes. No AI, no external services, synthetic data
> only.

## Step 1 — Enter the starter

Run from the **repo root** (the directory where you cloned this repo):

```bash
cd starters/ai-incident-support-assistant
```

## Step 2 — Run the starter

```bash
make setup
make test
make check
```

You should see the dataset validation pass and a clear success message. Keep the
`make check` output — it is part of your evidence.

## Step 3 — Open the dataset

Open the synthetic dataset:

```text
data/synthetic-incidents.jsonl
```

Each line is one JSON incident with the fields `id`, `title`, `service`,
`severity`, `scenario`, `symptoms`, `expected_next_action` and `contains_pii`.
This is **synthetic data only** — no real logs, no customer data, no PII.

## Step 4 — Answer these questions

Read the incidents and answer (write the answers into your `progress.md`):

- Which **services** appear?
- Which **types of incidents** appear?
- Which **human decision** should this assistant support?
- Which **data is missing** that you would want?
- Which **risks** would appear if this were a *real* log instead of synthetic?

## Step 5 — Fill in your artifacts

Edit the starter's copies of these files:

- [`problem-framing.md`](../../../../../../starters/ai-incident-support-assistant/problem-framing.md)
- [`privacy-note.md`](../../../../../../starters/ai-incident-support-assistant/privacy-note.md)
- [`progress.md`](../../../../../../starters/ai-incident-support-assistant/progress.md)

## Step 6 — Define a baseline WITHOUT AI

Describe a simple approach that needs **no LLM**. Any of these is acceptable:

- keyword search over `symptoms`;
- a severity-based routing table;
- a static FAQ;
- a manual checklist;
- a simple rule by `service` + `severity`.

Write *which* baseline you chose and, honestly, how far it gets you. This is the bar
any future AI has to beat.

## Step 7 — Define a simple metric

Pick **one** metric you could actually observe. Examples:

- time to find the next action;
- correct first-suggestion rate;
- number of incidents that need escalation;
- severity classification accuracy;
- perceived quality from a human review.

Justify it by the **cost of being wrong** — not just "accuracy".

## Step 8 — Record final evidence

Make sure you have captured:

- the `make check` output;
- `problem-framing.md` filled in;
- `privacy-note.md` filled in;
- `progress.md` updated;
- a short explanation of the **baseline** you chose;
- a short explanation of the **metric** you chose.

Then grade yourself with [self-assessment.md](./self-assessment.md) and compare your
work against the [examples](./examples/good-submission.md).

## Common mistakes

- ❌ Starting with **RAG**.
- ❌ Starting with an **Agent**.
- ❌ Using an **LLM without a baseline**.
- ❌ Using **real data**.
- ❌ Choosing a **vague metric** ("make it better").
- ❌ Defining the **solution before the problem**.
- ❌ Confusing a **demo with a product**.
- ❌ Ignoring **privacy**.
