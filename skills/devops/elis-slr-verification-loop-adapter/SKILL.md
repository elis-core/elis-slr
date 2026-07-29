---
name: elis-slr-verification-loop-adapter
description: SLR adapter for shared governance skill elis-verification-loop
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-verification-loop
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Verification Loop Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-verification-loop")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR Agent Role Mapping

The shared skill refers to implementer/Advisor/PO roles generically. For SLR:

| Role | SLR Agent | Notes |
|---|---|---|
| Implementer | elis-slr-harvest-impl-a, elis-slr-screen-impl-b, elis-slr-extract-impl-a, elis-slr-synth-impl-b, elis-slr-prisma-impl-b | Stage-specific |
| Stage Validator | elis-slr-harvest-val-b, elis-slr-screen-val-a, elis-slr-extract-val-b, elis-slr-synth-val-a, elis-slr-prisma-val-a | Stage-specific |
| Cross-Domain Advisor | elis-advisor | Governance review across domains |
| SLR Coordinator | elis-slr | Gate-review and handoff coordination |
| PO | Carlos Rocha | Final approval authority (same across all domains) |

## SLR Validation Criteria (Per Stage)

In addition to the shared-skill checks:

| Stage | SLR-Specific Validation Criteria |
|---|---|
| Harvest | Source coverage, query reproducibility, rate-limit handling |
| Screen | Inclusion/exclusion consistency, duplicate detection accuracy, PRISMA flow accuracy |
| Extract | Data extraction completeness, structured format compliance, inter-rater reliability |
| Synthesise | Heterogeneity assessment, bias evaluation, evidence grading, conclusion support |
| PRISMA | PRISMA flow diagram accuracy, protocol evidence completeness, reporting standard compliance |

## SLR Verification Stage Order

The SLR pipeline stages execute in strict order:

```
Harvest (impl → val)
    → Screen (impl → val)
        → Extract (impl → val)
            → Synthesise (impl → val)
                → PRISMA (impl → val)
                    → Cross-domain Advisor review
                        → PO approval
```

No stage may begin before the previous stage's validation passes.

## SLR PO Escalation Path

When max remediation loops are exhausted (3 loops per stage):

1. SLR stage validator blocks with PARTIAL/FAIL → BLOCKED verdict
2. SLR coordinator reviews: SLR-domain issue vs shared-governance issue
3. SLR-domain: elis-slr presents PO with options A–F (same as shared skill)
4. Shared-governance: route through elis-advisor for cross-domain PO decision

## SLR-Specific Pitfalls

- SLR validators are stage-specific — a harvest validator does not validate screen output
- Cross-stage contamination: extraction issues traced back to screen stage require screen remediation, not extract remediation
- SLR protocol evidence uses canonical name `elis-slr-protocol-evidence` — never the deprecated PRISMA-only name
- The SLR coordinator does not validate implementation output — validators do

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific role mapping, stage-specific validation criteria, stage ordering, and escalation paths.