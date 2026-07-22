# SLR-STAGE-6-SYNTHESIS-ROLLBACK.md

## Purpose

Rollback procedure for Stage 6 Synthesis worker profiles only. This artifact closes the rollback actionability gap identified by Advisor validation `t_4bfe3595` (FAIL).

This Stage 6 rollback is independent of the Kanban-native compliance rollback at `SLR-KANBAN-COMPLIANCE-ROLLBACK.md`.

## Scope

**Stage 6 Synthesis profiles only.** This procedure removes the two long-name Synthesis worker profiles created during SLR-AGENT-PROFILE-ROLLOUT-STAGE-6. It does NOT affect Harvest, Screen, Extract, coordinator, legacy short-name profiles, or any other SLR infrastructure.

## Rollback Target Profiles

| Profile | Path |
|---|---|
| Synthesis Implementer B | `/home/samurai/.hermes/profiles/elis-slr-synth-impl-b` |
| Synthesis Validator A | `/home/samurai/.hermes/profiles/elis-slr-synth-val-a` |

These are newly created profiles — no tar extraction or restoration from backup is needed. Simple removal is sufficient.

## Relationship to Compliance Rollback Artifact

- **Compliance rollback artifact:** `SLR-KANBAN-COMPLIANCE-ROLLBACK.md`
  - SHA256: `9e66e252f07cf1a05a416993768ba6b6b3ca415054137fae3cac67190000b0e9`
  - Covers: tar-based restore of 8 edited files in 7 profiles (kanban-worker skill copies, SKILLS.md, _shared edits)
- **This artifact:** covers only the two Stage 6 Synthesis profile directories
- The two artifacts are independent — neither amends nor depends on the other

## Rollback Commands

Copy/paste safe. Run on `elis-server` as the user who owns the profile directories.

```bash
# === STAGE 6 SYNTHESIS PROFILE ROLLBACK ===
# Target: elis-slr-synth-impl-b + elis-slr-synth-val-a only
# Artifact: SLR-STAGE-6-SYNTHESIS-ROLLBACK.md

# Step 1: Verify target directories exist before removal
echo "=== Pre-removal verification ==="
test -d /home/samurai/.hermes/profiles/elis-slr-synth-impl-b && echo "PRE: EXISTS  elis-slr-synth-impl-b" || echo "PRE: ABSENT  elis-slr-synth-impl-b"
test -d /home/samurai/.hermes/profiles/elis-slr-synth-val-a && echo "PRE: EXISTS  elis-slr-synth-val-a" || echo "PRE: ABSENT  elis-slr-synth-val-a"

# Step 2: Remove only the two Stage 6 Synthesis profile directories
echo "=== Removing Stage 6 Synthesis profiles ==="
rm -rf /home/samurai/.hermes/profiles/elis-slr-synth-impl-b
rm -rf /home/samurai/.hermes/profiles/elis-slr-synth-val-a

# Step 3: Verify removal
echo "=== Post-removal verification ==="
test -d /home/samurai/.hermes/profiles/elis-slr-synth-impl-b && echo "POST: FAIL — elis-slr-synth-impl-b still exists" || echo "POST: OK — elis-slr-synth-impl-b removed"
test -d /home/samurai/.hermes/profiles/elis-slr-synth-val-a && echo "POST: FAIL — elis-slr-synth-val-a still exists" || echo "POST: OK — elis-slr-synth-val-a removed"
```

## Cross-Profile Integrity Verification

After executing the removal, run these integrity checks. The rollback is only complete when ALL checks pass.

