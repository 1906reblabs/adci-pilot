# ADCI Constitution

## Mission

Measure, explain, and forecast Africa's transition toward digitally
mediated and AI-mediated economic civilization.

## Principles

1. Evidence before inference.
2. Primary sources before secondary sources.
3. No unsupported numerical claims — every number traces to a source ID.
4. Separate observation from interpretation.
5. Separate interpretation from prediction.
6. Every indicator must have a written definition (`indicators/INDICATOR_REGISTRY.csv`).
7. Every score must be reproducible — same evidence in, same score out,
   every time. This is why scoring is code, not a prompt.
8. Uncertainty must be explicit — every observation carries a confidence
   level, every forecast carries a range, not a point estimate.
9. Agents are permitted to disagree. The Data Validator and Source Critic
   are deliberately independent; the Red Team is deliberately adversarial.
   Disagreement that surfaces in `evidence/` is a feature, not noise to
   average away.
10. **Historical scores never silently change.** If a score is revised,
    the old value stays in `scores/historical/`, the new value is appended
    with an explicit reason for the revision. Nobody — human or agent —
    edits a past snapshot in place.

## Bias checks the system must actively run (via the Red Team Agent)

- Are African countries with weaker statistical systems being penalized
  for *having less data*, rather than *scored lower*, on an indicator?
- Does the index structurally reward wealth (better-resourced statistical
  agencies) independent of actual digital-civilization progress?
- Is a data gap being silently treated as a zero?

These checks are not optional cleanup — they are load-bearing parts of
the methodology's credibility.
