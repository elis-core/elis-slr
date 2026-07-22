# Gate B Staging Execution Packet — G2 Local Population and Staged-Content Review

**Status:** Draft — Awaiting PO Gate B Execution Approval Before Any Copy  
**Date:** 2026-06-23  
**Migration Plan:** `/home/samurai/.hermes/profiles/_shared/architecture/ELIS-MIGRATION-PLAN-CORE-SLR.md`  
**Gate A:** PO approved — migration plan  
**Gate B pre-flight:** PO approved — manifest validation (43/43 PASS)  
**Gate B execution (G2):** ELIS Supervisor — filesystem staging only, no GitHub operations  
**Next gate:** Gate C / G4 — push to `elis-slr` (requires separate PO approval + Advisor review)

---

## 1. Staging Path

**Exact staging root:**

```
/home/samurai/elis-staging/elis-slr-gate-b/
```

This path does not currently exist. It will be created by the Gate B execution script. It is outside any git repository, Hermes profile directory, OpenClaw workspace, or agent worktree. It is a temporary local staging area that will be removed after Gate B review or on rollback.

**Rationale:** The migration plan does not define an explicit staging path. This proposal uses a clearly-named temporary directory under the home directory, outside any existing project structure.

---

## 2. Copy Commands

All 42 source files are read from the legacy monorepo at `/home/samurai/openclaw/workspace-prog-impl/repo/` and copied into the staging directory. The legacy repo is read-only — never modified.

The charter copy (C1) is read from its absolute `_shared` path.

M1 (`MIGRATION.md`) is generated in-place — no source file.

**Execution script (single command, idempotent):**

```bash
#!/bin/bash
set -euo pipefail

STAGING="/home/samurai/elis-staging/elis-slr-gate-b"
SOURCE="/home/samurai/openclaw/workspace-prog-impl/repo"
CHARTER="/home/samurai/.hermes/profiles/_shared/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md"

# Remove any previous staging (idempotent re-run safety)
rm -rf "$STAGING"
mkdir -p "$STAGING"/{docs/{_active,_archive/2026-02,slr,openclaw,testing/slr-artifacts/{passing,failing},reviews/archive,architecture},}

# --- 42 file copies ---
# Protocol (§1.1) — 6 files
cp "$SOURCE/docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf" "$STAGING/docs/_active/"
cp "$SOURCE/docs/_active/ELIS_2025_SLR_REPO_SPEC.md"                                    "$STAGING/docs/_active/"
cp "$SOURCE/docs/_active/ELIS_2025_SLR_README_TEMPLATE.md"                              "$STAGING/docs/_active/"
cp "$SOURCE/docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md"                 "$STAGING/docs/_active/"
cp "$SOURCE/docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md"                       "$STAGING/docs/_active/"
cp "$SOURCE/docs/_archive/2026-02/ELIS_2025_SLR_Protocol_v1.8.pdf"                      "$STAGING/docs/_archive/2026-02/"

# Domain specs (§1.2) — 9 files
cp "$SOURCE/docs/slr/SLR_DOMAIN_SPEC.md"                 "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/HYBRID_SLR_VALIDATION.md"           "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/HARVEST_WORKFLOW_CONTRACT.md"       "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/SCREENING_LOCAL_CONTRACT.md"        "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/SCREENING_GOVERNANCE.md"            "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/EXTRACTION_OFF_HOST_CONTRACT.md"    "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/SYNTHESIS_OFF_HOST_CONTRACT.md"     "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/WORKLOAD_PLACEMENT_POLICY.md"       "$STAGING/docs/slr/"
cp "$SOURCE/docs/slr/LOCAL_SUPPORT_ANALYSIS.md"          "$STAGING/docs/slr/"

# Provisioning (§1.3) — 2 files
cp "$SOURCE/docs/openclaw/SLR_PROJECT_STORE_LAYOUT.md"               "$STAGING/docs/openclaw/"
cp "$SOURCE/docs/openclaw/SLR_PHASE_WORKSPACE_PROVISIONING_2026-03-25.md" "$STAGING/docs/openclaw/"

# Testing (§1.4) — 4 files
cp "$SOURCE/docs/testing/E2E_TEST_SLR.md"                   "$STAGING/docs/testing/"
cp "$SOURCE/docs/testing/SLR_QUALITY_CI.md"                 "$STAGING/docs/testing/"
cp "$SOURCE/docs/testing/slr-artifacts/passing/good_artifact.json" "$STAGING/docs/testing/slr-artifacts/passing/"
cp "$SOURCE/docs/testing/slr-artifacts/failing/bad_artifact.json" "$STAGING/docs/testing/slr-artifacts/failing/"

# Reviews (§1.5) — 15 files
cp "$SOURCE/docs/reviews/archive/REVIEW_PE-INFRA-SLR-02.md" "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_INFRA_SLR_04.md" "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_INFRA_SLR_07.md" "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_INFRA_SLR_08.md" "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_01.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_02.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_03.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_07.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_08.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_09.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_10.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_11.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_12.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_13.md"       "$STAGING/docs/reviews/archive/"
cp "$SOURCE/docs/reviews/archive/REVIEW_PE_SLR_15.md"       "$STAGING/docs/reviews/archive/"

# Architecture (§1.6) — 5 files
cp "$SOURCE/docs/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1.4.md" "$STAGING/docs/"
cp "$SOURCE/ELIS_SLR_AI_Platform_Conceptual_Architecture_v1_9.md"      "$STAGING/"
cp "$SOURCE/ELIS_MultiAgent_Implementation_Plan_v1_8_3.md"             "$STAGING/"
cp "$SOURCE/ELIS_MultiAgent_Implementation_Plan_v1_9.md"               "$STAGING/"
cp "$SOURCE/ELIS_MultiAgent_Implementation_Plan_v2_0.md"               "$STAGING/"

# Charter copy (§1.7) — 1 file
cp "$CHARTER" "$STAGING/docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md"

echo "Gate B G2 staging: 42 files copied to $STAGING"

# --- M1: Write MIGRATION.md ---
cat > "$STAGING/MIGRATION.md" << 'MIGEOF'
# ELIS SLR — Migration Provenance

**Repository:** `https://github.com/elis-core/elis-slr`  
**Migration date:** 2026-06-23  
**Migration plan:** `ELIS-MIGRATION-PLAN-CORE-SLR.md` (Gate A approved)  
**Source:** `rochasamurai/ELIS-Multi-AI-Agent-Platform` (legacy monorepo, read-only)  

