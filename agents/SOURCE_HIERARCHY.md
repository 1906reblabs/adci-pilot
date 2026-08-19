# Source Hierarchy

Used by the Source Scout (to prioritize search) and the Source Critic
(to score `source_quality`). Tier 1 is strongest.

**Tier 1 — Primary / official**
National statistics offices, central banks, telecom regulators
(e.g. ICASA, NCC, CA Kenya), ITU, World Bank, IMF, AfDB, GSMA
Intelligence, company primary disclosures (annual reports, regulatory
filings).

**Tier 2 — Credible secondary / industry**
Established research houses and industry bodies (e.g. Genesis Analytics,
BFA Global, McKinsey Africa, established VC-fund state-of-the-ecosystem
reports), major wire services (Reuters, Bloomberg) reporting primary
data.

**Tier 3 — Journalistic / trade press**
Reputable African and international outlets reporting on developments
without primary data attached (TechCabal, Rest of World, Semafor Africa,
etc.). Usable for context and triangulation, not as the sole source for a
numeric claim.

**Tier 4 — Unverified**
Company press releases with no independent confirmation, social media,
single-source claims with no methodology stated. Never sufficient alone
for a Tier-1-worthy numeric claim; flag and seek corroboration or drop.

A claim's `source_quality` in the evidence CSV is the **lowest** tier
among sources used to support it, unless two independent sources at a
higher tier corroborate it.
