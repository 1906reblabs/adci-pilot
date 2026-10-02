# Red Team Review — Week of 2026-08-26

This week's central finding is not a new error — it's confirmation that last week's two
blocking findings were real, and correcting them moved both Kenya's and Nigeria's headline
ADCI scores down (Kenya 55.7 → 48.8, Nigeria 58.5 → 53.2). **This is the single most
important thing for the Editor to get right in this week's brief: these drops are data
corrections, not a real-world decline in digital readiness, and should not be presented
as trend.** See Findings 1 and 2 below.

## Finding 1 — RESOLVED (was blocking): Kenya FIN-01
Last week's blocking finding (registration measure used as usage) is resolved. This
week's value (52.6, from the CBK/KNBS/FSD Kenya 2024 FinAccess demand-side survey) is a
genuinely different, more defensible construct — not a smaller version of the same
overstatement. The -45.4 point swing is arithmetic, not economics: M-Pesa daily-active
usage did not collapse between last week and this week. Confirmed by inspecting
`claims.csv` and `validator_review.csv`: the new claim traces to a named, dated, Tier-1-
origin survey with a stated methodology, unlike last week's uncaveated registration figure.
No further action needed on this specific finding, though see Finding 3 below for a
related, newly-surfaced issue.

## Finding 2 — RESOLVED (was blocking): Nigeria FIN-02
Also resolved, and worth stating plainly: **last week's Nigeria FIN-02 value (98.7,
implying Chainalysis rank #2) was wrong** — not just imprecise, actually wrong. This
week's Source Scout found Chainalysis's own current-edition blog post (published
2025-09-02, still the current edition as of this run) showing Nigeria at rank #6 of 151,
not #2. There is no evidence of a real-world rank change between last week and this week;
last week's Source Scout appears to have pulled from a stale or mismatched Chainalysis
reference. The -2.0 point change this week (98.7 → 96.7) understates how large the actual
correction is, because last week's *rank* (implied #2) was wrong by 4 places, even though
the *converted index values* happen to land close together (98.7 vs 96.7) — a reminder
that the ordinal-to-index formula compresses differences at the top of a long ranked list.
Also note: this week adopted a documented, consistent ordinal-to-index formula
(`100*(N-rank)/(N-1)`), applied to both FIN-02 and all three ECO-01 observations —
directly answering last week's Finding 2 request. See Finding 6 for a residual concern
about that formula itself.

## Finding 3 — NEW, worth-watching: FIN-01 is not measuring the same thing in any of the three countries this week
Kenya's FIN-01 (52.6) is a national household survey's daily-usage rate. Nigeria's FIN-01
(49.45) is an IMF *registered*-accounts count (no *active*-accounts series exists for
Nigeria in the IMF Financial Access Survey). South Africa's FIN-01 (7.26) is an IMF
*active*-accounts count. All three are legitimate, well-sourced, Tier-1-or-close numbers
for what they each measure — but they are three different constructs, not three
comparable readings of the same thing, and the Finance pillar (weight 1.0 in the ADCI
aggregation) is currently the least apples-to-apples pillar in the index as a result.
This is not a repeat of last week's blocking-severity problem (no single value here is
being presented with unwarranted precision or driving a near-maximal, distorting score —
see Finding 5 for why Nigeria's case in particular doesn't rise to blocking), but it does
mean this week's cross-country Finance comparison should be read with real caution.
**Recommend**: next cycle, either (a) locate Nigeria's IMF *active* mobile-money series if
one exists under a different code/vintage, or (b) formally split FIN-01 into two tracked
sub-measures (registration vs. active usage) the way IMF's own FAS schema already does,
rather than quietly picking whichever series is available per country.

## Finding 4 — NEW, worth-watching: FIN-01's "mobile money" framing may not fit South Africa's digital-finance model
South Africa's FIN-01 (7.26) is the lowest of any indicator score in this week's entire
dataset, yet this week's other evidence (GOV-02 = 88.7, best of the three; INF-01 = 75.6;
SARB's PayShap processing 725 million transactions worth R659bn since 2023) paints South
Africa as a highly digitized economy. The likely explanation, flagged in this week's
observations and Integration notes: FIN-01's underlying construct ("mobile money") is a
better fit for telco-led markets (Kenya, much of East/West Africa) than for South Africa's
bank/card/EFT-led digital-payments model. This is a genuine conceptual-error candidate per
the Constitution's Red Team checklist ("is an indicator poorly defined for what it's
trying to capture?") and is now visible in the data for the first time because this is the
first cycle South Africa has any FIN-01 value at all. **Recommend**: METHODOLOGY.md /
INDICATOR_REGISTRY.csv should consider whether FIN-01 needs a rail-agnostic reformulation,
or whether South Africa's low score here is accepted as a genuine (if narrow) measurement
of mobile-money specifically, with a supplementary broader indicator added later.

