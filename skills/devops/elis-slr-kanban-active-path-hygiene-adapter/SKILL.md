---
name: elis-slr-kanban-active-path-hygiene-adapter
description: SLR adapter for shared governance skill elis-kanban-active-path-hygiene
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-kanban-active-path-hygiene
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Kanban Active-Path Hygiene Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-kanban-active-path-hygiene")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR Board and Board Path

The shared skill references `~/.hermes/kanban/boards/elis-core/`. For the SLR domain:

- **SLR board:** `~/.hermes/kanban/boards/elis-slr/`
- **Board slug:** `elis-slr`
- **SLR coordinator:** elis-slr (performs active-path hygiene on the elis-slr board)

## SLR Pipeline Chains (Governed)

The SLR board has the following governed chains — one active path per chain:

| Chain | Stages |
|---|---|
| SLR Protocol | Protocol registration → protocol validation |
| SLR Harvest | Query construction → source selection → execution |
| SLR Screen | Title/abstract → full-text → inclusion |
| SLR Extract | Data extraction → quality assessment |
| SLR Synthesise | Evidence synthesis → heterogeneity assessment |
| SLR PRISMA | PRISMA flow → protocol evidence → reporting |

## SLR-Specific Archive Rules

When archiving a parent task on the elis-slr board:

1. Unlink all stale children before parent archive
2. Verify no downstream validation tasks depend on the archived path
3. Archive safety: children on the elis-slr board follow the same auto-archive semantics as elis-core
4. `promote --force` is forbidden on all governed SLR chains

## SLR Orchestrator Identity

The orchestrator performing active-path hygiene on the elis-slr board is **elis-slr** (the SLR coordinator), not elis-pm. The elis-pm does not operate the elis-slr board.

## No Cross-Board Leakage

Active-path hygiene operations on the elis-slr board must never affect:
- The elis-core board
- The elis-a2a-implementation board
- Any PE-governed board

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific board paths, pipeline chains, orchestrator identity, and cross-board isolation rules.