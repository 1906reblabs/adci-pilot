# Red Team Review — Week of 2026-09-09

Method: raw evidence first, then the engine output (`scores/current/adci_scores.json`). Every non-null
observation was traced to a source ID and to a claim that passed both reviews (0 exceptions), and the
engine arithmetic was independently re-computed from the registry (all three ADCI scores and every
pillar matched). A draft engine run on a scratch copy and the final run were identical.

Headline: ZAF 55.0 (+5.9), NGA 50.7 (-2.5), KEN 43.6 (-5.2). **None of these moves is a real-world
change in digital readiness.** They come from (a) removing INF-02 (stale vintage), and (b) South Africa's
FIN-02 being populated for the first time. See Findings 1 and 2.

## Finding 1 — BLOCKING (resolved this cycle by exclusion; prior published weeks affected): INF-02 was a 2020 value labelled 2026
All three INF-02 values (ZAF 1.41, NGA 1.71, KEN 2.62) trace to a Connecting Africa article dated
**4 May 2021** reporting A4AI **2020** data. Earlier cycles logged it as_of 2026-06-15 and "re-confirmed
unchanged / no newer edition found" for three weeks. This cycle's Validator and Critic caught it
(`validator_review.csv`, `critic_review.csv`, claims `*-INF-02-03-C1`), so the Indicator Agent wrote `null`.
Effect, from the engine: Infrastructure ZAF 84.3 -> 75.6, NGA 72.2 -> 56.1, KEN 61.0 -> 35.0 (each now one
indicator, flagged partial). This explains the whole NGA and KEN ADCI decline.
**Needs re-running:** INF-02 for all three countries once a current ITU data-only mobile broadband basket
(2025, 5GB, % of GNI p.c.) country value is sourced. The ITU Oct-2025 affordability page gives only global
and regional medians in fetchable text.
**Constitution principle 10:** the published weeks 2026-08-19, 08-26 and 09-02 contain this error. They
were not edited. Recommend appending revision rows (`revised_from`, `revision_reason`) rather than
leaving the trend line implying the three INF-02 readings were current.

## Finding 2 — worth-watching (escalated): South Africa's rise is mechanical, and FIN-02 starts a new series
South Africa's Finance pillar went 7.3 -> 45.4 because FIN-02 (93.1, rank #9 of 117) entered and
the pillar is the weighted mean of FIN-01 (7.26) and FIN-02 (weights 1.0 / 0.8). That is +38 pillar points
and, with Infrastructure -8.7, the net +5.9 ADCI. Nothing changed in South Africa between weeks; a missing
indicator was found. Two cautions: (a) Chainalysis changed method and country set (151 -> 117 countries,
four PPP-weighted factors, geometric mean), so Nigeria's 96.7 -> 98.3 is not a trend; (b) the Finance
pillar now averages a mobile-money measure with a crypto-rank measure for South Africa, which is a
construct blend, not a measure of digital-payments maturity.

## Finding 3 — worth-watching: Infrastructure now rests on one indicator that is not like-for-like
With INF-02 absent, INF-01 alone defines Infrastructure. Nigeria's INF-01 (56.1) is NCC broadband
**subscription** penetration; South Africa's (75.6) and Kenya's (35.0) are **surveys of individuals**. Multi-SIM
ownership means subscription penetration tends to overstate individual use; the 7.5pp NCC-vs-Kepios gap
flagged in week one has never been resolved. A single-indicator pillar is also fragile (Kenya 35.0).

## Finding 4 — worth-watching: GOV-01 is least comparable of any indicator now
- Nigeria 64.5% (142M/220M): denominator assumed; 200-250M gives roughly 71%-57%; numerator includes legal
  residents; the 142M is single-outlet. It lifted Nigeria's Government pillar 56.4 -> 59.1.
- South Africa 63.6% is a carry-forward on an older basis; newer DHA statements (34.7M issued, ~16M green books)
  could not be put on the same basis (claim failed validation). Confidence lowered to low. Likely understated.
- Kenya 40.6% is a fourth consecutive week on a May 2024 base; a June-2026 "34M captured" statement is the
  national ID register, not Maisha Namba.
Three countries, three different constructs. Recommend a documented definition (distinct holders / adult
population) before comparing.

## Finding 5 — worth-watching: not everything was live-verified
Carried forward without a fresh search this cycle: ZAF INF-01, all three ECO-01 (StartupBlink, annual), Kenya
FIN-01 (FinAccess 2024) and the Kenya INF-01 survey. Marked in observations notes. This is below the
standard set on 2026-09-02 ("a repeated score is only trustworthy if the search that produced it was repeated
too"). INF-02 slipped through three cycles for exactly this reason.

## Finding 6 — worth-watching: week label versus evidence dates
This run is labelled 2026-09-09 but was executed on 2026-10-01 and includes evidence published after the label
(Chainalysis 2026 index, 2026-09-23; NIMC 142M, 2026-09-16; DHA, 2026-09-20). The knowledge base holds no runs
for 2026-09-16, 09-23 or 09-30, so the trend line jumps from 09-02 to 09-09. If those weeks were run elsewhere,
re-upload them first; if not, the label should be understood as "first run after 09-02".

## Finding 7 — carried forward, unresolved
FIN-01 three-construct inconsistency (Kenya usage / Nigeria registered / South Africa active mobile-money
accounts), FIN-01 mobile-money framing under-measuring South Africa, no mapping for transaction-volume evidence
(NGA 126,325 transactions per 1000 adults, IMF), ordinal-to-index linearity (08-26 Findings 3, 4, 6, 7). ECO-02
still on FY2025; H1 2026 country totals (NGA $254M, KEN $126M, ZAF $83M) are context only. Kenya FIN-02 stays
missing (outside Chainalysis's published top 20).

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** Coverage ZAF 9/10, NGA 9/10, KEN 8/10. Kenya is lowest,
  but gaps are INF-02 (all three, source failure) and FIN-02 (data-access). Kenya's pillar scores that dropped
  most (Infrastructure) are driven by a missing indicator being excluded, not by being scored as zero. No
  country-specific penalty found, but Kenya's ADCI now leans on fewer indicators.
- **Index structurally rewarding wealth/statistical capacity?** South Africa has the highest ADCI this week
  (55.0) for the first time. That follows from FIN-02 data finally existing, and from the strongest GOV-02 and
  INF-01; it is partly the effect the constitution asks us to watch. Treat as unresolved; revisit once FIN-02 and
  INF-02 are populated for all three.
- **Data gap silently treated as zero?** No. `missing_indicators` lists INF-02 (all three) and FIN-02 (KEN);
  pillar scores are weight-renormalized over present indicators (engine arithmetic replicated).

## No fabrication found
Every non-null value traces to a source ID. Derived values show formulas in `claims.csv`: rank-to-index
(NGA-FIN-02, ZAF-FIN-02, three ECO-01 carried), NGA GOV-01 (142/220), IMF unit conversions.
