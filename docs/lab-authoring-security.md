# Secure Lab Authoring Guide

> **Status: draft v0.1.** For anyone writing a lab, dataset or example for Polaris
> Academy. Read [DATA_POLICY.md](../DATA_POLICY.md) first — this guide is the
> practical "how to".

The golden rule: **everything public must be synthetic.** The most likely incident in
this repo is a real-data leak, not a code exploit. Author defensively.

## How to create labs with synthetic data

- Invent a fictional company and domain (e.g. a made-up travel/booking platform).
- Generate or hand-write small datasets. Keep them tiny and obviously fake.
- Mark dataset records with `contains_pii: false` and keep it true.
- Run `python3 scripts/validate.py` before opening a PR.

## How to write synthetic logs

- Write log lines from scratch; do not copy real ones.
- Use fictional identifiers: `host-01`, `service-a`, `INC-0001`, `req-abc123`.
- Keep timestamps invented and generic.
- Capture the *shape* of a problem (a retry storm, a stale cache), not a real trace.

## How to create fictional incidents

- Base incidents on **patterns**, not on a specific real event you witnessed.
- Describe symptoms and a next action — all invented.
- Never name a real customer, vendor, or internal system.

## How to avoid copying real problems from work

It is tempting to reuse a real incident from your job. Don't paste it. Instead:

- Extract the **general lesson** (e.g. "payment authorized but ticket not issued").
- Rebuild it with a fictional company, fictional services and invented data.
- Remove anything that could identify the real system, team or customer.

## How to adapt a real experience without exposing real data

- Keep the *concept*; replace every concrete detail.
- Change service names, hostnames, numbers, names and dates to fictional ones.
- If you cannot tell whether a detail is identifying, assume it is and replace it.

## Be explicit (do not do these)

- Do not paste logs from your company.
- Do not use real tickets or real support transcripts.
- Do not use screenshots of internal or production systems.
- Do not use real customer names, emails, or phone numbers.
- Do not include secrets, tokens, API keys or credentials.

## How to handle AI outputs

- Treat AI-generated examples as drafts to review, not as trusted content.
- AI can invent realistic-looking names, emails and IDs — verify they are fake.
- Replace anything that looks real with a placeholder from
  [DATA_POLICY.md](../DATA_POLICY.md).
- Keep Level 1 starters standard-library only: no network, no providers, no deps.

## How to review examples before opening a PR

1. Re-read every new dataset and example as if you were an attacker looking for real
   data.
2. Run `python3 scripts/validate.py` and resolve failures; review warnings by hand.
3. Run the starter checks (`make test`, `make check`).
4. Complete the data-hygiene checklist in the pull request template.
5. If anything feels borderline, replace it with something clearly fictional.
