# Agent 09 — Calibration Agent

**Runs only if** a prior forecast in `scores/current/adci_scores.json`
(`forecast` field, written by Agent 10 in a previous week) has an
`as_of` date that has now arrived — i.e. something predicted is now
resolvable against this week's actual observation.

**Input:** the past forecast + this week's actual `scores/current/adci_scores.json`.

**Task:** was the prior forecast/prediction useful? Compute the gap
between predicted and actual. Note whether the miss (if any) traces to a
bad indicator observation, a bad pillar interpretation, or a genuinely
bad forecasting assumption — these need different fixes.

**Output** — `evidence/2026/<week>/calibration.md`:

```
## Nigeria — FIN-01 forecast review
Predicted (base case, made 2026-04-06): 74.0
Actual (2026-08-11): 71.2
Miss: -2.8
Likely cause: forecast assumed faster stablecoin-rail adoption than
this week's validated evidence supports.
```

This file accumulates over time — it's the record that should eventually
make `agents/10_forecast_agent.md` better calibrated, not just more
detailed.
