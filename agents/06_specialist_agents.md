# Agent 06 — Specialist Agents (one pass per pillar)

**Input:** `evidence/2026/<week>/observations.json`.

**Task:** run one pass per pillar present in the pilot indicator set.
Each pass adds interpretive commentary to the observations belonging to
that pillar — context a reader needs that a bare number doesn't convey.
**None of these passes changes a value or computes a score.**

- **Infrastructure** (INF-*) — think connectivity, broadband economics,
  data centres, energy reliability as a constraint on the above.
- **Finance** (FIN-*) — think fintech, mobile money, stablecoins/crypto,
  regulatory posture toward digital finance.
- **Government** (GOV-*) — think digital ID, public digital services,
  API-based government, regulatory maturity.
- **Economy** (ECO-*) — think startup density, digital trade, investment
  flows, formalization of the digital economy.
- **AI** (AI-*) — think talent (including diaspora), compute access,
  adoption, AI-native company formation, AI governance posture.
- **Society** — no dedicated indicators yet in the pilot registry; write
  one short note per country on digital skills/inclusion signal observed
  incidentally in this week's evidence, flagged as `pillar: "Society"` for
  future indicator design, not scored.

**Output** — add a `pillar_commentary` field to the relevant objects in
`evidence/2026/<week>/observations.json` (a string, 1-3 sentences).
