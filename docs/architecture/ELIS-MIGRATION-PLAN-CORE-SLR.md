# ELIS Core / ELIS SLR — Governed Migration Plan Packet

**Status:** Draft (Advisor-Revised) — Awaiting PO Approval Before Any Execution  
**Date:** 2026-06-23  
**Owner:** Carlos Rocha, Product Owner  
**Charter Reference:** `/home/samurai/.hermes/profiles/_shared/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md`

---

## 1. Artefact Inventory — What Belongs in `elis-slr`

**Source root (read-only):** `/home/samurai/openclaw/workspace-prog-impl/repo/`

For each artefact, the `Source` column is the path relative to the source root. The `Destination` column is the path within `elis-slr` after migration. All source files are copied — source repo is never modified.

### 1.1 Protocol and Governance Documents (SLR-only)

| # | Source | Destination in `elis-slr` | Type |
|---|---|---|---|
| P1 | `docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` | `docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` | PDF |
| P2 | `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | Doc |
| P3 | `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` | Doc |
| P4 | `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | Doc |
| P5 | `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | Doc |
| P6 | `docs/_archive/2026-02/ELIS_2025_SLR_Protocol_v1.8.pdf` | `docs/_archive/2026-02/ELIS_2025_SLR_Protocol_v1.8.pdf` | PDF |

### 1.2 SLR Domain Specification Documents

| # | Source | Destination | Type |
|---|---|---|---|
| D1 | `docs/slr/SLR_DOMAIN_SPEC.md` | `docs/slr/SLR_DOMAIN_SPEC.md` | Doc |
| D2 | `docs/slr/HYBRID_SLR_VALIDATION.md` | `docs/slr/HYBRID_SLR_VALIDATION.md` | Doc |
| D3 | `docs/slr/HARVEST_WORKFLOW_CONTRACT.md` | `docs/slr/HARVEST_WORKFLOW_CONTRACT.md` | Doc |
| D4 | `docs/slr/SCREENING_LOCAL_CONTRACT.md` | `docs/slr/SCREENING_LOCAL_CONTRACT.md` | Doc |
| D5 | `docs/slr/SCREENING_GOVERNANCE.md` | `docs/slr/SCREENING_GOVERNANCE.md` | Doc |
| D6 | `docs/slr/EXTRACTION_OFF_HOST_CONTRACT.md` | `docs/slr/EXTRACTION_OFF_HOST_CONTRACT.md` | Doc |
| D7 | `docs/slr/SYNTHESIS_OFF_HOST_CONTRACT.md` | `docs/slr/SYNTHESIS_OFF_HOST_CONTRACT.md` | Doc |
| D8 | `docs/slr/WORKLOAD_PLACEMENT_POLICY.md` | `docs/slr/WORKLOAD_PLACEMENT_POLICY.md` | Doc |
| D9 | `docs/slr/LOCAL_SUPPORT_ANALYSIS.md` | `docs/slr/LOCAL_SUPPORT_ANALYSIS.md` | Doc |

### 1.3 SLR Project Store and Provisioning Documents

| # | Source | Destination | Type |
|---|---|---|---|
| S1 | `docs/openclaw/SLR_PROJECT_STORE_LAYOUT.md` | `docs/openclaw/SLR_PROJECT_STORE_LAYOUT.md` | Doc |
| S2 | `docs/openclaw/SLR_PHASE_WORKSPACE_PROVISIONING_2026-03-25.md` | `docs/openclaw/SLR_PHASE_WORKSPACE_PROVISIONING_2026-03-25.md` | Doc |

### 1.4 SLR Testing Documentation

| # | Source | Destination | Type |
|---|---|---|---|
| T1 | `docs/testing/E2E_TEST_SLR.md` | `docs/testing/E2E_TEST_SLR.md` | Doc |
| T2 | `docs/testing/SLR_QUALITY_CI.md` | `docs/testing/SLR_QUALITY_CI.md` | Doc |
| T3 | `docs/testing/slr-artifacts/passing/good_artifact.json` | `docs/testing/slr-artifacts/passing/good_artifact.json` | Data |
| T4 | `docs/testing/slr-artifacts/failing/bad_artifact.json` | `docs/testing/slr-artifacts/failing/bad_artifact.json` | Data |

### 1.5 SLR Review Archive (15 files — exact)

| # | Source | Destination |
|---|---|---|
| R01 | `docs/reviews/archive/REVIEW_PE-INFRA-SLR-02.md` | `docs/reviews/archive/REVIEW_PE-INFRA-SLR-02.md` |
| R02 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_04.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_04.md` |
| R03 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_07.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_07.md` |
| R04 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_08.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_08.md` |
| R05 | `docs/reviews/archive/REVIEW_PE_SLR_01.md` | `docs/reviews/archive/REVIEW_PE_SLR_01.md` |
| R06 | `docs/reviews/archive/REVIEW_PE_SLR_02.md` | `docs/reviews/archive/REVIEW_PE_SLR_02.md` |
| R07 | `docs/reviews/archive/REVIEW_PE_SLR_03.md` | `docs/reviews/archive/REVIEW_PE_SLR_03.md` |
| R08 | `docs/reviews/archive/REVIEW_PE_SLR_07.md` | `docs/reviews/archive/REVIEW_PE_SLR_07.md` |
| R09 | `docs/reviews/archive/REVIEW_PE_SLR_08.md` | `docs/reviews/archive/REVIEW_PE_SLR_08.md` |
| R10 | `docs/reviews/archive/REVIEW_PE_SLR_09.md` | `docs/reviews/archive/REVIEW_PE_SLR_09.md` |
| R11 | `docs/reviews/archive/REVIEW_PE_SLR_10.md` | `docs/reviews/archive/REVIEW_PE_SLR_10.md` |
| R12 | `docs/reviews/archive/REVIEW_PE_SLR_11.md` | `docs/reviews/archive/REVIEW_PE_SLR_11.md` |
| R13 | `docs/reviews/archive/REVIEW_PE_SLR_12.md` | `docs/reviews/archive/REVIEW_PE_SLR_12.md` |
| R14 | `docs/reviews/archive/REVIEW_PE_SLR_13.md` | `docs/reviews/archive/REVIEW_PE_SLR_13.md` |
| R15 | `docs/reviews/archive/REVIEW_PE_SLR_15.md` | `docs/reviews/archive/REVIEW_PE_SLR_15.md` |

