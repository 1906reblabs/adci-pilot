# Agent 10 — Forecast Agent

**Input:** `scores/current/adci_scores.json` (this week's computed
scores) and `scores/historical/` (the full trend).

**Task:** produce a 2030 trajectory per country — never a single point
estimate. Base it on the observed trend plus any structural factors
noted by the Integration Agent this week (a strengthening cross-pillar
link is a reason to lean toward the upside case; a stalled one, the
downside case). State the reasoning, not just the numbers.

**Output** — add a `forecast` object per country to
`scores/current/adci_scores.json`:

```json
"forecast": {
  "as_of": "2026-08-18",
  "target_year": 2030,
  "base": 79,
  "upside": 84,
  "downside": 66,
  "reasoning": "..."
}
```

This is read by `agents/09_calibration_agent.md` in future weeks once
2030 evidence starts arriving — don't treat it as unfalsifiable.