```bash
# === CROSS-PROFILE INTEGRITY VERIFICATION ===

echo "=== 1. Confirm Stage 6 Synthesis profiles removed ==="
test -d /home/samurai/.hermes/profiles/elis-slr-synth-impl-b && echo "FAIL: elis-slr-synth-impl-b still present" || echo "PASS"
test -d /home/samurai/.hermes/profiles/elis-slr-synth-val-a && echo "FAIL: elis-slr-synth-val-a still present" || echo "PASS"

echo "=== 2. Confirm Harvest profiles unchanged ==="
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b; do
    test -d "/home/samurai/.hermes/profiles/$p" && echo "PASS: $p present" || echo "FAIL: $p missing"
done

echo "=== 3. Confirm Screen profiles unchanged ==="
for p in elis-slr-screen-impl-b elis-slr-screen-val-a; do
    test -d "/home/samurai/.hermes/profiles/$p" && echo "PASS: $p present" || echo "FAIL: $p missing"
done

echo "=== 4. Confirm Extract profiles unchanged ==="
for p in elis-slr-extract-impl-a elis-slr-extract-val-b; do
    test -d "/home/samurai/.hermes/profiles/$p" && echo "PASS: $p present" || echo "FAIL: $p missing"
done

echo "=== 5. Confirm coordinator files unchanged ==="
test -f /home/samurai/.hermes/profiles/elis-slr/SOUL.md && echo "PASS: SOUL.md present" || echo "FAIL: SOUL.md missing"
test -f /home/samurai/.hermes/profiles/elis-slr/SKILLS.md && echo "PASS: SKILLS.md present" || echo "FAIL: SKILLS.md missing"

echo "=== 6. Confirm legacy short-name Synthesis profiles untouched ==="
test -d /home/samurai/.hermes/profiles/synth-impl-b && echo "PASS: synth-impl-b present (untouched)" || echo "FAIL: synth-impl-b missing"
test -d /home/samurai/.hermes/profiles/synth-val-a && echo "PASS: synth-val-a present (untouched)" || echo "FAIL: synth-val-a missing"

echo "=== 7. Confirm kanban-worker skill copies in remaining worker profiles intact ==="
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b elis-slr-screen-impl-b elis-slr-screen-val-a elis-slr-extract-impl-a elis-slr-extract-val-b; do
    if [ -f "/home/samurai/.hermes/profiles/$p/skills/devops/kanban-worker/SKILL.md" ]; then
        echo "PASS: $p/kanban-worker/SKILL.md"
    else
        echo "FAIL: $p/kanban-worker/SKILL.md missing"
    fi
done

echo "=== 8. Confirm no Stage 7 or Stage 8 profiles exist ==="
for p in elis-slr-protocol-impl elis-slr-protocol-val elis-slr-integration-impl elis-slr-integration-val; do
    test -d "/home/samurai/.hermes/profiles/$p" && echo "WARN: $p exists (unexpected)" || echo "PASS: $p absent"
done

echo "=== Integrity check complete ==="
```

## Coordinator Reference Hashes (at artifact creation time)

These SHA256 values reflect the coordinator state BEFORE any rollback is executed. Verify these match if you suspect coordinator drift.

| File | SHA256 |
|---|---|
| `elis-slr/SOUL.md` | `a6699ac836d8c1b76ed2a73df878134294600a2e1ce6a96ae9f7015f2a3b08ad` |
| `elis-slr/SKILLS.md` | `62b454aa05ecfc9ae72fdfceb6b2b5967ddb2b1f2b7a94be1583046ca44848f816` |

## Recovery Path After Rollback

If the two Synthesis profiles need to be re-created after rollback, re-run the Stage 6 profile creation task (`t_74712b1c`), which creates:

1. `elis-slr-synth-impl-b` — model: `qwen/qwen3-coder-flash`, kanban-worker overlay
2. `elis-slr-synth-val-a` — model: `deepseek/deepseek-v4-pro`, kanban-worker overlay

Both profiles require 5 standard rollout files (AGENTS.md, CONFIG.md, SKILLS.md, CHECKLIST.md, .gitignore) plus a kanban-worker skill copy from the coordinator source.

## Governance

- **Implementer:** elis-supervisor (executed this artifact)
- **Validator:** elis-advisor (independent re-validation required — see child task)
- **PO:** Carlos Rocha
- **Artifact scope:** Documentation only. No live profile mutation during creation.
- **No credential files or credential metadata** were inspected, copied, hashed, moved, or exposed during artifact creation.
- **No Stage 7 (ELIS protocol finalization) or Stage 8 (Integration) profiles** were created.
- **No service/gateway restart, GitHub operation, smoke-chain activation, cron/background monitor, workflow migration, or Omnigent dependency** occurred during this remediation.

## Evidence

| Item | Value |
|---|---|
| Artifact path | `/home/samurai/.hermes/kanban/boards/elis-slr/artifacts/SLR-STAGE-6-SYNTHESIS-ROLLBACK.md` |
| Artifact SHA256 | Reported externally (see kanban_complete metadata and Discord PASS report) — self-referential embedding avoided |
| Compliance artifact SHA256 | `9e66e252f07cf1a05a416993768ba6b6b3ca415054137fae3cac67190000b0e9` |
| Kanban task | `t_8d532710` |
| Run ID | 89 |
| Created by | elis-supervisor |
| Date | 2026-07-22 |

## Rollback Decision Record

Before executing this rollback, confirm with PO that the decision to roll back Stage 6 Synthesis profiles is authorised. This artifact provides the procedure; it does not constitute authorisation to execute.

---

*Artifact created by elis-supervisor, Kanban task t_8d532710, Run 89. No live profiles were modified during creation.*
