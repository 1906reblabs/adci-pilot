# ADCI Methodology

## Pilot scope (current)

- Countries: South Africa, Nigeria, Kenya (`countries/*.yaml`)
- Indicators: 10, spanning 5 pillars (`indicators/INDICATOR_REGISTRY.csv`)
- Cadence: weekly evidence refresh, weekly score recompute

Do not expand scope until the pilot answers one question: **can
independent agents turn messy, unevenly-available African data into
country-level measurements that are reproducible week over week?**

If yes, expand in two dimensions independently:
- countries: 3 → 10 → 20 → 54
- indicators: 10 → 35 → 100+

Expand indicators before countries — a wrong methodology tested on 3
countries is cheaper to fix than a wrong methodology tested on 54.

## Score construction (deterministic, in `engine/scoring.py`)

```
indicator observation (0-100, normalized per indicator's direction)
        ↓  weighted average within pillar
pillar score
        ↓  weighted average within dimension (if using dimensions)
dimension score
        ↓  weighted average across pillars
ADCI score (0-100)
```

Weights live in `indicators/INDICATOR_REGISTRY.csv` (a `weight` column) so
changing emphasis is a data edit, not a code edit or a prompt edit.

## What agents produce vs. what code produces

Agents (LLM): evidence gathering, evidence validation/critique, structured
indicator *observations* (a value + confidence + source, not a score),
pillar-level interpretation, cross-pillar relationships, red-teaming,
calibration review, forecasting narrative, the human-readable brief.

Code (`engine/scoring.py`, deterministic): every actual arithmetic step
from observation to final ADCI score. No exceptions — see Constitution
principle 7.
