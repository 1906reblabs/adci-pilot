# Red Team Review — Week of 2026-09-30

Method: raw evidence first, then engine output. I traced every non-null observation (29) to claims that passed both reviews (0 exceptions), recomputed all three ADCI scores and every pillar without importing the engine (all matched: ZAF 57.07, NGA 52.80, KEN 48.06 before rounding), and re-ran the real engine on scratch copies of the observations to test sensitivity. Scratch runs were not published.

Headline: ZAF 57.1 (+2.1), NGA 52.8 (+1.8), KEN 48.1 (+4.5) versus 09-23. **All three moves are measurement events, none is a real-world change.** INF-02 returned (ITU 2025 values), and INF-01 was put on one construct for all three countries. See Findings 1 and 2.

**Process note:** this run is labelled 2026-09-30 but was executed on 2026-10-15. Its evidence includes items dated after the label (DHA statement 1 Oct 2026; TechCabal Jan-Aug funding, 4 Sep).

## Finding 1 — BLOCKING, resolved this cycle; published weeks affected: INF-01 was on the wrong construct for South Africa and Nigeria
The registry defines INF-01 as the percent of the population using the internet. Since week one the series has been:
- **South Africa 75.6**: the Stats SA GHS 2024 share of *households* with mobile internet access (ZAF-INF-01-22). A household measure, not individual use.
- **Nigeria 53.0 -> 57.4**: NCC broadband *subscriptions* per 100 people (NGA-INF-01-22). Multi-SIM use inflates it; NCC's own forum says about 27% own smartphones.
- **Kenya 35.0**: a people-based survey (correct construct).
The Validator now fails the first two on unit (`validator_pass` false), while the Critic passes them because the sources are authoritative for what they measure. That split is the adversarial pair working, and it also shows why this slipped through seven cycles: earlier reviews checked the source and the arithmetic but not the construct.
This run replaces them with ITU/WDI individuals using the internet, 2024: ZAF 78.4, NGA 41.2, KEN 35.0 (Kenya agrees with the Tier-1 CA+KNBS survey). Effect on this week's scores (engine, scratch run A): Nigeria -1.6, South Africa +0.3.
**Constitution principle 10:** published weeks 08-19 to 09-23 carry the old INF-01 values for ZAF and NGA. Nothing was edited and **no revision rows were created**; they change the published trend, so that is your decision. Recommendation: append revision rows (`revision_reason`: INF-01 construct mismatch) for the affected weeks. The Nigeria change is the larger one: 16.2 points on INF-01, which in the older single-indicator Infrastructure weeks is about 3 ADCI points (16.2 / 5 pillars).

## Finding 2 — RESOLVED (was blocking), with caveats: INF-02 has valid values again
ITU ICT Price Baskets 2025, data-only mobile broadband basket as % of GNI per capita: ZAF 1.27, NGA 1.56, KEN 4.1. I could not read the ITU xlsx (binary here) and used the StatOrigin mirror. Checks that support it: its South Africa 2024 value (1.63) equals ICASA's own relay of ITU 2024, and its Nigeria 2020 value (1.71) equals the stale figure that was wrongly logged as 2026, which independently confirms the 2020 error.
Cautions: (a) mirror dependence, so confidence is medium; confirm against the ITU file next cycle. (b) The 2025 edition moved to a 5GB basket; Kenya reads 1.79 (2024) and 4.1 (2025), so it is a method break, not a trend. Scratch run E (2024 values for all three) moves Kenya by +1.1 and the others by under 0.3. (c) Nigeria is no longer clearly the cheapest: South Africa is lower. The old A4AI-based claim was wrong on that point.
Effect on scores: INF-02 adds about +5.1 to Nigeria, +4.5 to Kenya and +1.6 to South Africa (scratch run C removes it).

## Finding 3 — worth-watching (escalated): the ranking of the three countries is not robust
South Africa leads (57.1) but:
- Without FIN-02 (rank-to-index on a new Chainalysis edition) the scores are ZAF 49.4, NGA 48.5, KEN 48.1: all within 1.3 points.
- If FIN-01 used Findex 2025 digital-payment shares (ZAF 67, NGA 54, KEN 89) the scores would be ZAF 63.7, KEN 55.3, NGA 53.3, which **puts Kenya above Nigeria**. The FIN-01 construct choice therefore changes the order of two countries.
- Nigeria's GOV-01 denominator (200M to 250M) moves Nigeria between 53.5 and 52.0.
Treat the order as unresolved, and do not read the +2.1 for South Africa as improvement.

