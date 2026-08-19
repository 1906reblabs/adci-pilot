# ADCI — Africa Digital Civilization Intelligence

A Claude-Project-run index that measures Africa's transition toward
digitally- and AI-mediated economic civilization. Agents research and
interpret inside the Project; a deterministic Python engine (run there,
via code execution) scores; you export the results to GitHub by hand;
GitHub Pages publishes them.

Pilot scope: **South Africa, Nigeria, Kenya** × **10 indicators**. Expand
only after the methodology proves itself (see `system/METHODOLOGY.md`).

## How it fits together

```
system/                the constitution — rules every agent must follow
indicators/             the indicator registry (schema for what gets measured)
countries/               per-country config (which indicators, notes, overrides)
agents/                  one prompt spec per agent role (Claude plays each role
                         in sequence, in one Project conversation, per AGENT_ROLES.md)
evidence/                raw sourced claims, produced in-session, dated by week
engine/                  scoring.py — deterministic math, NOT an LLM (see below)
scores/                  current/ = latest ADCI scores, historical/ = every past run,
                         nothing is ever overwritten, only appended with a reason
docs/                    the GitHub Pages dashboard (static HTML, reads docs/data/)
PROJECT_INSTRUCTIONS.md  paste into the Claude Project's custom instructions
WEEKLY_RUNBOOK.md        the human checklist — what you do, every week
```

The most important design rule, carried over from the architecture this
repo implements: **the LLM never assigns a country's score directly.**
Agents produce evidence and structured indicator observations;
`engine/scoring.py` does the arithmetic — executed for real, inside the
Project, via its code execution tool. This is what keeps the index
reproducible instead of vibes-based, even without a CI pipeline enforcing
it.

## What's already in this repo

`evidence/2026/2026-08-18/observations.json`, `scores/current/`,
`scores/historical/2026-08-18.json`, and `docs/data/adci_scores.json` are
filled with **sample data** so you can see the whole pipeline — including
`engine/scoring.py` and the dashboard — working end to end before you've
run a single real agent. The scores themselves are made up; the trend
lines in the dashboard are synthetic and labeled as such in the UI. Delete
these and let the first real weekly run populate them, or leave them as a
reference for what the shape of the output should look like.

## Setup

See `WEEKLY_RUNBOOK.md` for the full one-time setup (creating the
Project, turning on code execution, loading knowledge) and the exact
weekly steps. Short version: create the Claude Project, paste
`PROJECT_INSTRUCTIONS.md` into its custom instructions, upload `system/`,
`agents/`, `indicators/`, `countries/`, `engine/scoring.py`, and
`scores/historical/` as Project knowledge, push this repo to GitHub, and
turn on Pages (Settings → Pages → Deploy from branch → `main` / `/docs`).

This version needs no GitHub secrets and no Actions workflow — you're the
one moving files from the Project into the repo each week, which is also
your review step before anything publishes.

## From here to what the original ADCI design doc describes

This repo deliberately sits at stage 1 of that progression: *Claude
Project → prove methodology*, with the Project's knowledge doubling as
*Claude + structured files → institutional memory* rather than a fully
automated pipeline. That's a choice, not a limitation — a human export
step each week is a natural review gate while the methodology is still
being proven. Once you're confident in the pilot and want it unattended,
the natural next move is a GitHub Actions workflow that runs the same
`system/` + `agents/` + `engine/scoring.py` on a schedule instead of you
running it in the Project by hand — everything in this repo is already
shaped for that, if and when you want it.
