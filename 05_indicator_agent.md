# Agent 05 — Indicator Agent

**Input:** claims where both `validator_pass` and `critic_pass` are
`true`, plus `indicators/INDICATOR_REGISTRY.csv`, plus the most recent
prior observation for this (country, indicator) from
`scores/historical/`.

**Task:** produce exactly one observation per (country, indicator) this
week — the best-supported current value, not a list of candidate claims.
If multiple validated claims disagree, prefer the higher source tier; if
tiers tie, note the disagreement in `notes` and lower `confidence`.

**You do not compute a country score.** You produce the observation only.

**Output** — write/append to `evidence/2026/<week>/observations.json`,
one object per (country, indicator):

```json
{
  "country": "KEN",
  "indicator": "FIN-01",
  "value": 71.2,
  "unit": "index",
  "as_of_date": "2026-08-11",
  "confidence": "high",
  "source_ids": ["KEN-FIN-01-01", "KEN-FIN-01-02"],
  "previous_value": 68.9,
  "change": 2.3,
  "notes": ""
}
```

If no claim survived validation for a (country, indicator) this week,
still write an object with `value: null` and `notes: "no validated
evidence this week"` — this is how `engine/scoring.py` knows to exclude
it rather than treat it as zero.
