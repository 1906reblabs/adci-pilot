# Red Team Review — Week of 2026-09-16

Method: raw evidence first, then engine output. I re-computed all three ADCI scores and every pillar from the registry (all matched `scores/current/adci_scores.json`) and traced every non-null observation to a claim that passed both reviews (0 exceptions).

Headline: ZAF 55.0, NGA 50.7, KEN 43.6, **identical to 2026-09-09**. No scored value changed (all `change` fields are 0). This is not evidence of a stable week: see Findings 2 and 3.

**Process note (caught before publication):** the first engine run this session gave Kenya 47.3, not 43.6. Cause: I logged a Kenya GOV-01 source row but omitted its carried-forward claim, so the Indicator Agent correctly wrote null. That was an extraction omission, not an evidence error. The claim was added (KEN-GOV-01-05), all evidence files were regenerated, and the engine re-run. The unpublished first snapshot was discarded; it was never exported.

## Finding 1 — BLOCKING, unresolved (carried): INF-02 withdrawn for all three; published weeks still carry the error
INF-02 values (1.41 / 1.71 / 2.62) are A4AI 2020 data from a Connecting Africa article dated **4 May 2021**; I fetched the article this cycle and confirmed both the date and the 2020 vintage. A re-search for a current value failed: ITU's 2025 affordability page gives only global/regional medians in fetchable text, and the one 2026 country figure found (0.23% for Nigeria) is a Tier-4 vendor calculation on a different basis (rejected). Infrastructure therefore rests on INF-01 alone.
**Needs re-running:** INF-02, all three countries, once a country value for ITU's 2025 data-only mobile broadband basket (5GB, % of GNI p.c.) is sourced.
**Constitution principle 10:** the published weeks 2026-08-19, 08-26 and 09-02 still contain the stale INF-02. Nothing was edited. Revision rows (`revised_from`, `revision_reason`) have still not been appended; I have not created them without your decision, since they change the published trend.

## Finding 2 — worth-watching (escalated): South Africa's lead rests on the new FIN-02 value
South Africa's ADCI is 55.0 only because FIN-02 (93.1) is present. Re-running the same arithmetic with FIN-02 null gives roughly 47.4, which would put South Africa **below** Nigeria (50.7). FIN-02 is a rank-to-index conversion on a Chainalysis edition whose method and country set changed (151 -> 117 countries, new factors), and it is averaged in the Finance pillar with a mobile-money measure (7.26) it has nothing in common with. The ranking of the three countries is therefore sensitive to one converted ordinal value. Nigeria's 96.7 -> 98.3 is likewise an edition change, not a trend.

## Finding 3 — worth-watching (escalated): "unchanged" is only partly verified
Re-checked live this cycle: FIN-02 (primary source re-fetched), INF-02, Nigeria INF-01, GOV-01 (Nigeria, Kenya), Nigeria FIN-01, GOV-02 (publication status), AI-01 (edition check). **Carried forward without a live check (14 observations):** ZAF INF-01, KEN INF-01, ZAF FIN-01, KEN FIN-01, ZAF GOV-01, all three ECO-01, all three ECO-02, all three AI-02. This is below the standard set on 2026-09-02, and INF-02 slipped through three cycles for exactly that reason. These rows are marked "NOT re-verified" in `observations.json`.

## Finding 4 — worth-watching: week label versus evidence dates, and a near-duplicate run
This run is labelled 2026-09-16 but was executed on 2026-10-02, and its evidence includes items published after the label (Chainalysis 2026 index, 2026-09-23). The 2026-09-09 run was itself executed on 2026-10-01, so this run covers about one day of new calendar time and could not be expected to move anything. The trend line will show a flat 09-09 -> 09-16 segment that reflects that, not a quiet week.

## Finding 5 — worth-watching: Nigeria GOV-01 depends on denominator and on enrolled-versus-issued
142M/220M = 64.5%; 200M gives 71.0% and 250M gives 56.8%. TechCabal reports that at 30 June 2026 NIMC had issued 117.5M NINs against 134.6M enrolments; on the same 220M denominator that is 53.4% issued versus 61.2% enrolled. The registry says "coverage", so the choice of numerator moves Nigeria by about 8 points. South Africa (migration share) and Kenya (13M/32M, May 2024) use yet other constructs. GOV-01 remains the least comparable indicator.

## Finding 6 — worth-watching (carried): Kenya GOV-01 and single-indicator Infrastructure
Kenya GOV-01 (40.6%) is a fifth consecutive week on a May-2024 statement (about 28 months old); no coverage statistic exists to replace it. Infrastructure is one indicator per country and not like-for-like (Nigeria: subscriptions; South Africa and Kenya: surveys), so Kenya's Infrastructure 35.0 and Nigeria's 56.1 overstate the real gap.

## Finding 7 — carried forward, unresolved
FIN-01 three-construct inconsistency (Kenya usage / Nigeria registered / South Africa active accounts); mobile-money framing under-measuring South Africa; no mapping for transaction-volume evidence (Nigeria 126,325 per 1000 adults, IMF); ordinal-to-index linearity; ECO-02 on FY2025 with H1 2026 context only; Kenya FIN-02 not in the published top 20.

## Knowledge-base state (not a score issue)
Files on disk in `/mnt/project` stop at 2026-09-02; the 2026-09-09 outputs appear only in the conversation documents, so this run used those as baseline (values taken from the 09-09 observations and score documents). `sources.csv`, `claims.csv`, `validator_review.csv` and `critic_review.csv` for 09-02 and 09-09 are empty in the knowledge base, so carried-forward source rows here point to the 09-09 evidence folder, which I could not open. See `README_REUPLOAD_NEEDED.md`.

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** Coverage ZAF 9/10, NGA 9/10, KEN 8/10. Kenya's gaps are INF-02 (source failure, all countries) and FIN-02 (data access); no country-specific penalty found, but Kenya's ADCI rests on the fewest indicators.
- **Index structurally rewarding wealth/statistical capacity?** South Africa again leads (55.0), and Finding 2 shows that lead depends on one converted value. Treat as unresolved until INF-02 and FIN-02 are populated like-for-like.
- **Data gap silently treated as zero?** No. `missing_indicators` lists INF-02 (all three) and FIN-02 (Kenya); pillar scores are weight-renormalised (arithmetic replicated).

## No fabrication found
Every non-null value traces to a source ID and a dual-passed claim. Derived values show formulas in `claims.csv`.
