# Example — excellent submission (10/10 for Level 1)

> An **excellent** Lab 02 submission, followed by why it is excellent. "10/10 for
> Level 1" means excellent *data understanding and baseline design* — not production,
> not a specialist badge.

## The submission

**Dataset notes:** Inspected `data/synthetic-incidents.jsonl` via `make inspect-dataset`
and by reading each record. 8 synthetic records. Fields: `id`, `title`, `service`,
`severity`, `scenario`, `symptoms` (list of short strings), `expected_next_action`,
`contains_pii`. Triage-useful: `service`, `severity`, `symptoms`/`scenario` keywords.
`severity`: high=3, critical=2, medium=2, low=1. `contains_pii` is `false` on all 8 —
confirmed synthetic.

**Recurring patterns:** (1) queue / dead-letter reprocessing (INC-0001, INC-0006);
(2) latency / dependency timeouts (INC-0002); (3) cache staleness (INC-0003, INC-0008);
(4) retry storms / overload (INC-0007); (5) money-related (refunds, currency:
INC-0004, INC-0008).

**Easy cases:** INC-0001 (explicit "DLQ"), INC-0002 (explicit "p99 latency", "504").
**Ambiguous cases:** INC-0008 mentions both a stale cache *and* currency/invoice — it
matches two rules; INC-0005 ("search results empty after reindex") fits no keyword
rule cleanly.

**Baseline (deterministic, first match wins):**

| Rule | Signal | Output | Why |
| --- | --- | --- | --- |
| 1 | "DLQ" / "dead letter" | queue/reprocessing | clearest, most frequent signal |
| 2 | "timeout"/"latency"/"p99"/"50x" | latency/dependency | distinct operational class |
| 3 | "cache"/"stale" | cache/staleness | common and self-resolving pattern |
| 4 | "retry" | retry/overload | overload needs backoff, not reprocessing |
| 5 | payment/refund/invoice/currency | → human review | money: never auto-resolve |
| — | `severity == critical` | → human review | high blast radius, regardless of class |

**Metric:** coverage (share matched by a rule) **and** the count needing human
review. On this dataset: 6/8 matched a category rule; 2 fell through to
"uncategorized → human review"; money/critical cases routed to review.

**Why this metric, and its blind spot:** coverage is observable and cheap, but it
does **not** measure whether the chosen category is *correct* — a rule can fire on
the wrong case ("false confidence"). That gap is exactly what a later, *measured* AI
approach would have to improve.

**Limitations:** tiny dataset; keyword rules are brittle to wording; multi-match
cases (INC-0008) need a tie-break; no-match cases (INC-0005) are real and expected.

**Why not AI yet:** the dataset is small and now understood; a five-rule baseline
already classifies most cases and safely routes the rest to a human. An LLM now would
add cost, latency and a hallucination surface with **no measured gain** — and there
would be no baseline or metric to prove it helped.

**Questions for Lab 03:** Where does the baseline fail that an AI approach could fix?
How would we label a small golden set to measure category correctness, not just
coverage? Which cases must *always* stay with a human regardless of model quality?

## Why this is excellent

- **Evidence-driven** data understanding with concrete record references.
- **Ambiguous and no-match cases named**, not hidden.
- **A 5-rule deterministic baseline** with an explicit tie-break order and a reason
  per rule.
- **A metric that knows its own blind spot.**
- **A strong "why not AI yet"** tied to cost, measurement and safety.
- **Forward-looking questions** that set up Lab 03 cleanly.

**Verdict:** excellent for Level 1. The natural next step (Lab 03) is to label a small
golden set and measure whether an AI approach beats this baseline on *correctness*,
not just coverage.
