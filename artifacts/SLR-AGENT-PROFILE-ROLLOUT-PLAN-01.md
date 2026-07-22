# SLR Agent Profile Rollout Plan — SLR-AGENT-PROFILE-ROLLOUT-PLAN-01

## Document Metadata

| Field | Value |
|-------|-------|
| Document ID | SLR-AGENT-PROFILE-ROLLOUT-PLAN-01 |
| Version | 1.0 |
| Date | 2026-07-20 |
| Author | elis-supervisor |
| Parent Task | t_9e5f511e (SLR-AGENT-PROFILE-ROLLOUT-PLANNING-GATE-01) |
| Status | NOT EXECUTED — planning artifact only |
| Republished | 2026-07-20 via remediation task t_294bc965 (original scratch workspace GC'd) |

---

## Purpose

Staged rollout plan for creating 10 domain-scoped SLR worker agent profiles under the `elis-slr` profile family, plus 1 coordinator profile edit. The plan covers 11 profiles total across 8 stages, with per-stage backup/rollback, stop conditions, and a domain-scoped smoke test design.

---

## Staged Sequence

### Stage 0: Pre-Flight Checks

8 read-only checks before any mutation:

| Check | Description |
|-------|-------------|
| P0.1 | Verify `hermes` CLI installed and in PATH |
| P0.2 | Verify `/home/samurai/.hermes/` Hermes home exists |
| P0.3 | Verify Discord channel `#elis-slr-reports` is reachable (200) |
| P0.4 | Verify no concurrent PE active (check process table for other rollout) |
| P0.5 | Verify `/home/samurai/elis/backups/profiles/` backup target exists (or create) |
| P0.6 | Verify `elis-slr` coordinator profile exists and is operational |
| P0.7 | Verify model provider reachable (OpenRouter health check) |
| P0.8 | Verify sufficient disk space (>500MB free in $HOME) |

### Stage 1: Coordinator Profile Backup

- Action: `tar czf /home/samurai/elis/backups/profiles/elis-slr-backup-$(date +%Y%m%dT%H%M%SZ).tar.gz -C /home/samurai/.hermes/profiles/ elis-slr/`
- Stop condition (S9): Backup creation fails
- Rollback: N/A (no mutation yet)

### Stage 2: Coordinator Edits

- Profile: `elis-slr`
- Files edited (2):
  - `SOUL.md` line 51: path fix
  - `SKILLS.md` lines 113-114: path fix
- Stop condition (S10): Coordinator edit fails
- Stop condition (S11): Coordinator non-responsive after edit
- Rollback: Restore coordinator from Stage 1 backup

### Stage 3: Harvest Domain

- Profiles created (2): `elis-slr-harvest-impl-a`, `elis-slr-harvest-val-b`
- Files created (10): AGENTS.md, SOUL.md, SKILLS.md, config.yaml, channel_directory.json per profile
- Stop condition (S12): Profile creation fails (namespace conflict, etc.)
- Rollback: Per-domain `rm -rf` both profile dirs

### Stage 4: Screen Domain

- Profiles created (2): `elis-slr-screen-impl-b`, `elis-slr-screen-val-a`
- Files created (10): AGENTS.md, SOUL.md, SKILLS.md, config.yaml, channel_directory.json per profile
- Rollback: Per-domain `rm -rf` both profile dirs

### Stage 5: Extract Domain

- Profiles created (2): `elis-slr-extract-impl-a`, `elis-slr-extract-val-b`
- Files created (10): AGENTS.md, SOUL.md, SKILLS.md, config.yaml, channel_directory.json per profile
- Rollback: Per-domain `rm -rf` both profile dirs

### Stage 6: Synthesis Domain

- Profiles created (2): `elis-slr-synth-impl-b`, `elis-slr-synth-val-a`
- Files created (10): AGENTS.md, SOUL.md, SKILLS.md, config.yaml, channel_directory.json per profile
- Rollback: Per-domain `rm -rf` both profile dirs

### Stage 7: PRISMA Domain

- Profiles created (2): `elis-slr-prisma-impl-b`, `elis-slr-prisma-val-a`
- Files created (10): AGENTS.md, SOUL.md, SKILLS.md, config.yaml, channel_directory.json per profile
- Rollback: Per-domain `rm -rf` both profile dirs

### Stage 8: Full Integration Verification

- Verify all 11 profiles exist and are loadable by Hermes
- Verify coordinator can discover all 10 workers
- Verify channel directory entries match actual profiles
- Stop condition (S14): Integration verification fails
- Stop condition (S15): PO stop directive

---

## Affected Profiles

| # | Profile | Role | Stage |
|---|---------|------|-------|
| 1 | `elis-slr` | Coordinator (edited) | 2 |
| 2 | `elis-slr-harvest-impl-a` | Harvest Implementer A | 3 |
| 3 | `elis-slr-harvest-val-b` | Harvest Validator B | 3 |
| 4 | `elis-slr-screen-impl-b` | Screen Implementer B | 4 |
| 5 | `elis-slr-screen-val-a` | Screen Validator A | 4 |
| 6 | `elis-slr-extract-impl-a` | Extract Implementer A | 5 |
| 7 | `elis-slr-extract-val-b` | Extract Validator B | 5 |
| 8 | `elis-slr-synth-impl-b` | Synthesis Implementer B | 6 |
| 9 | `elis-slr-synth-val-a` | Synthesis Validator A | 6 |
| 10 | `elis-slr-prisma-impl-b` | PRISMA Implementer B | 7 |
| 11 | `elis-slr-prisma-val-a` | PRISMA Validator A | 7 |

---

## Affected Files

**Total: 52 files**

### Edited (2 files)

| File | Profile | Location |
|------|---------|----------|
| SOUL.md | elis-slr | Line 51 (path fix) |
| SKILLS.md | elis-slr | Lines 113-114 (path fix) |

### Created (50 files across 10 worker profiles)

Each of the 10 worker profiles receives 5 files:

| File | Purpose |
|------|---------|
| AGENTS.md | Agent identity and behavior specification |
| SOUL.md | Agent soul/identity core |
| SKILLS.md | Skill manifest |
| config.yaml | Hermes profile configuration |
| channel_directory.json | Channel/directory routing |

---

## Backup Plan

### Stage 1: Full Coordinator Backup
- `tar czf /home/samurai/elis/backups/profiles/elis-slr-backup-<timestamp>.tar.gz -C /home/samurai/.hermes/profiles/ elis-slr/`

### Stages 3-7: Per-Domain Snapshots
- Each domain stage creates its own snapshot of the two new profiles before proceeding

### Full Rollback
- Restore coordinator from Stage 1 backup
- `rm -rf` all 10 worker profile directories
- Estimated time: ~10 minutes

### Partial Rollback
- Per-domain `rm -rf` of the two profiles in the failing stage
- Estimated time: ~1 minute

---

## Validation Plan

### Self-Validation (during each stage)
- Coordinator functional checks: `hermes profile show elis-slr` succeeds
- File existence checks: all expected files present
- `grep` for stale paths in created profiles
- Channel directory consistency checks

### Independent Validation
- Advisor performs final independent validation
- Author (elis-supervisor) must NOT self-validate final rollout
- Validation criteria: all profiles loadable, coordinator discovers workers, no stale paths

---

## Smoke Test Plan

Designed but NOT activated. Smoke tests are domain-scoped and produce file output evidence even if the Discord channel is unreachable.

| Smoke ID | Domain | Scope |
|----------|--------|-------|
| SMOKE-10 | Harvest | Harvest domain agent round-trip |
| SMOKE-11 | Screen | Screen domain agent round-trip |
| SMOKE-12 | Extract | Extract domain agent round-trip |
| SMOKE-13 | Synthesis | Synthesis domain agent round-trip |
| SMOKE-14 | PRISMA | PRISMA domain agent round-trip |
| SMOKE-15 | End-to-End | Full cross-domain integration |

### Smoke Design Principles
- Evidence-first: file output + SHA256 for each smoke
- Domain-scoped: each smoke tests only its domain pair
- Channel check P0.3 prevents activation if `#elis-slr-reports` returns 403
- No reference to old task IDs (prevents SLR-SMOKE-02 revival)
- Evidence-first design decouples channel post from task success

---

## Stop Conditions

| Stop ID | Condition | Stage |
|---------|-----------|-------|
| S1 | SHA256 mismatch on any critical file | Any |
| S2 | Coordinator not operational | Any post-Stage 2 |
| S3 | Discord channel unreachable (403) | Stage 0 (P0.3) |
| S4 | Namespace conflict (profile already exists) | Stages 3-7 |
| S5 | Model provider unavailable | Stage 0 (P0.7) |
| S6 | Hermes CLI missing | Stage 0 (P0.1) |
| S7 | Bot token invalid | Stage 0 |
| S8 | Concurrent PE active | Stage 0 (P0.4) |
| S9 | Backup creation fails | Stage 1 |
| S10 | Coordinator edit fails | Stage 2 |
| S11 | Coordinator non-responsive after edit | Stage 2 |
| S12 | Profile creation fails | Stages 3-7 |
| S13 | kanban-worker nested layout defect detected | Stages 3-7 |
| S14 | Integration verification fails | Stage 8 |
| S15 | PO stop directive | Any |

---

## Coordinator-Worker Separation

- **Stage 2**: Coordinator edits only (2 files, path fix). Critical path.
- **Stages 3-7**: Worker creations, domain-batched.
- **Dependency**: No workers created until coordinator edits succeed.
- **Critical path**: Coordinator is the single point of failure — if Stage 2 fails, no workers are created.

---

## Non-Execution Confirmation

**Yes.** This artifact is a planning document only. No profile rollout has been executed. All actions described are planned, not performed.

---

## SLR-SMOKE-02 Revival Avoidance

| Measure | Mechanism |
|---------|-----------|
| Pre-flight channel check | P0.3 blocks rollout if `#elis-slr-reports` returns 403 |
| Domain-scoped smokes | Each smoke produces file evidence even if channel fails |
| No old task ID references | Smoke design contains zero references to prior SLR task IDs |
| Evidence-first design | Channel post is decoupled from task success determination |

---

## Remediation Record

This artifact was republished on 2026-07-20 via remediation task `t_294bc965` after the original scratch workspace (`t_9e5f511e`) was garbage-collected. The Advisor (via task `t_e949afbc`) could not validate the original at the expected path:

> `/home/samurai/.hermes/kanban/boards/elis-slr/workspaces/t_9e5f511e/SLR-AGENT-PROFILE-ROLLOUT-PLAN-01.md`

The original reported SHA256 was: `75e53e8ae19af05cbe98c065ab472a84b9e6dd6695c40abca7fa51c07a839467`

Content was reconstructed from the parent task (t_9e5f511e) handoff metadata and completion evidence. The substance is preserved; only the artifact path is now durable.

---

## Advisor FAIL Findings (verbatim, from t_e949afbc)

> Advisor validation evidence (read-only):
> Expected planning artifact from parent metadata:
> `/home/samurai/.hermes/kanban/boards/elis-slr/workspaces/t_9e5f511e/SLR-AGENT-PROFILE-ROLLOUT-PLAN-01.md`
> Expected parent-reported SHA256: `75e53e8ae19af05cbe98c065ab472a84b9e6dd6695c40abca7fa51c07a839467`
> 
> Read-only checks performed from workspace `/home/samurai/.hermes/kanban/boards/elis-slr/workspaces/t_e949afbc`:
> - `test -f .../SLR-AGENT-PROFILE-ROLLOUT-PLAN-01.md && sha256sum ... && wc -l ...` returned exit code 1 before hash/line output.
> - `/home/samurai/.hermes/kanban/boards/elis-slr/workspaces/t_9e5f511e` is missing.
> - Search under `/home/samurai/.hermes/kanban/boards/elis-slr` found no `*ROLLOUT*PLAN*.md` files.
> - Durable artifacts directory exists, but contains no rollout plan artifact.
> 
> Conclusion: FAIL. Criterion 1 fails because the planning artifact is not currently present at a durable/readable path, so criteria 2–11 cannot be independently source-verified from the required artifact.