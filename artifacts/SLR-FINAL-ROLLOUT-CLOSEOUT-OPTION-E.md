# SLR-FINAL-ROLLOUT-CLOSEOUT-OPTION-E — Combined Closeout Planning Packet

**Status:** PO-approved Option E planning only. Non-executing. No mutation of any lane.  
**Origin task:** t_19ac23fd (completed 2026-07-22)  
**Remediation:** Loop 1 — durable artifact regeneration + exclusions fix  
**Kanban task:** t_28a603b3  
**Run ID:** 102  
**Date:** 2026-07-22

---

## Executive Summary

This planning packet covers the three closeout lanes required to finalise the SLR agent profile rollout
(Stages 1–8) and transition to steady-state Kanban operations:

1. **Lane A — Repo Synchronisation:** Classify 30+ files into governance, architecture, skills,
   and profile identity categories with explicit runtime exclusions. No GitHub action.
2. **Lane B — Durable Skill/Template Persistence:** Rule 9 and gate-review rule are already durable
   in `_shared/`. The 3-loop remediation limit is the identified gap — proposed as governance addendum.
3. **Lane C — Runtime/Gateway Activation:** 12 worker profiles are pure Kanban (no gateway needed).
   Coordinator gateway is running; health checks and rollback path documented.

**This packet does NOT execute any lane.** It is a planning artifact for PO review and Advisor validation.

---

## Profile Manifest (13 total)

| # | Profile | Role | Gateway |
|---|---------|------|---------|
| 1 | elis-slr | Coordinator (kanban-worker overhead) | Running (hermes-gateway-elis-slr.service, channel 1518718649383387278) |
| 2 | elis-slr-harvest-impl-a | Harvest implementer | None (pure Kanban) |
| 3 | elis-slr-harvest-val-b | Harvest validator | None (pure Kanban) |
| 4 | elis-slr-screen-impl-b | Screen implementer | None (pure Kanban) |
| 5 | elis-slr-screen-val-a | Screen validator | None (pure Kanban) |
| 6 | elis-slr-extract-impl-a | Extract implementer | None (pure Kanban) |
| 7 | elis-slr-extract-val-b | Extract validator | None (pure Kanban) |
| 8 | elis-slr-synth-impl-b | Synthesis implementer | None (pure Kanban) |
| 9 | elis-slr-synth-val-a | Synthesis validator | None (pure Kanban) |
| 10 | elis-slr-protocol-impl-b | Protocol finalisation implementer | None (pure Kanban) |
| 11 | elis-slr-protocol-val-a | Protocol finalisation validator | None (pure Kanban) |
| 12 | elis-slr-integration-impl-a | Integration implementer | None (pure Kanban) |
| 13 | elis-slr-integration-val-b | Integration validator | None (pure Kanban) |

**Worker model assignments:**
- Implementers: `qwen/qwen3-coder-flash` (OpenRouter)
- Validators: `z-ai/glm-5` (OpenRouter)

---

## Stage 1–8 Rollout Evidence References

| Stage | Description | Profiles Created | Evidence Task |
|-------|-------------|-----------------|---------------|
| 1 | Harvest | elis-slr-harvest-impl-a, elis-slr-harvest-val-b | Prior PE tasks |
| 2 | Screen | elis-slr-screen-impl-b, elis-slr-screen-val-a | Prior PE tasks |
| 3 | Extract | elis-slr-extract-impl-a, elis-slr-extract-val-b | Prior PE tasks + SLR-STAGE-3-VALIDATION-ADDENDUM-01 |
| 4 | Knowledge Recovery | Classification + adoption artifacts | SLR-KNOWLEDGE-RECOVERY-01 (artifacts/ dir) |
| 5 | Kanban Compliance | Coordinator + worker skill layout | SLR-KANBAN-COMPLIANCE-ROLLBACK.md |
| 6 | Synthesis | elis-slr-synth-impl-b, elis-slr-synth-val-a | SLR-STAGE-6-SYNTHESIS-ROLLBACK.md |
| 7 | Protocol Finalisation | elis-slr-protocol-impl-b, elis-slr-protocol-val-a | SLR-STAGE-7-PROTOCOL-ROLLBACK.md |
| 8 | Integration | elis-slr-integration-impl-a, elis-slr-integration-val-b | SLR-STAGE-8-INTEGRATION-ROLLBACK.md |

All rollback artifacts are in: `/home/samurai/.hermes/kanban/boards/elis-slr/artifacts/`

---

## Lane A: Repo Synchronisation Planning

### Candidate Files

