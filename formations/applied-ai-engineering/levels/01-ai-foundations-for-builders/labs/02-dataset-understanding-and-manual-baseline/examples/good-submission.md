# Example — good submission

> A **good** Lab 02 submission, followed by why it is good. Solid Level 1 work.

## The submission

**Dataset notes:** Inspected `data/synthetic-incidents.jsonl` with
`make inspect-dataset`. 8 records. Fields: `id`, `title`, `service`, `severity`,
`scenario`, `symptoms`, `expected_next_action`, `contains_pii`. Useful for triage:
`service`, `severity`, `symptoms`. `severity` distribution: high=3, critical=2,
medium=2, low=1. `contains_pii` is `false` on every record.

**Recurring patterns:** queue/dead-letter issues (DLQ), latency/timeout issues,
cache staleness.

**Baseline (rule-based triage):**

| Rule | Signal | Output |
| --- | --- | --- |
| 1 | symptoms/scenario mention "DLQ" / "dead letter" | queue/reprocessing |
| 2 | mention "timeout" / "latency" / "504" | latency/dependency |
| 3 | mention "cache" / "stale" | cache/staleness |
| 4 | `severity == critical` | needs human review |

**Metric:** coverage — share of records matched by at least one rule.

**Limitations:** rules miss records with novel wording; small dataset; some incidents
match more than one rule.

## Why this is good

- **Grounded in evidence** — real counts and fields, not assumptions.
- **A deterministic baseline** anyone could run by hand.
- **A simple, measurable metric.**
- **Honest limitations.**

**Verdict:** good. To reach excellent, it would add ambiguous-case analysis, a sharper
"why not AI yet" argument, and questions prepared for Lab 03.
