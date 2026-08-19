# Scoring Rules

Reference for `engine/scoring.py`. Read this before changing the engine.

## Normalization

Every indicator value is normalized to 0-100 before aggregation:
- `direction: higher` → `100 * (value - min) / (max - min)`
- `direction: lower`  → `100 * (max - value) / (max - min)`

`min`/`max` come from `indicators/INDICATOR_REGISTRY.csv`. Set them to
plausible real-world bounds, not the current sample's min/max — otherwise
normalization drifts every time new countries are added.

## Missing data

A missing observation is **never** treated as zero. It is excluded from
that pillar's weighted average for that country that week, and the
pillar score is flagged `partial: true` with the count of missing
indicators. This is a direct implementation of Constitution principle
on bias against low-data-availability countries.

## Aggregation

Weighted arithmetic mean at each level (indicator → pillar → ADCI),
weights from the registry's `weight` column, renormalized over whatever
indicators actually have data that week (see Missing data above).

## Confidence

Each observation carries `confidence: high|medium|low` from the
Indicator Agent. `scoring.py` does not change the ADCI score based on
confidence, but it does propagate a `min_confidence` field per pillar and
per country so low-confidence scores are visibly flagged on the
dashboard rather than silently blended in.

## Revisions

If a re-run changes a past week's already-published observation, the new
score is a **new row** in `scores/historical/`, tagged
`revised_from: <old_score>` and `revision_reason: <text>`. The old row is
never deleted or edited.
