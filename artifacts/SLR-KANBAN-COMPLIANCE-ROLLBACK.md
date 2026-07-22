# SLR-KANBAN-COMPLIANCE-ROLLBACK — Actionable Rollback Evidence

## Document Metadata

| Field | Value |
|-------|-------|
| Document ID | SLR-KANBAN-COMPLIANCE-ROLLBACK |
| Version | 1.0 |
| Date | 2026-07-22 |
| Author | elis-supervisor |
| Parent Task | t_e82216db (ELIS-SLR-HERMES-KANBAN-NATIVE-COMPLIANCE-01) |
| Purpose | Actionable rollback procedures for G1–G5 Kanban-native compliance remediation |
| Governance | Documentation/artifact only — no live profile mutation |

## Changelog

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.1 | 2026-07-22 | elis-supervisor | RB3 fix: corrected coordinator tar restore commands — replaced `cd /home/samurai/.hermes/profiles/` + relative path extraction with `tar xzf ... -C /` to restore to correct absolute path instead of nested `home/samurai/...` tree. |
| 1.0 | 2026-07-22 | elis-supervisor | Initial rollback document (t_e82216db) |

---

## 1. Rollback Scope

This document covers rollback of the G1–G5 compliance remediation applied to the `elis-slr` profile family on 2026-07-22 ~12:10 UTC. It covers:

- **8 edited profile files** across the coordinator and 6 worker profiles
- **6 kanban-worker skill directories** copied into worker profiles (G1)

---

## 2. Edited Files Requiring Rollback Support (8 total)

### Coordinator (2 files)

| # | File | Profile |
|---|------|---------|
| 1 | `SOUL.md` | `elis-slr` (coordinator) |
| 2 | `SKILLS.md` | `elis-slr` (coordinator) |

### Worker AGENTS.md (6 files)

| # | File | Profile |
|---|------|---------|
| 3 | `AGENTS.md` | `elis-slr-harvest-impl-a` |
| 4 | `AGENTS.md` | `elis-slr-harvest-val-b` |
| 5 | `AGENTS.md` | `elis-slr-screen-impl-b` |
| 6 | `AGENTS.md` | `elis-slr-screen-val-a` |
| 7 | `AGENTS.md` | `elis-slr-extract-impl-a` |
| 8 | `AGENTS.md` | `elis-slr-extract-val-b` |

### Kanban-Worker Skill Directories (6, G1)

| # | Directory | Profile |
|---|-----------|---------|
| K1 | `skills/devops/kanban-worker/` | `elis-slr-harvest-impl-a` |
| K2 | `skills/devops/kanban-worker/` | `elis-slr-harvest-val-b` |
| K3 | `skills/devops/kanban-worker/` | `elis-slr-screen-impl-b` |
| K4 | `skills/devops/kanban-worker/` | `elis-slr-screen-val-a` |
| K5 | `skills/devops/kanban-worker/` | `elis-slr-extract-impl-a` |
| K6 | `skills/devops/kanban-worker/` | `elis-slr-extract-val-b` |

---

## 3. Restore Strategy Per File

### Coordinator Files — Option B: Deterministic Restore from Stage 1 Backup

**Source:** Stage 1 backup tar created 2026-07-20 16:33 UTC, before any G1–G5 remediation.

**Backup path:** `/home/samurai/elis/backups/profiles/elis-slr-backup-20260720T163308Z.tar.gz`

**Pre-remediation SHA256 (from backup):**

| File | Pre-Remediation SHA256 | Current SHA256 (post-G1–G5) |
|------|------------------------|------------------------------|
| `elis-slr/SOUL.md` | `1dc47062451bf91a8d835028598b3715a152515d236daf32f1cccd9325c48e8b` | `a6699ac836d8c1b76ed2a73df878134294600a2e1ce6a96ae9f7015f2a3b08ad` |
| `elis-slr/SKILLS.md` | `5668ecaabb24b9444ddc3ee7557c1594e6bd77d56363a729120ca4f4e594481a` | `62b454aa05ecfc9ae72fdfceb6b5967ddb2b1f2b7a94be1583046ca44848f816` |

