# Red Team Review — Week of 2026-08-19

This is the pilot's first real (non-sample) run. That context matters for
everything below: several of the issues found here are as much "this is
what an honest week-1 dataset looks like" as they are errors.

## Finding 1 — BLOCKING: Kenya's FIN-01 value measures the wrong thing
Kenya's Finance pillar score (98.0, the highest single-indicator score in
the entire dataset) rests entirely on KEN-FIN-01-01: a Communications
Authority of Kenya figure for *registered mobile-money subscriptions as a
share of population*. The registry defines FIN-01 as "digital/mobile-money
**transactions** per 100 adults" — a demand-side usage measure. CA's own
report explicitly cautions that the 98% figure is supply-side and not a
survey of active individual usage. Both the Data Validator and Source
Critic flagged this independently this week, and confidence was already
marked "low," but the raw value is still driving a near-maximal
normalized score for an entire pillar (n=1 indicator).
**Needs re-running:** KEN / FIN-01, once a genuine demand-side figure is
sourced (recommend CBK's FinAccess survey or GSMA's SOTIR Kenya-specific
90-day active-usage rate, both referenced but not pulled this cycle).

## Finding 2 — BLOCKING: Nigeria's FIN-02 value is an extrapolation, not a published figure
Nigeria's Finance pillar score (98.7, effectively maxed) rests on a
downstream linear conversion of Chainalysis's published global rank
(#2 of 151) into a 0-100 index — a transformation the Evidence Extractor
performed, not something Chainalysis itself published. The rank itself
is well-corroborated across multiple secondary sources this cycle, but
treating an ordinal rank as if it were a cardinal index overstates
precision and, combined with Finding 1, means **both** of this week's
single-indicator Finance pillars are resting on constructs weaker than
they appear from the final number alone.
**Needs re-running:** NGA / FIN-02, once either (a) Chainalysis's own
sub-index scores are located, or (b) the Indicator Agent adopts an
explicit, documented ordinal-to-index convention applied consistently
across all countries (right now only Nigeria has this treatment, since
Kenya's and South Africa's rank-based candidates failed review for
imprecision/staleness — see claims.csv).

## Finding 3 — Worth-watching: South Africa has the most missing data despite the strongest statistical base
South Africa's country notes (`countries/south_africa.yaml`) specifically
flagged a risk of the index rewarding data *availability* over real
progress, given Stats SA / SARB / ICASA's comparatively strong reporting.
This week produced the **opposite** anomaly: South Africa has the fewest
populated indicators of the three pilot countries (5 of 10) and is the
only one missing an **entire pillar** (Finance — both FIN-01 and FIN-02
came up empty). Given SARB and the JSE are generally well-documented,
this looks like a Source Scout sampling gap this cycle, not a genuine
South African data-availability problem — the Scout simply didn't find
South Africa's fintech/crypto evidence this week, while it did for
Nigeria and Kenya. This is worth flagging precisely because it's the
*inverse* of the bias the constitution asks the Red Team to watch for:
here, better-resourced statistical systems didn't translate into better
pilot coverage, because coverage this week was a function of what the
Scout searched for, not what's publicly available. Recommend the next
Source Scout pass explicitly target South African fintech/crypto sources
(SARB, JSE-listed fintechs, Luno/VALR disclosures) to close this gap.

## Finding 4 — Worth-watching: GOV-02, ECO-01, and AI-02 are empty for all three countries
No country produced a validated observation for these three indicators
this week. That's a 100% miss rate on 3 of 10 indicators, which is too
uniform to be a country-specific data-availability story — it's more
likely either (a) a genuine Source Scout coverage gap this cycle, or (b)
these three indicators are harder to find clean, current, country-level
public data for than the other seven (e.g. "share of core government
services fully online" and "active AI-native companies index" don't have
an obvious annual-report-style publisher the way internet penetration or
VC funding do). Recommend the Editor/Calibration Agents track this
specifically — if these three stay empty for multiple consecutive weeks,
that's a conceptual-error signal (per the Constitution's Agent 08
checklist) that these indicators may be poorly specified for what's
actually publicly measurable, not just under-searched.

## Finding 5 — Worth-watching: unreconciled INF-01 disagreements (both directions)
Nigeria (53.0% NCC vs. 45.5% Kepios) and Kenya (35.0% CA+KNBS vs. 40.5%
Kepios) both show real gaps between a Tier-1 regulator/stats-office
figure and a Tier-2 modeled estimate — in Nigeria's case the Tier-1
figure is *higher*, in Kenya's case it's *lower*. That inconsistency in
direction suggests these aren't simply "regulators overstate" or
"Kepios overstates" — they're measuring genuinely different constructs
(network-subscription growth vs. survey-modeled individual users). The
Indicator Agent's tie-break (prefer higher tier) is methodologically
sound per SOURCE_HIERARCHY, but the underlying definitional gap should
be resolved, not just adjudicated by tier, if it recurs next cycle.

## Finding 6 — Worth-watching: ECO-02's GDP-denominator sensitivity
South Africa's ECO-02 value (0.149%) was already flagged low-confidence
by the Source Critic because South Africa's cited nominal GDP ranged from
~$400B to ~$480B across sources found this cycle (World Bank 2024 actual
vs. IMF 2026 projection). Re-computing with the lower figure would move
the raw value to ~0.179% and the normalized pillar score from 3.0 to
~3.6 — directionally the same story (South Africa's disclosed tech
investment is a very small share of GDP relative to Kenya's), so this
does not change the qualitative read, but it's a reminder that ECO-02's
denominator needs a single, consistently-sourced GDP series (recommend
standardizing on IMF WEO, pulled directly rather than via secondary
aggregators, for all three countries next cycle).

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** Not observed
  this week in the direction the constitution anticipates — see Finding
  3, which found the opposite pattern (best-resourced country has the
  most gaps, traceable to Scout sampling rather than data unavailability).
- **Index structurally rewarding wealth/statistical capacity independent
  of real progress?** Too early to tell from n=1 real week — worth
  revisiting once 3-4 weeks of real data exist and pillar coverage
  stabilizes.
- **Data gap silently treated as zero?** No — verified directly in
  `scores/current/adci_scores.json`: missing indicators are listed
  explicitly in `missing_indicators` and excluded from pillar averages
  (confirmed by inspecting `engine/scoring.py`'s `normalize`/
  `score_country` functions, which only process observations with a
  non-null value).

## No fabrication found
No evidence of an agent inventing a number not traceable to a source ID.
Every non-null value in this week's `observations.json` traces to a
`source_id` in `sources.csv`, including the several values that required
an explicit, documented computation (GOV-01 and ECO-02 for multiple
countries) — those computations are shown in `claims.csv` notes and are
independently reproducible from the cited sources.