#### Governance (6 files)
- `_shared/GOVERNANCE.md`
- `_shared/SECURITY.md`
- `_shared/LEARNING.md`
- `_shared/STATUS.md`
- `_shared/TERMINOLOGY.md`
- `_shared/OBSIDIAN.md`

#### Architecture (6 files)
- `_shared/architecture/ELIS-ARCHITECTURE-PO-AGENTS-ROLES-MODELS-PROVIDERS_PLATFORM_TRANSITION_CORRECTED.md`
- `_shared/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md`
- `_shared/architecture/ELIS-GATE-B-EVIDENCE.md`
- `_shared/architecture/ELIS-GATE-B-STAGING-EVIDENCE.md`
- `_shared/architecture/ELIS-GATE-B-STAGING-EXECUTION.md`
- `_shared/architecture/ELIS-MIGRATION-PLAN-CORE-SLR.md`

#### Skills / Standards (3 files)
- `_shared/skills/AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL.md`
- `_shared/skills/ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL.md`
- `_shared/standards/ELIS_Agent_Communication_Skill_Best_Practices_Artifact_Exchange.md`

#### Profile Identity (~39 files)
- `elis-slr/SOUL.md`, `elis-slr/AGENTS.md`, `elis-slr/SKILLS.md` (coordinator: 3 files)
- 12 worker profiles × 3 identity files each = 36 files
- Total profile identity: 39 files

#### Rollback Artifacts (4 files)
- `SLR-KANBAN-COMPLIANCE-ROLLBACK.md` (SHA256: prior art)
- `SLR-STAGE-6-SYNTHESIS-ROLLBACK.md` (SHA256: `6e94a799...`)
- `SLR-STAGE-7-PROTOCOL-ROLLBACK.md` (SHA256: prior art)
- `SLR-STAGE-8-INTEGRATION-ROLLBACK.md` (SHA256: prior art)

**Total candidate files (including rollbacks): ~58 files**

### Explicitly Excluded (NOT for repo sync)

| Category | Patterns |
|----------|----------|
| Runtime config | `config.yaml`, `.env`, `auth.*` |
| Gateway state | `gateway_state.json`, `gateway.lock`, `gateway.pid` |
| Session data | `logs/`, `sessions/`, `audio_cache/`, `sandboxes/` |
| Database | `state.db*` |
| Channel state | `channel_directory.json` |
| Runtime binaries | `bin/`, `cache/`, `checkpoints/` |
| Pairing data | `pairing/` |
| Agent runtime | `memories/`, `cron/`, `hooks/` |
| Dev cache | `models_dev_cache.json` |
| Bundled skills | `skills/ (bundled copies)` |
| Backups | `*.bak*` |

### Branch Strategy (proposed)
- Base: `main`
- Feature branch: `feature/slr-closeout-option-e`
- No push/PR/merge in this planning task
- Future PE: elis-github executes after PO approval

---

## Lane B: Durable Skill/Template Persistence

### Rule 9 — Validation Lifecycle Enforcement

**Status:** Already durable ✅  
**Location:** `_shared/skills/AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL.md` §9  
**Content:** PASS → kanban_complete → done; PARTIAL/FAIL/BLOCKED → kanban_block → blocked  
**Action required:** None. Rule is already in shared governance.

### Gate-Review Rule — Permanent SLR Gate Review

**Status:** Already durable ✅  
**Location:** `_shared/GOVERNANCE.md` — PE Rules + Role Separation + Evidence Discipline  
**Content:** Advisor reviews; PO approves. No self-approval. Independent validation mandatory.  
**Action required:** None. Rule is already in shared governance.

### 3-Loop Remediation Limit

**Status:** Gap — not yet durable ⚠️  
**Proposal:** Add `REMEDIATION_LOOP_LIMIT_RULE` to `_shared/GOVERNANCE.md`:
- Maximum 3 remediation loops per implementation task
- After 3rd non-PASS validation verdict, block and surface PO decision with options A–F
- PO directive required after 3 failures
**Action required:** Governance addendum (future PE, after PO approval)
**Candidate file:** `_shared/GOVERNANCE.md` (append new section)

### Proposed Mutation Plan (future PE, not this task)
1. PO approves governance addendum content
2. elis-supervisor patches `_shared/GOVERNANCE.md` with remediation loop limit rule
3. elis-advisor validates
4. Commit to repo (elis-github)

---

## Lane C: Runtime/Gateway Activation

### Coordinator Gateway
- **Service:** `hermes-gateway-elis-slr.service` (user systemd)
- **Status:** Running
- **Channel:** 1518718649383387278 (coordinator home)
- **Reporting channel:** 1519705198275203215 (`#elis-slr-reports`, send_message only, not gateway-bound)