## Scope

This repository contains the SLR-domain artefacts migrated from the ELIS monorepo.
42 files were copied from the legacy monorepo. 1 file (`MIGRATION.md`) was generated
at commit time. Total: 43 files in the initial commit.

## Artefact Categories

| Category | Count |
|---|---|
| Protocol documents | 6 |
| Domain specifications | 9 |
| Provisioning documents | 2 |
| Testing documentation | 4 |
| Review archive | 15 |
| Architecture and planning | 5 |
| Charter reference copy | 1 |
| Migration metadata | 1 |
| **Total** | **43** |

## History

This repository starts with a clean initial commit. Full git history is preserved in
the legacy monorepo at `rochasamurai/ELIS-Multi-AI-Agent-Platform` and in the ELIS Core
repository at `https://github.com/elis-core/elis-core`.

## Governance

This repository is governed by the ELIS Core / ELIS SLR Architecture Charter and Routing
document (`docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md`).

Canonical authority for the charter remains with the `_shared` architecture directory
on elis-server. The copy in this repository is for reference and discoverability only.

## Migration Plan Reference

`/home/samurai/.hermes/profiles/_shared/architecture/ELIS-MIGRATION-PLAN-CORE-SLR.md`
MIGEOF

echo "Gate B G2 staging: 43 files total in $STAGING (42 copied + 1 generated)"
```

**Copy mode:** `cp` (not `mv`, not `ln`). Source files are untouched. Destination is a fresh directory.

**Total operations:** 42 `cp` commands + 1 `mkdir -p` tree.

---

## 3. Generated MIGRATION.md Content

After the 42 file copies, the following file is written to `$STAGING/MIGRATION.md`:

```markdown
# ELIS SLR — Migration Provenance

**Repository:** `https://github.com/elis-core/elis-slr`  
**Migration date:** 2026-06-23  
**Migration plan:** `ELIS-MIGRATION-PLAN-CORE-SLR.md` (Gate A approved)  
**Source:** `rochasamurai/ELIS-Multi-AI-Agent-Platform` (legacy monorepo, read-only)  

## Scope

This repository contains the SLR-domain artefacts migrated from the ELIS monorepo.
42 files were copied from the legacy monorepo. 1 file (`MIGRATION.md`) was generated
at commit time. Total: 43 files in the initial commit.

## Artefact Categories

| Category | Count |
|---|---|
| Protocol documents | 6 |
| Domain specifications | 9 |
| Provisioning documents | 2 |
| Testing documentation | 4 |
| Review archive | 15 |
| Architecture and planning | 5 |
| Charter reference copy | 1 |
| Migration metadata | 1 |
| **Total** | **43** |

## History

This repository starts with a clean initial commit. Full git history is preserved in
the legacy monorepo at `rochasamurai/ELIS-Multi-AI-Agent-Platform` and in the ELIS Core
repository at `https://github.com/elis-core/elis-core`.

## Governance

This repository is governed by the ELIS Core / ELIS SLR Architecture Charter and Routing
document (`docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md`).

