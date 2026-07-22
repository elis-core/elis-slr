# SLR-STAGE-8-INTEGRATION-ROLLBACK.md

## Purpose
Rollback procedure for Stage 8 Integration worker profiles.
Removes `elis-slr-integration-impl-a` and `elis-slr-integration-val-b`.
Restores platform to pre-Stage-8 state.

## Created
2026-07-22 | elis-supervisor | Kanban t_e4b3a75c run 95

## Preconditions
- Stage 7 Protocol profiles (elis-slr-protocol-impl-b, elis-slr-protocol-val-a) intact
- Coordinator (elis-slr) SOUL.md and SKILLS.md unmodified

## Rollback Steps

### 1. Remove Integration profiles
```bash
rm -rf /home/samurai/.hermes/profiles/elis-slr-integration-impl-a
rm -rf /home/samurai/.hermes/profiles/elis-slr-integration-val-b
```

### 2. Verify removal
```bash
test ! -d /home/samurai/.hermes/profiles/elis-slr-integration-impl-a && echo "impl-a removed"
test ! -d /home/samurai/.hermes/profiles/elis-slr-integration-val-b && echo "val-b removed"
```

### 3. Verify template profiles intact
```bash
for p in elis-slr-protocol-impl-b elis-slr-protocol-val-a; do
  test -d /home/samurai/.hermes/profiles/$p && echo "$p: PRESENT" || echo "$p: MISSING"
done
```

### 4. Verify all 10 prior worker profiles intact
```bash
for p in elis-slr-harvest-impl-a elis-slr-harvest-val-b \
         elis-slr-screen-impl-b elis-slr-screen-val-a \
         elis-slr-extract-impl-a elis-slr-extract-val-b \
         elis-slr-synth-impl-b elis-slr-synth-val-a \
         elis-slr-protocol-impl-b elis-slr-protocol-val-a; do
  test -d /home/samurai/.hermes/profiles/$p && echo "$p: PRESENT" || echo "$p: MISSING"
done
```

### 5. Verify coordinator unmodified
```bash
stat --format='%Y %n' /home/samurai/.hermes/profiles/elis-slr/SOUL.md
stat --format='%Y %n' /home/samurai/.hermes/profiles/elis-slr/SKILLS.md
```
Pre-Stage-8 timestamps: SOUL.md 1784718644, SKILLS.md 1784718654

## No additional cleanup required
- No gateway, service, cron, or Discord changes were made
- No credential files were created
- No .env files exist in either profile

## Post-rollback state
Platform identical to Stage 7 completion state.
No Integration worker profiles exist.
All 10 prior profiles + coordinator intact.