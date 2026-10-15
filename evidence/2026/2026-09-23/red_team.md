# Red Team Review — Week of 2026-09-23

Method: raw evidence first, then engine output. Every non-null observation (26) traces to a source ID and a claim that passed both reviews (checked programmatically, 0 exceptions). All three ADCI scores and every pillar were recomputed independently from the registry. They match the engine, except Nigeria's ADCI (mine 50.9, engine 51.0): the engine averages already-rounded pillar scores. That is a rounding convention, not an error.

Headline: ZAF 55.0 (0.0), NGA 51.0 (+0.3), KEN 43.6 (0.0). The only scored change is Nigeria INF-01 (56.1 -> 57.4, NCC July 2026). **There is almost no real-world signal in this week's scores, and that is partly because most of the evidence was not re-checked (Finding 1).**

## Finding 1 — BLOCKING-adjacent (worth-watching, escalated): 24 of 26 values were carried forward, not re-verified
Only NGA INF-01 and NGA GOV-01 were checked live and produced claims on current data. Searches were also run for INF-02, Kenya FIN-02, Kenya GOV-01 and a 2026 UN E-Gov edition; none changed a value. The other 24 values are labelled "CARRIED FORWARD" in claims.csv, observation notes and source rows. This is below the 2026-09-02 standard ("a repeated score is only trustworthy if the search that produced it was repeated too"), and INF-02 slipped through three cycles that way. Not re-checked: ZAF INF-01, GOV-01, GOV-02; all ECO-01; all ECO-02; AI-01 and AI-02; FIN-01 (all three); ZAF and NGA FIN-02; Kenya GOV-02. The dual-pass reviews for these are consistency checks only, not independent re-verification.
**Needs re-running:** a full live pass next cycle. Do not read the unchanged ZAF and KEN scores as "verified stable".

## Finding 2 — BLOCKING (unresolved, carried): INF-02 still has no valid value for any country
Re-searched. A4AI figures resurface (same 2020 data), the ITU Oct-2025 page gives only a global median (1.4%) and regional medians, and the only 2026 country figure is Tier-4 vendor data on a different construct. Claims *-INF-02-10-C1 and NGA-INF-02-11-C1 failed both reviews. Infrastructure remains INF-01 only for all three countries (partial). **Needs re-running:** ITU ICT Price Baskets data-hub country values (5GB data-only, 2025), or the ICASA State of ICT report for ZAF (which tabulates the ITU basket for SADC).

## Finding 3 — RESOLVED on request: INF-02 revision rows appended for 2026-08-19, 08-26, 09-02
Revision rows `2026-08-19_rev1.json`, `2026-08-26_rev1.json`, `2026-09-02_rev1.json` were added to scores/historical/ (originals untouched), each tagged `revised_from` per country and `revision_reason`. They were produced by running engine/scoring.py on observations reconstructed from each week's published snapshot with INF-02 set to missing. Only INF-02 was changed. Effect on ADCI: 08-19 ZAF 50.8->48.6, NGA 58.5->53.7, KEN 55.7->49.2; 08-26 and 09-02 ZAF 49.1->47.4, NGA 53.2->49.4, KEN 48.8->43.6. Caveat: the 08-19 week also contained other errors (Kenya FIN-01 98.0, Nigeria FIN-02 rank #2) that were corrected in later published weeks, not in this revision, so the revised 08-19 values still contain them.

## Finding 4 — worth-watching: Infrastructure is a single, non-like-for-like indicator
Unchanged from 09-09 Finding 3. Nigeria's INF-01 is an NCC subscription count (57.4%); South Africa's (75.6) and Kenya's (35.0) are surveys of individuals. NCC's own communique says about 27% of Nigerians own a smartphone, which shows how far subscription penetration can overstate individual use. Nigeria's rise this week is real in the series but should not be compared across countries.

## Finding 5 — worth-watching: week labels and gaps
This run is labelled 2026-09-23 and was executed 2026-10-05. The 2026-09-09 run (executed 2026-10-01) already used the Chainalysis 2026 index (23 Sep) and NIMC (16 Sep) evidence, so evidence for 09-16 and 09-23 is largely already in the series. No runs exist for 09-16 or 09-30. The trend line therefore has irregular spacing.

## Finding 6 — carried forward, unresolved
FIN-01 three-construct inconsistency; FIN-01 mobile-money framing under-measures South Africa; GOV-01 three constructs (Nigeria 142M/220M assumed denominator, South Africa 63.6 older basis likely understated, Kenya 40.6 on a May-2024 base for a fifth week); ordinal-to-index linearity (FIN-02 is on a new 117-country basis, so the NGA/ZAF values are not trend-comparable with pre-09-09 weeks); ECO-02 on FY2025 with H1 2026 context only; Kenya FIN-02 missing (outside published top 20); UN E-Gov 2026 edition not found published.

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** Coverage ZAF 9/10, NGA 9/10, KEN 8/10; gaps are INF-02 (source failure, all three) and FIN-02 (access, Kenya). Kenya's ADCI (43.6) is the lowest and also rests on the fewest indicators, so the concern recurs. Treat as unresolved until INF-02 and FIN-02 are populated.
- **Index rewards wealth/statistical capacity?** South Africa highest (55.0), driven by GOV-02, INF-01 and FIN-02 now existing, partly the effect the constitution asks us to watch. Unresolved.
- **Data gap silently treated as zero?** No. `missing_indicators` lists INF-02 (all) and FIN-02 (KEN); pillar scores are weight-renormalized (recomputed).

## No fabrication found
Every non-null value traces to a source ID. Derived values: NGA GOV-01 (142/220) and rank-to-index conversions carried from earlier cycles.
