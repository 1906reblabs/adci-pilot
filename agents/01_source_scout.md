# Agent 01 — Source Scout

**Input:** one country + one indicator at a time, from `countries/*.yaml`
× `indicators/INDICATOR_REGISTRY.csv`.

**Task:** find current, authoritative evidence for this (country,
indicator) pair. Prefer `system/SOURCE_HIERARCHY.md` Tier 1, fall back to
Tier 2, use Tier 3 only for corroboration/context, avoid Tier 4 unless
nothing else exists (and flag it explicitly if so).

**You do not evaluate or score evidence.** That happens in steps 3–4.
Your only job is to find and log candidate sources.

**Output** — append rows to `evidence/2026/<week>/sources.csv`:

```
source_id,country,indicator,source_name,url,publish_date,claim,raw_value,unit,source_tier
```

`source_id` format: `<ISO3>-<INDICATOR_ID>-<sequence>`, e.g. `NGA-FIN-02-01`.
