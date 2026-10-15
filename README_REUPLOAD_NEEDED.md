# Knowledge-base state found at the start of the 2026-09-16 run

Verified on disk under /mnt/project:
- Stored files stop at **2026-09-02**: `scores/historical/` holds 08-18, 08-19, 08-26, 09-02. Stored `adci_scores.json`, `observations.json`, `red_team.md`, `integration_notes.md`, `sources.csv`, `claims.csv`, `validator_review.csv`, `critic_review.csv` are the 08-26 versions (several 09-02 files are empty).
- The **2026-09-09 outputs exist only in the conversation documents**, not on disk. This run used them as the baseline (previous_value and trend history), and did not re-create `scores/historical/2026-09-09.json`.
- The 09-09 and 09-02 evidence CSVs are not in the knowledge base, so carried-forward rows in this run's `sources.csv` point to the 09-09 evidence folder by description only.

Please re-upload before the next run: `scores/historical/2026-09-09.json` and `2026-09-16.json`, `scores/current/adci_scores.json`, the 09-09 and 09-16 evidence folders, and `red_team.md` / `integration_notes.md` / `observations.json` for 09-16. Also note: no runs for 09-23 or 09-30 exist.