### 1.6 SLR Architecture and Planning Documents

| # | Source | Destination | Type |
|---|---|---|---|
| A1 | `docs/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1.4.md` | `docs/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1.4.md` | Architecture |
| A2 | `ELIS_SLR_AI_Platform_Conceptual_Architecture_v1_9.md` | `ELIS_SLR_AI_Platform_Conceptual_Architecture_v1_9.md` | Architecture |
| A3 | `ELIS_MultiAgent_Implementation_Plan_v1_8_3.md` | `ELIS_MultiAgent_Implementation_Plan_v1_8_3.md` | Planning |
| A4 | `ELIS_MultiAgent_Implementation_Plan_v1_9.md` | `ELIS_MultiAgent_Implementation_Plan_v1_9.md` | Planning |
| A5 | `ELIS_MultiAgent_Implementation_Plan_v2_0.md` | `ELIS_MultiAgent_Implementation_Plan_v2_0.md` | Planning |

### 1.7 Reference Copy of Architecture Charter

| # | Source | Destination | Notes |
|---|---|---|---|
| C1 | `/home/samurai/.hermes/profiles/_shared/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | `docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | **Reference copy only.** Canonical authority remains with the source at `_shared/architecture/`. This copy is for discoverability within the SLR repository. Any conflict is resolved in favour of the `_shared` canonical. |

### 1.8 Initial Commit Metadata

| # | Destination | Content |
|---|---|---|
| M1 | `MIGRATION.md` | Migration provenance document (generated at commit time) |

### 1.9 Artefact Count Summary

See §11 for the complete 43-row manifest with source paths, destinations, categories, copy mode, transform status, secret checks, ownership, and gate assignments.

| Category | Count |
|---|---|
| Protocol documents (§1.1) | 6 |
| Domain specifications (§1.2) | 9 |
| Provisioning docs (§1.3) | 2 |
| Testing docs (§1.4) | 4 |
| Review archive (§1.5) | 15 |
| Architecture/planning (§1.6) | 5 |
| Charter copy (§1.7) | 1 |
| Migration metadata (§1.8) | 1 |
| **Total** | **43** |

