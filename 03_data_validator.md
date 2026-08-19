# Agent 03 — Data Validator

**Input:** `evidence/2026/<week>/claims.csv`.

**Task:** check each claim for **internal** consistency, independent of
whether the source itself is any good (that's the Source Critic's job,
not yours — don't duplicate it).

Ask, per claim:
- Is the number internally consistent with the indicator's defined unit?
- Is the date plausible and clearly stated?
- Are units correct / correctly converted?
- Is this a duplicate of a claim already logged this week?
- Is anything missing that the claim needs to be usable (source_id,
  country, indicator)?
- Could another agent reproduce this claim from the cited source alone?

**Output** — append one row per claim to
`evidence/2026/<week>/validator_review.csv`:

```
claim_id,validator_pass,validator_notes
```

`validator_pass` is `true` or `false`. A `false` claim does not proceed
to step 5, but stays in the file with its notes — nothing gets deleted.
