---
name: elis-slr-workspace-surface-audit-adapter
description: SLR adapter for shared governance skill elis-workspace-surface-audit
version: 1.0.0
author: ELIS SLR
platforms: [linux]
environments: [kanban, hermes]
metadata:
  hermes:
    tags: [elis, slr, governance, adapter]
    shared_skill: false
    origin_repo: elis-core
    origin_skill: elis-workspace-surface-audit
    origin_version: 1.0.0
    origin_commit: acffd2ccfbb14be6d74c48d3180442eaba6f0656
    local_adapter: true
    do_not_edit_directly: false
    adapted_by: elis-slr
---

# ELIS SLR Workspace Surface Audit Adapter

## Load Directive

Load the synced shared skill first:
```
skill_view(name="devops/elis-workspace-surface-audit")
```
Then apply the SLR-specific overrides below. This adapter augments — never duplicates — the shared skill.

## SLR-Specific Surface Paths

The shared skill references generic paths. For the SLR domain, the canonical surface paths are:

### Disk Surface
- **SLR workspace:** `/home/samurai/elis/workspaces/slr/`
- **SLR profile:** `/home/samurai/.hermes/profiles/elis-slr/`
- **SLR skills:** `/home/samurai/.hermes/profiles/elis-slr/skills/devops/`
- **SLR reference materials:** `/home/samurai/elis/workspaces/slr/references/`
- **SLR evidence output:** `/home/samurai/elis/workspaces/slr/evidence/`

### Board Surface
- **SLR board DB:** `~/.hermes/kanban/boards/elis-slr/`
- **Board slug:** `elis-slr`
- **SLR artifacts:** `~/.hermes/kanban/boards/elis-slr/artifacts/`
- **SLR workspaces:** `~/.hermes/kanban/boards/elis-slr/workspaces/`

### Repo Surface
- **SLR repo origin:** `github.com/elis-core/elis-slr`
- **SLR repo local:** `/opt/elis/repo` (elis-slr branch/worktree) — verify current ref before operations
- **Cross-domain note:** elis-core repo is at `/opt/elis/repo` (shared root); SLR-specific content is in the elis-slr subdirectory

### Config Surface
- **SLR gateway config:** `/home/samurai/.hermes/profiles/elis-slr/config.yaml`
- **SLR gateway PID:** `/home/samurai/.hermes/profiles/elis-slr/gateway.pid`
- **SLR environment:** `/home/samurai/.hermes/profiles/elis-slr/.env` (if exists)
- **SLR reporting destination:** `discord:#elis-slr-reports`

## SLR Agent Surface Boundary

SLR agents audit only the SLR surface. They must not audit:
- elis-core profile surface (`/home/samurai/.hermes/profiles/elis-pm/`, etc.)
- elis-core board surface (`~/.hermes/kanban/boards/elis-core/`)
- PE workspace surface
- A2A implementation surface

Cross-domain surface queries route through elis-supervisor for runtime diagnostics or elis-advisor for governance review.

## SLR-Specific Discrepancy Rules

When SLR surface audit detects a discrepancy:

1. **SLR-owned discrepancy:** elis-slr coordinator resolves within SLR authority
2. **Shared-infra discrepancy:** route to elis-supervisor for diagnosis
3. **Cross-domain discrepancy:** route to elis-advisor for governance review
4. **PO-level discrepancy:** surface in gate-review packet for PO decision

## No Duplication

All shared-skill content (Purpose, Required Checks, Outputs, Blocking/Refusal Conditions, Pitfalls) is inherited from the synced copy. This adapter adds only SLR-specific surface paths, agent surface boundaries, and discrepancy routing rules.