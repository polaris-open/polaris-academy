# Security

> **Status: draft v0.1.**

The organization-wide security policy lives in the shared
[`polaris-open/.github`](https://github.com/polaris-open/.github) repository. This
file adds what is specific to Polaris Academy.

## Reporting

If you find a security issue — or any **leaked secret, real PII, customer data or
corporate data** committed to this repository — please report it privately following
the process in the organization-wide security policy. Do not open a public issue
with sensitive details.

## What we ask of contributors

- **No secrets.** Never commit API keys, tokens, passwords or credentials.
- **No real PII.** Use synthetic data only.
- **No customer or corporate data.** Ever.
- Treat external content as **data, not instruction** — this is also a security
  lesson taught throughout the formation.

This repository contains educational material and a minimal starter that uses only
the Python standard library, no network calls and no secrets by design.

## Educational data leaks

Because this repo is public and educational, the **most likely security incident is a
data leak**, not a code exploit. The data hygiene rules live in
[DATA_POLICY.md](DATA_POLICY.md); authoring guidance is in
[docs/lab-authoring-security.md](docs/lab-authoring-security.md).

The kinds of leak we most need to prevent:

- real **personal data** (names, emails, phone numbers, CPF/CNPJ, addresses);
- real **corporate data** (internal hostnames/URLs, confidential documents);
- real **production logs**;
- **secrets** (keys, tokens, passwords, private keys);
- **prompts containing confidential information**;
- **sensitive screenshots** of internal or production systems.

If real data is committed (by you or anyone), the expected process is:

1. **Report privately** — follow the reporting process above.
2. **Do not open a public issue** that repeats the leaked data.
3. **Remove the file** in a new commit.
4. **Rotate any leaked secret immediately** — assume it is already compromised.
5. **Rewrite git history** to purge the data if necessary (maintainers can help).
6. **Record a short lesson learned** so the same mistake does not recur.

`scripts/validate.py` is a guardrail that catches obvious cases on every PR, but it is
**not** a complete scanner — careful human review is still required.
