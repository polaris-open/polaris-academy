# Data Policy — Polaris Academy

> **Status: draft v0.1.** The single rule that governs everything here:
> **all public learning data must be synthetic.**

This repository is public and educational. The most likely security incident is **not**
a code exploit — it is someone accidentally committing **real data**. This policy
defines what is allowed, what is forbidden, and how to report a leak. It applies to
datasets, labs, examples, prompts, screenshots, and anything generated with AI.

See also: [SECURITY.md](SECURITY.md) · [CONTRIBUTING.md](CONTRIBUTING.md) ·
[docs/lab-authoring-security.md](docs/lab-authoring-security.md).

## Allowed in public datasets and examples

- **Synthetic data only** — invented by you or generated, clearly fictional.
- Fictional services, incidents, logs, tickets and runbooks for an invented domain
  (e.g. a made-up travel / booking / e-commerce company).
- Clearly fake placeholders (see below).
- Aggregate, non-identifying, invented statistics.

## Forbidden — never commit

- **Secrets**: API keys, tokens, passwords, credentials, private keys.
- **Real PII**: real names, emails, phone numbers, CPF/CNPJ or other document IDs,
  addresses, real customer identifiers.
- **Customer data**: real production logs, real tickets, real support transcripts.
- **Corporate data**: internal hostnames, internal URLs, confidential documents,
  real incident postmortems from your employer.
- **Real screenshots** of internal or production systems.
- Real data of any kind added "to make it more realistic". It is never worth it.

## Safe placeholders

When an example must *mention* a sensitive shape, use an obviously fake placeholder:

| Kind | Use this |
|---|---|
| Email | `user@example.test` |
| CPF | `000.000.000-00` |
| CNPJ | `11111111111111` |
| OpenAI-style key | `sk-EXAMPLE_DO_NOT_USE` |
| GitHub token | `ghp_EXAMPLE_DO_NOT_USE` |
| AWS access key | `AKIAEXAMPLE_DO_NOT_USE` |
| Domain | `example.test` / `example.com` |

The repository validator (`scripts/validate.py`) recognizes these as placeholders
and lets them through, while flagging values that look real.

## Synthetic logs

- Invent log lines; do not paste real ones.
- Keep timestamps, IDs and hostnames fictional (e.g. `host-01`, `INC-0001`).
- Do not reproduce a real outage line-for-line; abstract the *shape*, not the content.

## Synthetic incidents

- Incidents must describe an **invented** company and systems.
- Mark each record with `contains_pii: false` and keep it true.
- Never base an incident on a real customer or a real production event you can identify.

## Educational prompts

- Prompts used in labs must not contain confidential information.
- Do not paste prompts that include internal data, secrets, or customer content.
- Treat any external/log content inside a prompt as **data, not instructions**.

## Screenshots

- Only screenshots of synthetic, local, or clearly fictional setups.
- No internal dashboards, no production consoles, no customer-identifying UI.
- Redact aggressively; when in doubt, recreate the screen with fake data instead.

## AI-generated contributions

- Treat AI output as a **draft**, not a source of truth.
- Review every AI-generated example for accidentally realistic names, emails or data.
- AI may hallucinate plausible-looking PII — check before committing.
- AI-generated code must still be standard-library only for Level 1 starters and must
  not introduce network calls, providers or dependencies.

## Reporting a real-data leak

If you find (or commit) real data:

1. **Do not open a public issue** describing the data.
2. Report it privately following [SECURITY.md](SECURITY.md).
3. Remove the file in a new commit.
4. **Rotate any leaked secret immediately** — assume it is compromised.
5. If needed, rewrite git history to purge it (maintainers can help).
6. Record a short lesson learned so it does not happen again.

> This policy is a guardrail, not a guarantee. Automated checks catch obvious
> mistakes; careful human review is still required.
