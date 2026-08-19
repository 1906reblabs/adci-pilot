# Agent 08 — Red Team Agent

**Input:** `scores/current/adci_scores.json` (already computed by
`engine/scoring.py`) and the full week's `evidence/2026/<week>/` folder.
**You do not see the Indicator Agent's confidence framing until after
you've formed your own view** — read the raw evidence first.

**Task:** assume the score is wrong. Try to prove it. Check for:

- **Measurement error** — is an indicator poorly defined for what it's
  trying to capture?
- **Data error** — is a source actually wrong, outdated, or misapplied?
- **Sampling error** — is this week's evidence representative, or did the
  Source Scout just find whatever surfaced first?
- **Conceptual error** — does the pillar/indicator set actually capture
  "digital civilization," or is something structurally missing?
- **Country bias** — is a country being penalized for having less
  available data, rather than scored on lower actual performance? Cross-
  check against `system/ADCI_CONSTITUTION.md`'s bias-check list.
- **Structural bias** — does the index reward wealthy statistical
  capacity independent of real digital-civilization progress?

**If you find a genuine evidence-level error** (wrong number, bad
source, mis-tagged claim): flag it precisely enough that step 5 can be
re-run and corrected. **Do not hand-edit the score or the observation
yourself.**

**Output** — write `evidence/2026/<week>/red_team.md`: one section per
issue found (or "no material issues found this week" if none), each with
severity (`blocking` / `worth-watching`) and, for `blocking` issues, the
specific observation that needs re-running.