**Restore commands:**
```bash
tar xzf /home/samurai/elis/backups/profiles/elis-slr-backup-20260720T163308Z.tar.gz \
    -C / \
    home/samurai/.hermes/profiles/elis-slr/SOUL.md \
    home/samurai/.hermes/profiles/elis-slr/SKILLS.md
```

### Worker AGENTS.md Files — Option B: Forward-Remediation by Section Removal

**Context:** No pre-remediation backup copies of worker AGENTS.md exist. The Stage 1 backup tar (2026-07-20) predates worker profile creation (Stages 3–5, 2026-07-20 through 2026-07-22). No per-stage snapshots were preserved (scratch workspaces GC'd).

**Deterministic procedure:** The G1–G5 remediation added exactly two sections to each worker AGENTS.md:
- **G2 — Evidence Scoping section:** Lines 13–21 (9 lines: header, content, Hermes-native identifier list)
- **G4 — channel_directory.json section:** Lines 50–51 (2 lines: header, content)

All 6 worker AGENTS.md files have identical section line ranges. Removing these two sections deterministically reconstructs the pre-remediation state.

**Expected post-rollback SHA256 (deterministically computed):**

| Profile | Expected Post-Rollback SHA256 |
|---------|------------------------------|
| `elis-slr-harvest-impl-a/AGENTS.md` | `004f10d26b8bfe3824063831d931d553fdb5bc39f83c06d8a56f271e2dbcc21e` |
| `elis-slr-harvest-val-b/AGENTS.md` | `c3fa77a758611f82039880232e571816a3201094055cfd7ecd691d9216a9d179` |
| `elis-slr-screen-impl-b/AGENTS.md` | `0e9dbf3c856e4f1226319f80acfb689f71b5fe5318ad2be85bff6e4e71a02263` |
| `elis-slr-screen-val-a/AGENTS.md` | `5b8664b0c5fc8c1ca4f1517698ac2a83c5208a07d297b052c614ac9350a7188e` |
| `elis-slr-extract-impl-a/AGENTS.md` | `5b7f6a36cbdb79297fbd8c2f98be1ecfdeb4456f6a0b2c70f9ffce116492ec96` |
| `elis-slr-extract-val-b/AGENTS.md` | `696fdb06fa0a7db20700c5518bf30c9ad831714434abc838a02c66d222e02d93` |

**Restore command (one-liner for all 6 files):**
```bash
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b \
         elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    sed -i -e '13,21d' -e '41,42d' \
        "/home/samurai/.hermes/profiles/$p/AGENTS.md"
done
```

---

## 4. Honest Recoverability Classification

| # | File | Classification | Basis |
|---|------|---------------|-------|
| 1 | `elis-slr/SOUL.md` | **IS recoverable** — exact pre-remediation content in Stage 1 backup tar | Backup tar created 2026-07-20, before G1–G5 |
| 2 | `elis-slr/SKILLS.md` | **IS recoverable** — exact pre-remediation content in Stage 1 backup tar | Backup tar created 2026-07-20, before G1–G5 |
| 3 | `elis-slr-harvest-impl-a/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Worker profiles created after backup; no stage snapshots preserved |
| 4 | `elis-slr-harvest-val-b/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Same as above |
| 5 | `elis-slr-screen-impl-b/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Same as above |
| 6 | `elis-slr-screen-val-a/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Same as above |
| 7 | `elis-slr-extract-impl-a/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Same as above |
| 8 | `elis-slr-extract-val-b/AGENTS.md` | **NOT recoverable from backup** — no pre-remediation copy exists. Forward-remediation by deterministic section removal is available (see §3). | Same as above |

---

## 5. Kanban-Worker Directory Rollback (G1)

All 6 directories confirmed present as of 2026-07-22.

**Rollback command:**
```bash
for profile in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b \
               elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    rm -rf /home/samurai/.hermes/profiles/$profile/skills/devops/kanban-worker/
done
```

---

## 6. Edited-Files Rollback Commands (Complete)

### Full rollback — all 8 edited files + 6 kanban-worker directories

```bash
# Step 1: Restore coordinator files from Stage 1 backup
tar xzf /home/samurai/elis/backups/profiles/elis-slr-backup-20260720T163308Z.tar.gz \
    -C / \
    home/samurai/.hermes/profiles/elis-slr/SOUL.md \
    home/samurai/.hermes/profiles/elis-slr/SKILLS.md

# Step 2: Forward-remediate worker AGENTS.md (remove G2 Evidence Scoping + G4 channel_directory.json)
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b \
         elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    sed -i -e '13,21d' -e '41,42d' \
        "/home/samurai/.hermes/profiles/$p/AGENTS.md"
done

# Step 3: Remove kanban-worker skill directories (G1)
for profile in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b \
               elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    rm -rf /home/samurai/.hermes/profiles/$profile/skills/devops/kanban-worker/
done
```

---

## 7. Verification Steps After Rollback

### Verify coordinator SHA256 matches pre-remediation state

```bash
echo "1dc47062451bf91a8d835028598b3715a152515d236daf32f1cccd9325c48e8b  /home/samurai/.hermes/profiles/elis-slr/SOUL.md" | sha256sum -c
echo "5668ecaabb24b9444ddc3ee7557c1594e6bd77d56363a729120ca4f4e594481a  /home/samurai/.hermes/profiles/elis-slr/SKILLS.md" | sha256sum -c
```

### Verify worker AGENTS.md SHA256 matches expected post-rollback state

```bash
echo "004f10d26b8bfe3824063831d931d553fdb5bc39f83c06d8a56f271e2dbcc21e  /home/samurai/.hermes/profiles/elis-slr-harvest-impl-a/AGENTS.md" | sha256sum -c
echo "c3fa77a758611f82039880232e571816a3201094055cfd7ecd691d9216a9d179  /home/samurai/.hermes/profiles/elis-slr-harvest-val-b/AGENTS.md" | sha256sum -c
echo "0e9dbf3c856e4f1226319f80acfb689f71b5fe5318ad2be85bff6e4e71a02263  /home/samurai/.hermes/profiles/elis-slr-screen-impl-b/AGENTS.md" | sha256sum -c
echo "5b8664b0c5fc8c1ca4f1517698ac2a83c5208a07d297b052c614ac9350a7188e  /home/samurai/.hermes/profiles/elis-slr-screen-val-a/AGENTS.md" | sha256sum -c
echo "5b7f6a36cbdb79297fbd8c2f98be1ecfdeb4456f6a0b2c70f9ffce116492ec96  /home/samurai/.hermes/profiles/elis-slr-extract-impl-a/AGENTS.md" | sha256sum -c
echo "696fdb06fa0a7db20700c5518bf30c9ad831714434abc838a02c66d222e02d93  /home/samurai/.hermes/profiles/elis-slr-extract-val-b/AGENTS.md" | sha256sum -c
```

### Verify kanban-worker directories removed

```bash
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b \
         elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    test -d "/home/samurai/.hermes/profiles/$p/skills/devops/kanban-worker/" \
        && echo "STILL EXISTS: $p" \
        || echo "REMOVED: $p"
done
```

### Verify G1–G5 compliance state reverted

- G1 (kanban-worker copies): directories absent
- G2 (Evidence Scoping): section absent from worker AGENTS.md
- G3 (coordinator idempotency_key + kanban-orchestrator): reverted by SOUL.md/SKILLS.md restore
- G4 (channel_directory.json): section absent from worker AGENTS.md
- G5 (role clarity): reverted by SOUL.md/SKILLS.md restore

```bash
# Quick checks
grep -c 'Evidence Scoping' /home/samurai/.hermes/profiles/elis-slr-screen-impl-b/AGENTS.md  # expected: 0
grep -c 'channel_directory.json' /home/samurai/.hermes/profiles/elis-slr-screen-impl-b/AGENTS.md  # expected: 0
grep -c 'idempotency_key' /home/samurai/.hermes/profiles/elis-slr/SOUL.md  # expected: 0
grep -c 'kanban-orchestrator' /home/samurai/.hermes/profiles/elis-slr/SKILLS.md  # expected: 0
```

---

## 8. Confirmation — No Live Profile Mutation

**Confirmed.** This task (t_e82216db) created documentation only. No live profile files were changed. The 8 edited files remain in their post-G1–G5 state until PO-initiated rollback is executed.

- No `AGENTS.md`, `SOUL.md`, `SKILLS.md`, `config.yaml`, `channel_directory.json`, or kanban-worker `SKILL.md` files were written to.
- No `write_file`, `patch`, or `terminal` commands that mutate profile directories were executed.

---

## 9. Confirmation — No Credential Access

**Confirmed.** No `.env` files or credential metadata were inspected, copied, hashed, compared, moved, or exposed. The backup tar listing was inspected for file names only — no file contents containing secrets were read. SHA256 computation used only profile identity files (AGENTS.md, SOUL.md, SKILLS.md), which contain no secrets.

---

## 10. Confirmation — No Unauthorized Actions

**Confirmed.** None of the following were performed:
- No service/gateway restart
- No GitHub operations
- No smoke-chain activation
- No cron or background monitor creation
- No Omnigent dependency introduced
- No Stage 6 execution
- No agent dispatch
- No kanban board mutation beyond task lifecycle calls

---

## Appendix A: Current SHA256 Post-G1–G5 (for rollback verification)

| File | Current SHA256 (post-G1–G5) | Profile |
|------|-----------------------------|---------|
| SOUL.md | `a6699ac836d8c1b76ed2a73df878134294600a2e1ce6a96ae9f7015f2a3b08ad` | elis-slr |
| SKILLS.md | `62b454aa05ecfc9ae72fdfceb6b5967ddb2b1f2b7a94be1583046ca44848f816` | elis-slr |
| AGENTS.md | `2b2eb2e2dcb1c9999f50de22e5f60c5f59acc64ea4580db666d0c22ef3d24c12` | elis-slr-harvest-impl-a |
| AGENTS.md | `56e8d24bce384940c7edb88f7b2503f9b6eb19054d7ce44f1413f45762ed1a4d` | elis-slr-harvest-val-b |
| AGENTS.md | `40e824f65cf2a6be29a3708723449bd84acee84cb66680e22d37d8f1b9897ccc` | elis-slr-screen-impl-b |
| AGENTS.md | `51e7a4452caf66c4804283a9f642e8805e9ecb5565722a6c8290d793b2bf8e30` | elis-slr-screen-val-a |
| AGENTS.md | `bfaea1599581306650aa2c0d8ee530478454a9db25af4fb1d39867daedabba36` | elis-slr-extract-impl-a |
| AGENTS.md | `c72c96e8e54f48a4237769d9ea3f1b005671753268e716f062c35f1b8e345859` | elis-slr-extract-val-b |

## Appendix B: Stage 1 Backup Tar Reference

- **Path:** `/home/samurai/elis/backups/profiles/elis-slr-backup-20260720T163308Z.tar.gz`
- **Size:** 20,381,012 bytes (~19.4 MB)
- **Created:** 2026-07-20 16:33 UTC
- **Contents:** Full `elis-slr` coordinator profile (SOUL.md, SKILLS.md, AGENTS.md, config.yaml, skills/, cache/)
- **Worker profiles:** NOT included (workers created in Stages 3–5 after this backup)
