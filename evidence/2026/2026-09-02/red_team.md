# Red Team Review — Week of 2026-09-02

Headline: **every country's ADCI score is unchanged from last cycle** (ZAF 49.1, NGA 53.2, KEN
48.8). Before accepting that at face value, the first job this week was to check whether "no
change" reflects a genuinely quiet data week or a search process that just re-confirmed old
answers without looking hard enough. Verdict: genuinely quiet — every one of this week's 22
re-confirmation claims was checked against a live source this cycle (not copied from the file),
and the three indicators actively targeted for new evidence (FIN-02 ZAF/KEN, GOV-01 KEN) were
searched with fresh, specific queries, not just re-run boilerplate. See Finding 1.

## Finding 1 — worth-watching: identical scores this week are verified, not assumed
Inspected `sources.csv`: every re-confirmation row for INF-01/INF-02/FIN-01/GOV-01/GOV-02/
ECO-01/ECO-02/AI-01/AI-02 records a genuine check this cycle (e.g. "no newer edition found",
"no newer data point posted") rather than silently repeating last week's row unchanged. This
matters because a pipeline that produces the same score every week without re-verifying invites
exactly the kind of stale-vintage error Finding 2 caught two cycles ago (Nigeria's rank #2 → #6
correction). This week's process avoided that failure mode, but it's worth stating the standard
explicitly for future cycles: **a repeated score is only trustworthy if the search that produced
it was repeated too.**

## Finding 2 — worth-watching (escalated from prior cycles): Kenya's GOV-01 primary-source gap is now confirmed, not just suspected
Two cycles ago, Kenya's GOV-01 (40.6%) was flagged low-confidence because it rested on a May
2024 government statement that kept getting recycled by secondary press without an update. Last
cycle recommended checking immigration.go.ke directly. This cycle did exactly that, and found
**no consolidated coverage statistics published there at all** — only individual press releases
about specific initiatives (KCSE candidate IDs, awareness campaigns). This changes the diagnosis:
the problem is not lazy secondary journalism, it's that Kenya's Directorate of Immigration
Services does not appear to publish a running Maisha Namba coverage number anywhere Claude can
find. Three consecutive weekly cycles have now failed to locate a fresher figure by any method.
**Recommend**: Simphiwe consider whether GOV-01's confidence for Kenya should be formally
downgraded further (a distinct tier below "low," e.g. "stale — no update path currently known"),
and whether the Society-level observation on Kenya's digital-ID reporting cadence (now flagged
three cycles running) has matured enough to justify actually drafting the future Society
indicator these notes keep gesturing at, rather than deferring it again.

## Finding 3 — worth-watching (recurring, unresolved): FIN-01's cross-country construct inconsistency
Unchanged from last cycle's Finding 3: Kenya's FIN-01 is a survey usage rate, Nigeria's is IMF
registered accounts, South Africa's is IMF active accounts — three different constructs, still
not comparable apples-to-apples, and no new evidence this cycle changed that picture in either
direction. Per the project's own "on the horizon" priorities, this remains the single most
significant open methodological issue and has now persisted across three real-data weeks
without a proposed resolution being adopted. Recommend this move from a recurring red-team note
to an actual METHODOLOGY.md revision item on the next occasion Simphiwe has bandwidth for a
non-weekly-run session, rather than being re-logged a fourth time.

## Finding 4 — worth-watching: FIN-02 remains structurally ungettable for two of three countries via the current source strategy
Third consecutive week with no validated FIN-02 for South Africa or Kenya. This cycle
established more precisely *why*: Chainalysis's own SSA regional report gives South Africa and
Kenya real, sourced context (2nd and top-5 in the region by dollar volume respectively) but never
states their position in the global 151-country Overall Index table, which is what this
indicator's ordinal-to-index formula requires. The global table itself is only published as an
interactive map (JavaScript-rendered, not fetchable) beyond the top 20. **This is now a
structural access limitation, not a search-effort gap** — repeating the same search next cycle
is unlikely to produce a different result. Recommend one of: (a) requesting/purchasing access to
Chainalysis's full country data via the linked "Geography of Crypto" report rather than the free
blog post, (b) defining a documented fallback construct for FIN-02 when a global rank is
unavailable (e.g. regional volume rank, converted via a clearly-labeled, lower-confidence
formula), or (c) accepting FIN-02 as structurally partial for these two countries going forward
and reflecting that explicitly in the methodology rather than re-attempting the same search weekly.

## No fabrication found
Every non-null value in this week's `observations.json` traces to a `source_id` in
`sources.csv`. No value was invented, carried forward without a check, or silently guessed for a
missing indicator.

## Bias checks (per ADCI_CONSTITUTION.md)
- **Weaker statistical systems penalized for less data?** No evidence of this — coverage is
  identical to last cycle (9/10, 10/10, 9/10) and both remaining gaps (FIN-02 for ZAF, KEN) are
  the *same* structural data-access issue, not a country-specific penalty.
- **Index structurally rewarding wealth/statistical capacity independent of real progress?**
  Continues to argue against this: South Africa, the pilot's strongest statistical system, still
  has the lowest ADCI score of the three (49.1), still dragged down by the same FIN-01 construct
  mismatch, not by data unavailability.
- **Data gap silently treated as zero?** No — confirmed again in `scores/current/adci_scores.json`:
  FIN-02 remains listed in `missing_indicators` for ZAF and KEN and excluded from their Finance
  pillar averages.