### 1.10 Explicitly Excluded from `elis-slr` Migration

The following are **not** repository artefacts to be copied into `elis-slr`. They are runtime/server-side constructs that live on elis-server only and are documented here for completeness — not as migration targets:

| Item | Nature | Why Excluded |
|---|---|---|
| SLR stage workspaces (`workspace-slr-harvest/` etc.) | Server filesystem directories | Runtime workspace skeletons. Managed by the separate `/srv/elis/workspaces/` rename operation. Not a git artefact. |
| SLR agent profiles (11 Hermes profiles) | Server Hermes configuration | Runtime agent profiles. Not in any git repo. Profile configs remain on elis-server. Only SOUL.md path references will point to `elis-slr` paths after workspace rename. |
| SLR Kanban board (`elis-slr`) | Hermes Kanban board | Runtime board. Already operational. Not a git artefact. |

---

## 2. What Remains in `elis-core`

### 2.1 Platform Infrastructure (not SLR-specific)

| Path | Rationale |
|---|---|
| `elis/cli.py` | ELIS CLI — serves both domains |
| `elis/__init__.py`, `elis/__main__.py` | Package root |
| `elis/agent_id.py` | Agent identity — core platform |
| `elis/manifest.py` | Run manifest — core platform |
| `elis/reviewer_identity.py` | Reviewer identity mapping — core |
| `elis/role_surface.py` | Role surface — core |
| `elis/workflow_state_machine.py` | Workflow state machine — core |
| `elis/agentic/asta.py`, `elis/agentic/evidence.py`, `elis/agentic/__init__.py` | Agentic framework — core |
| `scripts/check_agent_scope.py` | Scope check — core |
| `scripts/check_control_plane_wiring.py` | Control plane — core |
| `scripts/dispatch_implementer_runner.py` | Dispatch — core |
| `scripts/pm_assign_pe.py` | PM tooling — core |
| `scripts/gh_bot.py`, `scripts/hello_bot.py` | Bot tooling — core |

### 2.2 SLR-Aware Platform Code (stays in core — shared infrastructure)

These are platform components that SLR domains *use* but are not SLR artefacts themselves. They remain in `elis-core` and are consumed as a dependency by SLR agents.

| Path | Rationale |
|---|---|
| `elis/pipeline/search.py` | Search pipeline — used by Harvest |
| `elis/pipeline/dedup.py` | Dedup pipeline — used by Harvest |
| `elis/pipeline/screen.py` | Screen pipeline — used by Screen |
| `elis/pipeline/merge.py` | Merge pipeline — cross-domain |
| `elis/pipeline/validate.py` | Validate pipeline — cross-domain |
| `elis/sources/base.py` | Source adapter base |
| `elis/sources/config.py` | Source configuration |
| `elis/sources/crossref.py` | Crossref adapter |
| `elis/sources/scopus.py` | Scopus adapter |
| `elis/sources/openalex.py` | OpenAlex adapter |
| `elis/sources/http_client.py` | HTTP client |
| `elis/sources/__init__.py` | Sources package init |
| `elis/hybrid_slr_validation.py` | SLR validation framework — platform code |
| `elis/harvest_workflow.py` | Harvest workflow — platform code |
| `elis/harvest_contract.py` | Harvest contract — platform code |
| `elis/screening_governance.py` | Screening governance — platform code |
| `elis/screening_local_contract.py` | Screening contract — platform code |
| `elis/extraction_offhost_contract.py` | Extraction contract — platform code |
| `elis/synthesis_offhost_contract.py` | Synthesis contract — platform code |
| `elis/workload_placement_policy.py` | Placement policy — platform code |
| `elis/local_support_analysis.py` | Support analysis — platform code |

**Rationale for keeping SLR-aware code in core:** The Python package `elis/` is a monolithic platform package. The SLR pipeline code, source adapters, and contracts are tightly coupled to the core framework (CLI, manifest, state machine, agentic layer). Splitting the Python package requires a separate engineering PE — this is a code refactor, not a file migration. Post-split, these would move to `elis-slr` as a separate package.

### 2.3 Governance Documents (core — reference SLR but govern both domains)