## Finding 4 — worth-watching (decision needed): FIN-01 now has a candidate replacement
The Findex 2025 digital-payment share (World Bank, same survey method, all three countries; relayed by secondary outlets) removes the three-construct problem flagged since 08-26. It is not scored because it is a share of people, not the registry's index of mobile-money transactions (the Validator fails it on unit; the Critic passes the source). Whether FIN-01 should be redefined as rail-agnostic digital-payment penetration is a METHODOLOGY.md and registry decision. Note it would lift Kenya (+7.2), South Africa (+6.6) and Nigeria (+0.5) in the current engine.

## Finding 5 — worth-watching: AI-01 provenance and construct
The 52.1 / 37.7 / 49.7 scores come from the **Qhala and Qubit Hub AI Talent Readiness Index for Africa 2025 (April 2025)**. Earlier weeks attributed them to PwC/Strategy&, whose August 2025 outlook relays the same figures. The index is a readiness composite (digital skills 40%, data and infrastructure 35%, government readiness 25%), not AI-skilled workforce per capita. Confidence lowered medium to low for all three; values unchanged (ZAF 52.15 as published). This is the third AI-pillar definition or provenance problem in four cycles (AI-02 count vs SAP, Ataraxis vs PwC). The Ataraxis 2026 index (ZAF 66.5, NGA 49.15, KEN 47.6) is a different construct and was not used.

## Finding 6 — worth-watching: Kenya GOV-01 may not measure Maisha Namba
Sixth week on the May-2024 base (13M / 32M). New contradicting evidence: an Aug 2025 NDIC progress report cites 90,038 Maisha Numbers issued in four counties (KEN-GOV-01-21). The 13M may count IDs captured in the national register rather than Maisha Namba. If so, 40.6% overstates coverage. Not resolved; confidence stays low. Also South Africa GOV-01 (63.6, carried, low confidence) is probably understated: a 1 Oct 2026 DHA statement puts green-book-only holders at about 14.7M, down from 16M. A 34M cumulative-card figure failed both reviews (ZAF-GOV-01-22-C1).

## Finding 7 — worth-watching: verification coverage this week
Of 29 non-null observations: **21 re-checked live with a changed or confirmed value** (INF-01, INF-02, FIN-01, AI-01, AI-02, ECO-01 all countries; FIN-02 ZAF and NGA; GOV-01 NGA), **3 edition-status checks with value carried** (GOV-02; UN 2026 edition still unpublished), and **5 carried without refresh** (ECO-02 all three: Partech FY2025 page not re-fetched; GOV-01 ZAF and KEN). Two further limits: FIN-02 was confirmed against two secondary outlets, not Chainalysis's own page; and the StartupBlink N=120 used in ECO-01 is carried from earlier runs and not restated in this run's sources (ranks are sensitive to N).

## Finding 8 — carried, unresolved
Ordinal-to-index linearity; FIN-01 mobile-money framing under-measuring South Africa; transaction-volume evidence (NGA 126,325 per 1000 adults) with no mapping; ECO-02 on FY2025 with 2026 data on two different trackers (H1 Big Deal; Jan-Aug TechCabal Insights) as context only; Kenya FIN-02 missing (outside the published top 20); GOV-01 measured three ways.

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** Coverage ZAF 10/10, NGA 10/10, KEN 9/10 (first week with two complete countries). Kenya's gap is FIN-02, a data-access limit. No country-specific penalty found.
- **Index structurally rewarding wealth/statistical capacity?** South Africa leads again, mostly from GOV-02, INF-01, INF-02 and FIN-02. Finding 3 shows the lead is thin and depends on FIN-02 and on the FIN-01 construct. Unresolved.
- **Data gap silently treated as zero?** No. `missing_indicators` lists only FIN-02 for Kenya; pillar scores are weight-renormalised (recomputed independently).

## No fabrication found
Every non-null value traces to a source ID and a dual-passed claim. Derived values (rank conversions, 142M/220M, unit conversions) show formulas in `claims.csv`.