Canonical authority for the charter remains with the `_shared` architecture directory
on elis-server. The copy in this repository is for reference and discoverability only.

## Migration Plan Reference

`/home/samurai/.hermes/profiles/_shared/architecture/ELIS-MIGRATION-PLAN-CORE-SLR.md`
```

---

## 4. 43-Row Staged-Content Verification

After the copy script runs, ELIS Supervisor must verify:

- 43 files exist in the staging directory (42 copied + 1 generated `MIGRATION.md`)
- Each file's size matches the Gate B evidence table
- Directory structure matches the destination paths in the §11 manifest
- No unexpected files are present in staging

Verification command:

```bash
find "$STAGING" -type f | wc -l   # Expected: 43
```

A 43-row pass/fail table will be generated, comparing staged file sizes to the Gate B evidence baseline.

---

## 5. Staged Secret/Sensitive-Data Scan

After population, ELIS Supervisor must re-run the secret scan on all 40 copied text files plus the generated `MIGRATION.md` in the staging directory (same 12 patterns as Gate B). 2 PDFs (P1, P6) are skipped as binary. The expected result is identical to Gate B: 0 secrets detected, 1 known false positive (A5 — `OPENAI_API_KEY` as documentation reference).

---

## 6. Proof That `elis-core` is Not Mutated

**Proof mechanism:** `git status` on the legacy monorepo clone AND the canonical repo before and after staging.

```bash
# Before staging
echo "=== /opt/elis/repo ==="
git -C /opt/elis/repo status -sb
git -C /opt/elis/repo diff --stat

echo "=== workspace-prog-impl/repo (legacy source) ==="
git -C /home/samurai/openclaw/workspace-prog-impl/repo status -sb
git -C /home/samurai/openclaw/workspace-prog-impl/repo diff --stat

# After staging (must be identical — no changes to either repo)
echo "=== /opt/elis/repo ==="
git -C /opt/elis/repo status -sb
git -C /opt/elis/repo diff --stat

echo "=== workspace-prog-impl/repo (legacy source) ==="
git -C /home/samurai/openclaw/workspace-prog-impl/repo status -sb
git -C /home/samurai/openclaw/workspace-prog-impl/repo diff --stat
```

The legacy monorepo at `workspace-prog-impl/repo/` is read via `cp` only — no writes.

---

## 7. Proof That No GitHub Operation or Remote Change is Performed

**Evidence:** Before-and-after verification of the staging directory's absence of any `.git` directory.

```bash
# After staging population:
test -d "$STAGING/.git" && echo "FAIL: .git present" || echo "PASS: no .git directory"
```

The staging directory is a plain filesystem directory. No `git init`, `git clone`, `git remote`, or any GitHub CLI operation is performed. No network access is required.

Additionally, `git remote -v` for all known local clones is checked before and after to confirm no remote changes:

```bash
for repo in /opt/elis/repo /home/samurai/openclaw/workspace-prog-impl/repo /home/samurai/ELIS-SLR-Agent; do
    echo "=== $repo ==="
    git -C "$repo" remote -v
done
```

---

## 8. Rollback/Removal

**Rollback command (single line, safe):**

```bash
rm -rf /home/samurai/elis-staging/elis-slr-gate-b/
```

This removes the entire staging directory. No other filesystem state is affected. The source files are never modified. No git state is changed.

**Rollback verification:**

```bash
test -d /home/samurai/elis-staging/elis-slr-gate-b/ && echo "FAIL: staging still exists" || echo "PASS: staging removed"
```

---

## 9. Evidence Package

After Gate B execution, ELIS Supervisor will produce a `ELIS-GATE-B-STAGING-EVIDENCE.md` file at `/home/samurai/.hermes/profiles/_shared/architecture/` containing:

1. Copy script output (summary lines) plus 43-row staged-content verification table confirming all expected files are present with matching sizes
2. `MIGRATION.md` content verification
3. 43-row staged-content pass/fail table (file count, size match)
4. Secret scan results (0 secrets)
5. `elis-core` untouched proof (before/after `git status`)
6. No-GitHub proof (no `.git` in staging, remotes unchanged)
7. Rollback command verification
8. Confirmation that no GitHub, remote, profile, board, runtime, gateway, `.env`, or cutover action was performed

---

## 10. Gate B Execution Approval

| What | When |
|---|---|
| PO approves Gate B execution (G2) | Before any staging filesystem action, including `rm -rf`, `mkdir`, `cp`, or writing `MIGRATION.md` |

Gate B execution is filesystem-only. No GitHub operations. All actions are local and reversible. The staging directory is temporary — it will be removed after Gate B review or on rollback.

After Gate B evidence is delivered and Advisor-reviewed, the next gate (Gate C / G4) would involve `git init`, `git remote add`, `git commit`, and `git push` to `elis-slr` — each requiring separate PO approval.