| Path | Rationale |
|---|---|
| `docs/governance/ELIS_Multi_Agent_Governance_Architecture_v2.md` | Governance — covers both domains |
| `docs/governance/ELIS_PE_Operating_Protocol.md` | PE protocol — covers both domains |
| `docs/governance/ELIS_Token_Usage_Guidelines_for_Multi_AI_Agents.md` | Token guidelines — covers both |
| `docs/governance/ELIS_Token_Usage_Guidelines_Implementation_Plan.md` | Token implementation — covers both |
| `docs/architecture/ELIS_Core_SLR_Architecture_Charter_and_Routing.md` | **Already in elis-core** — canonical location |

### 2.4 Schemas and Data (shared infrastructure)

| Path | Rationale |
|---|---|
| `schemas/` (all files) | Schema definitions — consumed by both domains |
| `json_jsonl/` (all files) | Runtime data — historical, cross-domain |

### 2.5 Tests

Test files are cross-cutting. A test-by-test classification is deferred to the Python package split PE. All tests remain in `elis-core`. SLR-specific tests will move to `elis-slr` as part of the package split.

---

## 3. Current Source Paths and Existing Remotes

### 3.1 Active Git Clones on elis-server

| Path | Remote | Branch |
|---|---|---|
| `/opt/elis/repo/` | `https://github.com/rochasamurai/ELIS-Multi-AI-Agent-Platform.git` | `feature/pe-ops-a2a-loopback-01-v2` |
| `/home/samurai/openclaw/workspace-prog-impl/repo/` | Same | (various) |
| `/home/samurai/ELIS-SLR-Agent/` | Same | (unknown) |

### 3.2 Target Repositories

| Repository | URL | Current State |
|---|---|---|
| `elis-core` | `https://github.com/elis-core/elis-core` | Active — existing content |
| `elis-slr` | `https://github.com/elis-core/elis-slr` | **Foundation — empty, created 2026-06-23** |

---

## 4. History Strategy — Start Clean

**Recommendation: Start clean for `elis-slr`.**

Rationale:

1. The `elis/` Python package is a monorepo that cannot be cleanly `git filter-repo`'d without breaking the platform code that remains in `elis-core`. A filtered history would produce a non-functional codebase.

2. The `ELIS-SLR-Agent/` directory already contains a snapshot subset of SLR files — it was clearly intended as a clean-slate SLR repo.

3. The SLR document artefacts (protocol PDFs, SLR domain docs, review archives) have their own provenance in their content. Git history adds little value for documents.

4. The monorepo history remains preserved in `elis-core`. Nothing is lost.

**Approach:**

- `elis-slr` receives a single initial commit containing the 43 artefacts listed in the §11 manifest (42 copied + 1 generated).
- The commit message records provenance: "Initial population from ELIS monorepo (`rochasamurai/ELIS-Multi-AI-Agent-Platform`). See `elis-core` for full git history."
- `elis-core` retains all git history intact. No history rewrite in `elis-core`.
- A `MIGRATION.md` file is placed at the root of `elis-slr` documenting the source, date, scope, and artefact count of the initial population.

---

## 5. GitHub Operation Owner and Approval Gates

### 5.1 Execution Owner

**ELIS GitHub** (`elis-github` profile) performs all GitHub operations, after explicit PO approval per operation.

### 5.2 Operation Sequence and Gates

| Step | Operation | Owner | Gate |
|---|---|---|---|
| G1 | Clone `elis-slr` to staging area | ELIS GitHub | PO approval |
| G2 | Copy SLR artefacts into clone (43 files, per §1 manifest) | ELIS Supervisor | PO approval (filesystem only, no git push) |
| G3 | Review staged content against manifest | ELIS Advisor | Governance/readiness review |
| G4 | Commit and push to `elis-slr` | ELIS GitHub | PO approval per push |
| G5 | Verify `elis-slr` content on GitHub | ELIS Supervisor | Evidence report |
| G6 | Post-migration review | ELIS Advisor | Governance PASS |
| G7 | Closure | PO | Final sign-off |

**Push authorisation boundary:** No push, force-push, or remote rewrite is authorised by this plan alone. G4 may authorise a normal push only after separate PO approval. Force-push and remote rewrite are out of scope unless separately approved.

