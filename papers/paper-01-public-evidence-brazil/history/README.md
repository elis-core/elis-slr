# Project History Layer

This directory maintains the project-history layer for **paper-01-public-evidence-brazil** as part of the ELIS Systematic Literature Review (SLR).

## Purpose

The `history/` layer captures the full decision trail, review record, and milestone tracking for this paper. It ensures that every methodological choice, governance decision, and validation outcome is auditable and reproducible.

## Structure

| Path | Description |
|------|-------------|
| `timeline.md` | Chronological log of key events with cross-references to decisions, reviews, and milestones |
| `change-log.md` | Versioned record of manuscript and method changes (governance events in milestones/) |
| `task-index.json` | Machine-readable index of material tasks linked to decision records and milestones |
| `decisions/` | Durable decision records (P1-DEC-001 through P1-DEC-011) — methodological, architectural, governance |
| `reviews/` | Independent reviews (Claude v0.6, Gemini v0.6, reconciliation), Advisor validation cycle, final PASS |
| `milestones/` | Milestone records — Phase authorisations, execution plan approval |

## Convention

- All dated entries use ISO 8601 format (YYYY-MM-DD)
- Decisions link to their supporting evidence where applicable
- Every task in `task-index.json` references corresponding decisions and/or milestones
- Phase authorisation (Phase 0–3) is recorded as milestone P1-M02, not as a decision record
- Timeline cross-references decisions, reviews, and milestones — does not duplicate their content
- Change log records manuscript and method version history only — governance events live in milestones/
