# Example — excellent submission (10/10 for Level 1)

> An **excellent** Lab 01 submission, followed by why it is excellent. "10/10 for
> Level 1" means excellent *framing* — not production, not a specialist badge.

## The submission

**Problem (scoped):** For booking/ticketing incidents where payment is authorized but
the ticket is not issued, the on-call engineer cannot quickly tell *which* service
owns the failure and *what* the safe first action is. Scope is deliberately limited
to this incident family, not "all incidents".

**Persona:** On-call engineer during a rotation; comfortable with dashboards, not
with the assistant's internals; under time pressure.

**Current workflow:** Alert → check payment status → check issuance status → search
runbooks → infer the owning service → post in chat → take a first action. Most time
is lost inferring the owning service and the safe first step.

**Desired outcome:** A consistent, correct **first next action** for this incident
family, with the human still deciding.

**Baseline without AI:** A rule by `service` + `severity` backed by a small lookup of
`symptoms` keywords (e.g. "DLQ", "stale exchange rate", "retry storm") → a default
next action drawn from `expected_next_action`. Implementable in an afternoon.

**Where the baseline is enough — and where not:** For the frequent, well-known
patterns (DLQ replay, cache invalidation) the rule is likely *enough* on its own.
It breaks for novel symptom phrasings and conflicting signals — which is the only
place a model might later earn its place.

**Metric:** Correct first-suggestion rate against `expected_next_action`. It would
**catch** wrong routing, but would **not catch** a suggestion that is technically
listed yet unsafe in context — so a human review stays in the loop.

**Privacy note:** `synthetic-incidents.jsonl`, confirmed synthetic
(`contains_pii: false` everywhere). No real logs/customer/corporate data. If this
were ever fed real data, raw incident text and any identifiers would **not** be sent
to a model; only minimized, masked fields would be considered — and not in this lab.

**Risks and limits:** Small dataset; rule brittleness; over-trust risk (people may
follow a confident-looking suggestion). The assistant **supports** a human decision;
it does not make it. This is a framing exercise, **not** a product or a demo.

**Why AI is not needed yet:** Success here is defined and largely reachable by a
simple rule + lookup. Adding an LLM now would add cost, latency and a hallucination
surface with **no measured gain** — there is not even a baseline to beat yet.

**Evidence:** `make check` passes (output in `progress.md`); `problem-framing.md`,
`privacy-note.md`, `progress.md` filled in and reproducible from a clean clone.

## Why this is excellent

- **Tight scope** — one incident family, not "everything".
- **Workflow well described**, so the value is obvious.
- **Defensible baseline**, with explicit conditions where it is enough.
- **A metric that knows its own blind spot.**
- **Explicit risks/limits**, no promise of production.
- **A clear argument for why an LLM is not justified yet** — the heart of Level 1.
- **Reproducible evidence.**

**Verdict:** excellent for Level 1. The natural next step (Level 2, planned) is to
*build the baseline, then measure whether an LLM beats it* — with evals.
