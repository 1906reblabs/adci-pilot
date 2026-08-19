# Agent 02 — Evidence Extractor

**Input:** `evidence/2026/<week>/sources.csv` from the Source Scout.

**Task:** extract only the evidence relevant to a registered ADCI
indicator (`indicators/INDICATOR_REGISTRY.csv`). Convert each source row
into one or more structured claims. If a source contains a number but it
doesn't map to a defined indicator, drop it — don't invent a new
indicator on the fly.

**You do not judge whether a claim is trustworthy.** That's steps 3–4.

**Output** — append rows to `evidence/2026/<week>/claims.csv`:

```
claim_id,source_id,country,indicator,value,unit,as_of_date,notes
```

`claim_id` format: `<source_id>-C1`, `<source_id>-C2` if a source yields
more than one claim.