### Worker Gateways
- **Status:** None needed ✅
- **Rationale:** All 12 worker profiles dispatch via pure Kanban on elis-server.
  No Discord gateway binding required. The coordinator is the sole gateway profile.

### Health Checks (proposed for future PE)
```bash
# Coordinator gateway liveness
systemctl --user is-active hermes-gateway-elis-slr.service

# Kanban dispatcher liveness
hermes kanban ping --board elis-slr

# Profile dispatch test (dry-run)
hermes kanban create "SLR-CLOSEOUT-HEALTHCHECK" --assignee elis-slr-harvest-impl-a --board elis-slr
```

### Rollback / Disable Path
```bash
# Stop coordinator gateway
systemctl --user stop hermes-gateway-elis-slr.service

# OR disable Kanban dispatch in gateway (config-only, no service stop)
# Set in config.yaml: kanban.dispatch_in_gateway: false
```

### No-Op Path
- If all 12 workers dispatch correctly via Kanban without gateway, no gateway activation changes are needed.
- Coordinator gateway remains as-is.
- No new services, no new channels, no new bindings.

---

## Rollback Artifacts (4, in artifacts/ dir)

| Artifact | SHA256 Prefix | Scope |
|----------|--------------|-------|
| SLR-KANBAN-COMPLIANCE-ROLLBACK.md | prior art | Coordinator + worker skill layout |
| SLR-STAGE-6-SYNTHESIS-ROLLBACK.md | 6e94a799 | Remove elis-slr-synth-impl-b, elis-slr-synth-val-a |
| SLR-STAGE-7-PROTOCOL-ROLLBACK.md | prior art | Remove elis-slr-protocol-impl-b, elis-slr-protocol-val-a |
| SLR-STAGE-8-INTEGRATION-ROLLBACK.md | prior art | Remove elis-slr-integration-impl-a, elis-slr-integration-val-b |

---

## Risks and Blockers

| Severity | Risk | Mitigation |
|----------|------|------------|
| MEDIUM | No durable 3-loop remediation limit | Codify before next remediation cycle (future PE) |
| MEDIUM | elis-slr repo contains no profile identity files | This packet proposes sync plan; PO must approve |
| LOW | Coordinator SOUL topology stale (lists PRISMA, omits Integration/Protocol) | Defer to PE; coordinator SOUL update is non-blocking |
| LOW | PRISMA profiles exist without elis-slr- prefix | Migration deferred; current profiles use correct prefix |

---

## Known Gaps

1. **3-loop remediation limit** — not codified in shared governance (see Lane B)
2. **Coordinator SOUL topology** — references pre-Stage-7 state (PRISMA profiles)
3. **PRISMA naming convention** — legacy profiles lack `elis-slr-` prefix
4. **Repo sync execution** — no profile identity files committed to elis-slr repo yet

---

## Proposed Sequencing

1. ✅ Option E planning (t_19ac23fd — original; t_28a603b3 — remediation)
2. ⏳ Advisor validation (t_b01cda70 — blocked, awaiting this remediation)
3. ⬜ PO approval
4. ⬜ Repo sync execution (future PE)
5. ⬜ Governance addendum for 3-loop limit (future PE)
6. ⬜ Coordinator topology fix (future PE)
7. ⬜ Closeout health check

---

## Explicit Exclusions (13/13 — complete)

This planning packet does NOT authorise:

1. ❌ Repo synchronisation execution
2. ❌ GitHub push, PR, or merge
3. ❌ Skill/template mutation
4. ❌ Runtime/gateway activation
5. ❌ Service/gateway restart
6. ❌ Credential access
7. ❌ Workflow migration
8. ❌ Smoke-chain activation
9. ❌ SLR-SMOKE-02 revival
10. ❌ Cron/background monitor creation or activation
11. ❌ Omnigent production dependency
12. ❌ Rollback execution
13. ❌ SLR Stage B or later coordination-standard adoption

**All 13 Not Approved items from the PO directive are listed.**
**No execution of any lane. Planning only.**

---

## Kanban-Worker Skill Reference

- SHA256: `4d8c4206...` (kanban-worker skill, used by all 12 worker profiles as overlay)

---

*Generated by elis-supervisor, run 102, task t_28a603b3, 2026-07-22*
*Durable path: ~/.hermes/kanban/boards/elis-slr/artifacts/SLR-FINAL-ROLLOUT-CLOSEOUT-OPTION-E.md*
*This is the canonical planning artifact. Scratch workspace copies are NOT canonical.*