## Finding 5 — NEW, worth-watching (not blocking): Nigeria FIN-01's registration-based construct
This directly parallels last week's Kenya blocking finding — but is being classified
worth-watching, not blocking, for two reasons: (1) the value (49.45) is a moderate, not
near-maximal, score, so it isn't quietly inflating the Finance pillar to a false ceiling
the way Kenya's 98.0 did last week; (2) the observation notes already caveat this
explicitly and hold confidence at medium rather than high. Still, this is a recurrence of
the same construct issue in a different country, and is worth Simphiwe's attention: if a
genuine active-usage figure for Nigeria surfaces next cycle (NIBSS/CBN publish transaction
*volumes* but not in a form that maps to this indicator's 0-100 scale — see Finding 7),
it should replace this one.

## Finding 6 — worth-watching: the new ordinal-to-index formula is a documented convention, not a solved problem
`100*(N-rank)/(N-1)` is linear in rank, which implicitly treats every one-place rank
difference as equally meaningful — true for standings but not necessarily for the
underlying real-world gap. A country moving from rank 6 to rank 7 of 151 might reflect a
tiny real difference or a large one; the formula can't tell. This is a defensible,
transparent choice (it directly answers last week's request for consistency) but it is a
choice, not ground truth, and the Editor should avoid implying these converted values carry
the same precision as a directly-published cardinal score.

## Finding 7 — worth-watching: some real-world activity doesn't fit the registry's declared 0-100 index scale at all
Nigeria's NIBSS platform processed roughly 11 billion instant-payment transactions in 2024
— a real, well-sourced, Tier-1 number that simply has no defined way to become a 0-100
index value under the current registry (dividing by adult population still produces a
number in the thousands-per-adult range). This week's Indicator Agent correctly declined
to force this into a raw_value rather than fabricate a transformation, but it means a
genuinely strong piece of evidence sat unused this cycle. **Recommend**: METHODOLOGY.md
add an explicit normalization convention for high-volume transaction-count evidence (e.g.,
log-scale, or percentile against a defined global/regional reference set) so this class of
evidence isn't systematically discarded.

## Finding 8 — worth-watching: definitional conflict on AI-02 (recurring pattern from last week's AI-01)
TechCabal Insights' AI-native startup counts (NGA 50, ZAF 49, KEN 31) and SAP/Vanson
Bourne's broader "AI-focused" counts (NGA 456, ZAF 726, KEN 204) diverge by roughly 10-15x
because they use different definitions, not because one is wrong. This is the same pattern
Finding 5 flagged last week for AI-01 (PwC talent-readiness vs. Ataraxis readiness scores)
— now recurring for a second AI indicator. Two divergent-definition situations in two
consecutive cycles, both in the AI pillar, suggests AI-related indicators may be
structurally harder to source with a single settled definition than other pillars.
Recommend the Calibration Agent track this specifically once forecasts built on AI-01/
AI-02 start resolving.

## Coverage this week (contrast with last week's Finding 3)
South Africa: 9 of 10 indicators (only FIN-02 missing). Nigeria: 10 of 10 — complete for
the first time in this pilot. Kenya: 9 of 10 (only FIN-02 missing). Last week's Finding 3
(South Africa had the *worst* coverage despite the *strongest* statistical base) is fully
resolved this cycle — South Africa's Finance-pillar gap has narrowed from "both indicators
missing" to "one of two missing," matching Kenya exactly, and Nigeria has no gaps at all.

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** No evidence of this again this
  week — coverage is now close to even (9/10, 10/10, 9/10) across all three countries.
- **Index structurally rewarding wealth/statistical capacity independent of real
  progress?** This week's evidence argues against this more directly than any prior
  cycle: South Africa — by far the pilot's strongest statistical system — has the
  *lowest* ADCI score this week (49.1, below Nigeria's 53.2), dragged down specifically by
  a Finance-pillar construct mismatch (Finding 4), not by data unavailability. A wealth-
  rewarding index would not produce this result.
- **Data gap silently treated as zero?** No — confirmed again by inspecting
  `scores/current/adci_scores.json`: FIN-02 is listed in `missing_indicators` for both
  South Africa and Kenya and excluded from their Finance-pillar averages (each pillar
  score for those two countries is computed from FIN-01 alone, weight-renormalized, not
  penalized by an implicit zero for FIN-02).

## No fabrication found
Every non-null value in this week's `observations.json` traces to a `source_id` in
`sources.csv`, including derived/converted values (the ordinal-to-index conversions and
unit conversions), each with the formula shown in `claims.csv` notes and independently
reproducible from the cited source.
