# Project History Layer

This directory maintains the project-history layer for **paper-01-public-evidence-brazil** as part of the ELIS Systematic Literature Review (SLR).

## Purpose

The `history/` layer captures the full decision trail, review record, and milestone tracking for this paper. It ensures that every methodological choice, literature inclusion/exclusion decision, and coding decision is auditable and reproducible.

## Structure

| Path | Description |
|------|-------------|
| `timeline.md` | Chronological log of key events and decisions |
| `change-log.md` | Versioned record of changes to paper content and methodology |
| `task-index.json` | Machine-readable index of SLR tasks and their statuses |
| `decisions/` | Decision records — methodological, coding, literature inclusion/exclusion |
| `reviews/` | Peer and supervisory review records — see `2026-08-07-advisor-final-execution-plan-validation.md` |
| `milestones/` | Milestone tracking for paper progression — see `P1-M02-execution-plan-approved.md` |

## Convention

- All dated entries use ISO 8601 format (YYYY-MM-DD)
- Decisions link to their supporting evidence where applicable
- Every task in `task-index.json` references a corresponding decision or milestone