---

## 6. Rollback Plan

### 6.1 Pre-push Rollback

Before G4 (push), rollback is trivial:
- Delete the staging clone directory.
- No remote state has changed.

### 6.2 Post-push Rollback

After G4, if rollback is required, a separate PO-approved rollback operation must be executed by ELIS GitHub. The preferred method is reverting the population commit (a new commit that removes the migrated content). Explicit PO approval is required for any alternative action.

No force-push or repository deletion is authorised by this migration plan.

### 6.3 Safety Guarantees

- No planned mutation to `elis-core`. Residual operational risk is limited to accidental execution error and is mitigated by read-only source handling.
- `elis-slr` is empty pre-migration. No data can be lost.
- The source monorepo (`rochasamurai/ELIS-Multi-AI-Agent-Platform`) is never modified.
- All migration operations are additive only.

---

## 7. Profile/Workspace Rebinding Impact

### 7.1 Immediate Impact (Post-Migration)

| Profile | Current Reference | Post-Migration Reference |
|---|---|---|
| `elis-slr/SOUL.md` | `/home/samurai/openclaw/workspace-slr-harvest/repo/...` | `/srv/elis/workspaces/slr/repo/docs/_active/...` |
| `elis-slr/skills/.../slr-protocol-guidance.md` | `/home/samurai/openclaw/workspace-prog-impl/repo/...` | `/srv/elis/workspaces/slr/repo/docs/_active/...` |
| `elis-pm/skills/.../slr-protocol-guidance.md` | Same | Same |

These are **path references**, not git remotes. They change when the `/srv/elis/workspaces/` rename is executed (separate PO-approved operation).

### 7.2 Git Remote Rebinding (Future — Not Part of This Migration)

No agent profile currently has a git remote configured. Agent profiles use `cwd: .` (their profile directory) except `elis-github` (`/opt/elis/agent-worktrees/github-agent`). Git remote rebinding is only needed when:

1. The Python package split is complete (separate PE).
2. SLR agents need to clone `elis-slr` for PE operations.
3. The `/srv/elis/workspaces/slr/repo/` clone exists and is ready for use.

This is deferred to a future "SLR Agent Git Enablement" PE.

### 7.3 Profiles Not Touched

No Hermes profile config, `.env`, SOUL.md, or AGENTS.md is modified during this migration except the path references documented above (which are part of the workspace rename, not the GitHub migration).

---

## 8. Advisor Review Requirements

### 8.1 Pre-Execution Review

- Confirm artefact inventory (§1) correctly separates SLR artefacts from core platform code, and all 43 files in the §11 manifest exist at stated source paths.
- Confirm destination paths are consistent and non-colliding within `elis-slr`.
- Confirm the Python package split deferral (§2.2 rationale) is sound.
- Confirm clean-history strategy (§4) does not lose irreplaceable provenance.
- Confirm rollback plan (§6) covers both pre-push and post-push states without force-push.

### 8.2 Post-Execution Review

- Verify `elis-slr` contains exactly the 43 artefacts listed in the §11 manifest (42 copied + 1 generated).
- Verify `elis-core` is unmodified.
- Verify no secret exposure in committed content.
- Verify `MIGRATION.md` is present, accurate, and matches the manifest.

---

## 9. PO Approval Gates

| Gate | What | When |
|---|---|---|
| **A** | Approve this migration plan | Before any file copy |
| **B** | Approve staging area population (G2) | Before copy to staging |
| **C** | Approve push to `elis-slr` (G4) | After Advisor review of staged content |
| **D** | Closure or further instructions (G7) | After post-migration verification |

Each gate is explicit. No gate implies the next.

---

## 10. Out of Scope (Explicitly Deferred)

| Item | Deferred To |
|---|---|
| Python package split (`elis/` → `elis-core` + `elis-slr` packages) | Separate engineering PE |
| SLR agent git remote binding | "SLR Agent Git Enablement" PE |
| Profile `.env` propagation for SLR agents | Separate PO-authorized operation |
| `/srv/elis/workspaces/` filesystem rename | Separate PO-approved operation |
| Workspace-to-agent `cwd` binding | Post-rename configuration PE |
| `elis-slr` CI/workflow setup | Post-population infrastructure PE |
| Removal of SLR content from `elis-core` | Post-split cleanup (after package split) |
| Gateway activation changes | Separate PO-authorized operation |

