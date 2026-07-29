---
name: elis-slr-implementer-self-check-adapter
description: SLR adapter for shared governance skill elis-implementer-self-check
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-implementer-self-check
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Implementer Self-Check Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-implementer-self-check")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR-Specific Agent Identities

The shared skill lists "elis-pm, elis-supervisor, elis-github" as implementing agents. For the SLR domain, the implementing agents are:

- **elis-slr-harvest-impl-a** — Harvest stage implementer
- **elis-slr-screen-impl-b** — Screen stage implementer
- **elis-slr-extract-impl-a** — Extract stage implementer
- **elis-slr-synth-impl-b** — Synthesise stage implementer
- **elis-slr-prisma-impl-b** — PRISMA stage implementer
- **elis-slr** — SLR coordinator (self-check before handoff to SLR validators)

## SLR-Specific Forbidden Literals

Append to the shared-skill forbidden-literal scan:

- `elis-slr-prisma-only` — deprecated name; use `elis-slr-protocol-evidence`
- `elis-slr-prisma-evidence` — deprecated name; use `elis-slr-protocol-evidence`
- Any PRISMA-only evidence-skill naming variant
- `elis-core/board` — elis-core board references in SLR context
- `PE-OPS-*` — PE task IDs in SLR context

## SLR Validation Handoff

Before submitting for SLR validation, the SLR implementing agent must route to:

| Stage | Validator |
|---|---|
| Harvest | elis-slr-harvest-val-b |
| Screen | elis-slr-screen-val-a |
| Extract | elis-slr-extract-val-b |
| Synthesise | elis-slr-synth-val-a |
| PRISMA | elis-slr-prisma-val-a |

The SLR coordinator (elis-slr) performs self-check before handoff to elis-advisor for cross-domain governance review.

## SLR-Specific Paths

- SLR board: `~/.hermes/kanban/boards/elis-slr/`
- SLR workspace: `/home/samurai/elis/workspaces/slr/`
- SLR profile: `/home/samurai/.hermes/profiles/elis-slr/`
- SLR shared skills: `/home/samurai/.hermes/profiles/elis-slr/skills/devops/`

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific identities, paths, forbidden literals, and validation routing.