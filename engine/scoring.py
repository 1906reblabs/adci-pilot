#!/usr/bin/env python3
"""
ADCI deterministic scoring engine.

This is intentionally plain code, not an LLM call. See
system/SCORING_RULES.md before changing anything here — the normalization,
missing-data, and revision rules are load-bearing for the index's
credibility, not implementation details.

Usage:
    python engine/scoring.py --week 2026-08-18

Reads:
    indicators/INDICATOR_REGISTRY.csv
    evidence/2026/<week>/observations.json

Writes:
    scores/current/adci_scores.json          (overwritten each run)
    scores/historical/<week>.json            (appended, never overwritten)
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "indicators" / "INDICATOR_REGISTRY.csv"
SCORES_CURRENT = ROOT / "scores" / "current" / "adci_scores.json"
SCORES_HISTORICAL_DIR = ROOT / "scores" / "historical"


def load_registry(path: Path) -> dict:
    registry = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["min"] = float(row["min"])
            row["max"] = float(row["max"])
            row["weight"] = float(row["weight"])
            registry[row["id"]] = row
    return registry


def load_observations(week: str) -> list:
    obs_path = ROOT / "evidence" / "2026" / week / "observations.json"
    if not obs_path.exists():
        sys.exit(f"No observations file at {obs_path}. Run agents 01-05 first.")
    with open(obs_path, encoding="utf-8") as f:
        data = json.load(f)
    # accept either a bare list or {"observations": [...]}
    return data["observations"] if isinstance(data, dict) else data


def normalize(value: float, indicator: dict) -> float:
    lo, hi = indicator["min"], indicator["max"]
    if hi == lo:
        return 0.0
    pct = (value - lo) / (hi - lo)
    if indicator["direction"] == "lower":
        pct = 1 - pct
    return max(0.0, min(100.0, pct * 100))


def score_country(country_obs: list, registry: dict) -> dict:
    """Weighted-average up: indicator -> pillar -> ADCI, skipping nulls."""
    pillar_indicators = defaultdict(list)  # pillar -> [(norm_value, weight, confidence)]
    indicator_scores = {}
    missing = []

    for obs in country_obs:
        ind_id = obs["indicator"]
        indicator = registry.get(ind_id)
        if indicator is None:
            continue  # unregistered indicator, ignore rather than guess
        pillar = indicator["pillar"]
        if obs.get("value") is None:
            missing.append(ind_id)
            continue
        norm = normalize(float(obs["value"]), indicator)
        weight = indicator["weight"]
        indicator_scores[ind_id] = {
            "raw_value": obs["value"],
            "normalized": round(norm, 1),
            "confidence": obs.get("confidence", "unknown"),
        }
        pillar_indicators[pillar].append((norm, weight, obs.get("confidence", "unknown")))

    pillar_scores = {}
    for pillar, entries in pillar_indicators.items():
        total_weight = sum(w for _, w, _ in entries)
        if total_weight == 0:
            continue
        weighted = sum(v * w for v, w, _ in entries) / total_weight
        confidences = [c for _, _, c in entries]
        min_confidence = min(confidences, key=lambda c: {"high": 2, "medium": 1, "low": 0, "unknown": -1}.get(c, -1))
        pillar_scores[pillar] = {
            "score": round(weighted, 1),
            "n_indicators": len(entries),
            "partial": any(ind["pillar"] == pillar and obs.get("value") is None
                            for obs, ind in ((o, registry.get(o["indicator"])) for o in country_obs)
                            if ind),
            "min_confidence": min_confidence,
        }

    if pillar_scores:
        adci = sum(p["score"] for p in pillar_scores.values()) / len(pillar_scores)
    else:
        adci = None

    return {
        "adci_score": round(adci, 1) if adci is not None else None,
        "pillars": pillar_scores,
        "indicators": indicator_scores,
        "missing_indicators": missing,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", required=True, help="Week identifier, e.g. 2026-08-18")
    args = parser.parse_args()

    registry = load_registry(REGISTRY_PATH)
    observations = load_observations(args.week)

    by_country = defaultdict(list)
    for obs in observations:
        by_country[obs["country"]].append(obs)

    results = {
        "week": args.week,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "countries": {c: score_country(obs, registry) for c, obs in by_country.items()},
    }

    SCORES_CURRENT.parent.mkdir(parents=True, exist_ok=True)
    SCORES_HISTORICAL_DIR.mkdir(parents=True, exist_ok=True)

    with open(SCORES_CURRENT, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    historical_path = SCORES_HISTORICAL_DIR / f"{args.week}.json"
    if historical_path.exists():
        sys.exit(
            f"{historical_path} already exists. Historical snapshots are never "
            f"overwritten — if this is a genuine revision, add a 'revised_from' "
            f"and 'revision_reason' field by hand and rename, per SCORING_RULES.md."
        )
    with open(historical_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Wrote {SCORES_CURRENT} and {historical_path}")
    for country, data in results["countries"].items():
        print(f"  {country}: ADCI = {data['adci_score']}")


if __name__ == "__main__":
    main()