---

## 11. Exact Migration Manifest (Before Gate B)

Each row is a single file — no wildcards, ranges, or directory-level entries.
All source paths are relative to `/home/samurai/openclaw/workspace-prog-impl/repo/`
unless prefixed with an absolute path.

| # | Source | Destination in `elis-slr` | Category | Copy Mode | Transform | Secret Check | Owner | Gate |
|---|---|---|---|---|---|---|---|---|
| **Protocol Documents (§1.1)** |
| P1 | `docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` | `docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` | Protocol | Copy | As-is | Pass | Supervisor | B |
| P2 | `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | Protocol | Copy | As-is | Pass | Supervisor | B |
| P3 | `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` | Protocol | Copy | As-is | Pass | Supervisor | B |
| P4 | `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | Protocol | Copy | As-is | Pass | Supervisor | B |
| P5 | `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | Protocol | Copy | As-is | Pass | Supervisor | B |
| P6 | `docs/_archive/2026-02/ELIS_2025_SLR_Protocol_v1.8.pdf` | `docs/_archive/2026-02/ELIS_2025_SLR_Protocol_v1.8.pdf` | Protocol | Copy | As-is | Pass | Supervisor | B |
| **Domain Specifications (§1.2)** |
| D1 | `docs/slr/SLR_DOMAIN_SPEC.md` | `docs/slr/SLR_DOMAIN_SPEC.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D2 | `docs/slr/HYBRID_SLR_VALIDATION.md` | `docs/slr/HYBRID_SLR_VALIDATION.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D3 | `docs/slr/HARVEST_WORKFLOW_CONTRACT.md` | `docs/slr/HARVEST_WORKFLOW_CONTRACT.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D4 | `docs/slr/SCREENING_LOCAL_CONTRACT.md` | `docs/slr/SCREENING_LOCAL_CONTRACT.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D5 | `docs/slr/SCREENING_GOVERNANCE.md` | `docs/slr/SCREENING_GOVERNANCE.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D6 | `docs/slr/EXTRACTION_OFF_HOST_CONTRACT.md` | `docs/slr/EXTRACTION_OFF_HOST_CONTRACT.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D7 | `docs/slr/SYNTHESIS_OFF_HOST_CONTRACT.md` | `docs/slr/SYNTHESIS_OFF_HOST_CONTRACT.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D8 | `docs/slr/WORKLOAD_PLACEMENT_POLICY.md` | `docs/slr/WORKLOAD_PLACEMENT_POLICY.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| D9 | `docs/slr/LOCAL_SUPPORT_ANALYSIS.md` | `docs/slr/LOCAL_SUPPORT_ANALYSIS.md` | Domain spec | Copy | As-is | Pass | Supervisor | B |
| **Provisioning Documents (§1.3)** |
| S1 | `docs/openclaw/SLR_PROJECT_STORE_LAYOUT.md` | `docs/openclaw/SLR_PROJECT_STORE_LAYOUT.md` | Provisioning | Copy | As-is | Pass | Supervisor | B |
| S2 | `docs/openclaw/SLR_PHASE_WORKSPACE_PROVISIONING_2026-03-25.md` | `docs/openclaw/SLR_PHASE_WORKSPACE_PROVISIONING_2026-03-25.md` | Provisioning | Copy | As-is | Pass | Supervisor | B |
| **Testing Documentation (§1.4)** |
| T1 | `docs/testing/E2E_TEST_SLR.md` | `docs/testing/E2E_TEST_SLR.md` | Testing | Copy | As-is | Pass | Supervisor | B |
| T2 | `docs/testing/SLR_QUALITY_CI.md` | `docs/testing/SLR_QUALITY_CI.md` | Testing | Copy | As-is | Pass | Supervisor | B |
| T3 | `docs/testing/slr-artifacts/passing/good_artifact.json` | `docs/testing/slr-artifacts/passing/good_artifact.json` | Testing | Copy | As-is | Pass | Supervisor | B |
| T4 | `docs/testing/slr-artifacts/failing/bad_artifact.json` | `docs/testing/slr-artifacts/failing/bad_artifact.json` | Testing | Copy | As-is | Pass | Supervisor | B |
| **Review Archive (§1.5)** |
| R01 | `docs/reviews/archive/REVIEW_PE-INFRA-SLR-02.md` | `docs/reviews/archive/REVIEW_PE-INFRA-SLR-02.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R02 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_04.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_04.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R03 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_07.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_07.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R04 | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_08.md` | `docs/reviews/archive/REVIEW_PE_INFRA_SLR_08.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R05 | `docs/reviews/archive/REVIEW_PE_SLR_01.md` | `docs/reviews/archive/REVIEW_PE_SLR_01.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R06 | `docs/reviews/archive/REVIEW_PE_SLR_02.md` | `docs/reviews/archive/REVIEW_PE_SLR_02.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R07 | `docs/reviews/archive/REVIEW_PE_SLR_03.md` | `docs/reviews/archive/REVIEW_PE_SLR_03.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R08 | `docs/reviews/archive/REVIEW_PE_SLR_07.md` | `docs/reviews/archive/REVIEW_PE_SLR_07.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R09 | `docs/reviews/archive/REVIEW_PE_SLR_08.md` | `docs/reviews/archive/REVIEW_PE_SLR_08.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R10 | `docs/reviews/archive/REVIEW_PE_SLR_09.md` | `docs/reviews/archive/REVIEW_PE_SLR_09.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R11 | `docs/reviews/archive/REVIEW_PE_SLR_10.md` | `docs/reviews/archive/REVIEW_PE_SLR_10.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R12 | `docs/reviews/archive/REVIEW_PE_SLR_11.md` | `docs/reviews/archive/REVIEW_PE_SLR_11.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R13 | `docs/reviews/archive/REVIEW_PE_SLR_12.md` | `docs/reviews/archive/REVIEW_PE_SLR_12.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R14 | `docs/reviews/archive/REVIEW_PE_SLR_13.md` | `docs/reviews/archive/REVIEW_PE_SLR_13.md` | Review | Copy | As-is | Pass | Supervisor | B |
| R15 | `docs/reviews/archive/REVIEW_PE_SLR_15.md` | `docs/reviews/archive/REVIEW_PE_SLR_15.md` | Review | Copy | As-is | Pass | Supervisor | B |
| **Architecture and Planning (§1.6)** |
| A1 | `docs/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1.4.md` | `docs/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1.4.md` | Architecture | Copy | As-is | Pass | Supervisor | B |
| A2 | `ELIS_SLR_AI_Platform_Conceptual_Architecture_v1_9.md` | `ELIS_SLR_AI_Platform_Conceptual_Architecture_v1_9.md` | Architecture | Copy | As-is | Pass | Supervisor | B |
| A3 | `ELIS_MultiAgent_Implementation_Plan_v1_8_3.md` | `ELIS_MultiAgent_Implementation_Plan_v1_8_3.md` | Planning | Copy | As-is | Pass | Supervisor | B |
| A4 | `ELIS_MultiAgent_Implementation_Plan_v1_9.md` | `ELIS_MultiAgent_Implementation_Plan_v1_9.md` | Planning | Copy | As-is | Pass | Supervisor | B |
| A5 | `ELIS_MultiAgent_Implementation_Plan_v2_0.md` | `ELIS_MultiAgent_Implementation_Plan_v2_0.md` | Planning | Copy | As-is | Pass | Supervisor | B |
| **Charter Copy (§1.7)** |
| C1 | `/home/samurai/.hermes/profiles/_shared/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | `docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | Governance | Copy | As-is | Pass | Supervisor | B |
| **Migration Metadata (§1.8)** |
| M1 | (none — generated) | `MIGRATION.md` | Metadata | N/A | Generated | Pass | Supervisor | B |

**Manifest summary:** 43 rows. 42 files copied as-is from source; 1 file (M1) generated at commit time. All secret checks pass. All execution owners: ELIS Supervisor. All approval gates: Gate B (staging population).

---

## 12. Pre-Flight Manifest Validation

Before Gate B (staging population), ELIS Supervisor must verify every file in the §11 manifest exists at its stated source path. The verification must produce a 43-row pass/fail table as evidence.

This verification must be performed and evidenced before any file copy.