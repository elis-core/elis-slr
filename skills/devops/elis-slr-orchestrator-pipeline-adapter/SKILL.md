---
name: elis-slr-orchestrator-pipeline-adapter
description: SLR adapter for shared governance skill elis-orchestrator-pipeline
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-orchestrator-pipeline
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Orchestrator Pipeline Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-orchestrator-pipeline")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR Orchestrator Role

The shared skill lists "PM, Advisor, GitHub" as orchestrator agents. For the SLR domain:

- **SLR orchestrator:** elis-slr (coordinator)
- **SLR pipeline decomposer:** elis-slr
- **SLR stage promoter:** elis-slr
- **Cross-domain reviewer:** elis-advisor (same as shared skill)

The SLR coordinator (elis-slr) owns the full elis-slr board lifecycle. The ELIS PM does not operate the elis-slr board. The Advisor reviews SLR gate packets at cross-domain boundaries.

## SLR Pipeline Stages

The SLR governed pipeline uses these stage names instead of PE stage names:

| Stage | Description | Impl Agent | Val Agent |
|---|---|---|---|
| Harvest | Source selection and query execution | elis-slr-harvest-impl-a | elis-slr-harvest-val-b |
| Screen | Inclusion/exclusion and dedup | elis-slr-screen-impl-b | elis-slr-screen-val-a |
| Extract | Structured data extraction | elis-slr-extract-impl-a | elis-slr-extract-val-b |
| Synthesise | Evidence synthesis and bias eval | elis-slr-synth-impl-b | elis-slr-synth-val-a |
| PRISMA | PRISMA flow and protocol evidence | elis-slr-prisma-impl-b | elis-slr-prisma-val-a |

Each stage has exactly one active path at any time.

## SLR Agent Pool

SLR agents operate on the `elis-slr` board:

- **Coordinator:** elis-slr
- **Implementers:** elis-slr-harvest-impl-a, elis-slr-screen-impl-b, elis-slr-extract-impl-a, elis-slr-synth-impl-b, elis-slr-prisma-impl-b
- **Validators:** elis-slr-harvest-val-b, elis-slr-screen-val-a, elis-slr-extract-val-b, elis-slr-synth-val-a, elis-slr-prisma-val-a
- **Cross-domain:** elis-advisor (governance review), elis-supervisor (runtime diagnostics)

## SLR Board Reference

The shared skill references `~/.hermes/kanban/boards/elis-core/`. For the SLR domain, the board is:

- **Path:** `~/.hermes/kanban/boards/elis-slr/`
- **Slug:** `elis-slr`

## No PE Workflow Governance

The SLR orchestrator does not govern PE workflow, PE chains, PE agent dispatch, or PE board operations. Those are the domain of elis-pm on the elis-core board. Cross-domain coordination is information-only.

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific pipeline stages, agent pool identities, board paths, and domain-boundary rules.