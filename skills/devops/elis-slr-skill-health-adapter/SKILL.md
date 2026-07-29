---
name: elis-slr-skill-health-adapter
description: SLR adapter for shared governance skill elis-skill-health
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-skill-health
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Skill Health Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-skill-health")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR Skill Namespace

The SLR domain has two skill categories:

### SLR-Specific Skills (owned by SLR)

All skills with the `elis-slr-*` prefix. These are domain-specific and amended directly:
- `elis-slr-protocol`
- `elis-slr-harvest`, `elis-slr-screen`, `elis-slr-extract`, `elis-slr-synthesis`
- `elis-slr-integration`, `elis-slr-reference-library`
- `elis-slr-protocol-evidence`, `elis-slr-public-evidence-library`
- `elis-slr-operations`

### SLR Adapter Skills (linked to shared)

All skills with `elis-slr-*-adapter` naming. These adapt shared governance skills:
- `elis-slr-implementer-self-check-adapter`
- `elis-slr-kanban-active-path-hygiene-adapter`
- `elis-slr-orchestrator-pipeline-adapter`
- `elis-slr-skill-health-adapter`
- `elis-slr-verification-loop-adapter`
- `elis-slr-workspace-surface-audit-adapter`

### Synced Shared Skills (read-only)

Skills with `do_not_edit_directly: true`. These are synced from elis-core and must never be amended locally:
- `elis-implementer-self-check`, `elis-kanban-active-path-hygiene`
- `elis-orchestrator-pipeline`, `elis-skill-health`
- `elis-tool-boundary`, `elis-verification-loop`
- `elis-workspace-surface-audit`

Amendments to synced skills must be made at the canonical source (elis-core) and re-synced. When a synced skill produces a recurring failure pattern, the amendment goes to elis-core, not the SLR local copy. The SLR adapter may be amended locally to address SLR-specific failure patterns.

## SLR Advisor Routing

The shared skill references "the Advisor" — for SLR, the same elis-advisor handles cross-domain governance review. For SLR-domain-specific skill-health issues, the SLR coordinator (elis-slr) may perform initial triage before routing to the Advisor.

## SLR Skill Amendment Authority Chain

```
SLR skill failure pattern detected
    → elis-slr triages (SLR-domain vs shared-governance)
        → SLR-domain skill: elis-slr proposes amendment, Advisor validates, PO approves
        → Shared-governance skill: elis-slr reports → elis-core amendment through PM + Advisor + PO
        → Adapter skill: elis-slr amends locally, Advisor validates, PO approves
```

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific skill namespace, amendment authority chain, and Advisor routing rules.