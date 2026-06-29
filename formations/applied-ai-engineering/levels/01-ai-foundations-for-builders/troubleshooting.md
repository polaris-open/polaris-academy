# Troubleshooting — Level 1

> **Status: draft v0.1.** First troubleshooting guide. If you hit something not
> listed here, see [SUPPORT.md](../../../../SUPPORT.md) — community is support, not
> dependency.

## "I don't know where to start"

Start with the [lab guide](lab-guide.md), step 1. Don't try to design anything yet
— just read the synthetic incidents and write 3 observations in `progress.md`. The
lab is ordered so each step takes ~5–10 minutes. You are framing a problem, not
building a model.

## "make doesn't run"

- Make sure you are inside the starter directory:
  `cd starters/ai-incident-support-assistant`.
- Check `make` is installed: run `make --version`. On macOS it ships with the Xcode
  Command Line Tools (`xcode-select --install`). On Linux, install `make` via your
  package manager (e.g. `sudo apt-get install make`).
- If `make` truly isn't available, you can run the underlying command directly:
  `python3 tests/test_dataset.py`.

## "Python is not installed"

- Check with `python3 --version` (and `python --version`).
- If neither works, install Python 3 from [python.org](https://www.python.org/) or
  your package manager. The starter only needs the **standard library** — no `pip
  install`, no virtualenv required.
- `make setup` will tell you which interpreter it found.

## "Invalid JSONL dataset"

- Each line of `data/synthetic-incidents.jsonl` must be one valid JSON object. A
  trailing comma, a missing quote or a blank line in the middle will break it.
- Run `make test` — the error message names the line number.
- If you edited the dataset, undo your change or restore the file. For Level 1 you
  do **not** need to modify the dataset.

## "I don't know how to choose a metric"

- Ask: *what does it cost when the assistant is wrong?* If a missed critical
  incident is far worse than a false alarm, you care about recall on critical cases,
  not overall accuracy.
- Pick something you could actually measure on this dataset, e.g. "% of incidents
  where my suggested next action matches `expected_next_action`".
- It is fine to start simple and refine. The [rubric](rubric.md) only asks that the
  metric be measurable and justified by the cost of error.

## "I'm trying to use an LLM too early"

Stop — that's not this level. Level 1 has **no LLM, no RAG, no Agent**. If you feel
the urge to "just call a model", that's exactly the habit this level is designed to
break. Define the problem, the metric and the baseline without AI first. The LLM
work begins in Level 2 (planned), *after* you can prove whether AI is even needed.
