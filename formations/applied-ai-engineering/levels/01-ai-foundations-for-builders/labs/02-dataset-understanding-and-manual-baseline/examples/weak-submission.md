# Example — weak submission

> A deliberately **weak** Lab 02 submission, followed by why it is weak. Use it to
> recognize the failure pattern in your own work.

## The submission

**Dataset notes:** I looked at the dataset and it seems fine. There are some
incidents about bookings and payments.

**Baseline:** The assistant should read the incident and figure out what to do. We
should plug in an LLM so it understands everything automatically.

**Metric:** —

**Limitations:** —

## Why this is weak

- **No evidence of inspection.** "Seems fine" is not a record count, not a field
  list, not a pattern. There is no proof the dataset was actually examined.
- **Not a baseline.** "Let the LLM figure it out" is the opposite of a deterministic
  manual baseline — and it reaches for AI before anything is understood or measured.
- **No metric.** Nothing to measure "better" against.
- **No limitations.** No honesty about what the approach cannot do.
- **Blocking:** jumping straight to an LLM is exactly what Lab 02 forbids.

**Verdict:** redo. There is nothing here a Lab 03 AI attempt could be measured against.
