# Agent Roles

Eleven roles, run in sequence by Claude in a single Project conversation
(see `PROJECT_INSTRUCTIONS.md`). Each has its own spec in `agents/`.
Summary:

| # | Role | Reads | Writes | May score? |
|---|------|-------|--------|------------|
| 01 | Source Scout | registry + web | raw sources | no |
| 02 | Evidence Extractor | raw sources | structured claims | no |
| 03 | Data Validator | claims | pass/fail + notes | no |
| 04 | Source Critic | claims | pass/fail + notes | no |
| 05 | Indicator Agent | validated claims | indicator observations | no |
| 06 | Specialist Agents (×6 pillars) | observations | pillar commentary | no |
| 07 | Integration Agent | observations | cross-pillar notes | no |
| — | **engine/scoring.py** | observations + registry | **scores** | **yes — only this** |
| 08 | Red Team Agent | scores + evidence | falsification report | no |
| 09 | Calibration Agent | past forecasts + outcomes | calibration report | no |
| 10 | Forecast Agent | scores + history | 2030 base/upside/downside | no |
| 11 | Editor Agent | everything above | weekly brief + dashboard data | no |

Two independent design rules worth keeping visible:

- **Collection agents don't evaluate their own evidence.** The Source
  Scout and Evidence Extractor never judge quality — that's steps 3–4.
- **The two validators are adversarial pairs, not a single QA step.** The
  Data Validator checks internal consistency (units, dates, duplicates,
  reproducibility). The Source Critic checks the source itself
  (authority, methodology, bias, contradiction). A claim needs both to
  pass.
