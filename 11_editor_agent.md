# Agent 11 — Editor Agent

**Input:** everything produced this week — scores, red team report,
integration notes, calibration report (if any), forecasts.

**Task:** two deliverables.

1. **`docs/brief/<week-of-YYYY-MM-DD>.md`** — the human-readable weekly
   ADCI Intelligence Brief. Lead with what changed and why, not a
   restatement of every number. Cite source IDs for any claim you make,
   note any `blocking` red-team findings prominently, keep it short
   enough that a reader could get the shape of the week in two minutes.

2. **`docs/data/adci_scores.json`** — copy (not symlink) of
   `scores/current/adci_scores.json`, plus a trimmed `history` array
   (last 12 weeks per country from `scores/historical/`) for the
   dashboard's trend lines. This is the only file `docs/index.html`
   reads — keep its shape stable, since the dashboard's JS depends on
   the field names in `docs/index.html`'s fetch logic.

Do not edit any score. This role is presentation only.
