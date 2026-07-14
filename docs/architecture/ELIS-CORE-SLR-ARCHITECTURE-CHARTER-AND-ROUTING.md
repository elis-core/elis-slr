# ELIS Core / ELIS SLR Architecture Charter and Routing

> **Last updated:** 2026-06-23 — Added `elis-slr` GitHub repository existence and governed migration plan preconditions.
> **Repository creation notice:** `elis-slr` repo now exists at `https://github.com/elis-core/elis-slr` (foundation state — empty/awaiting governed population). No migration, file movement, remote changes, history split, profile rebinding, gateway activation, or production cutover is authorised by this creation.

## 1. Purpose

ELIS is separating platform execution from SLR research execution to reduce routing ambiguity, prevent PM overreach, preserve governance boundaries, and support a target architecture that includes a standalone ELIS SLR repository/platform.

The `elis-slr` GitHub repository (`https://github.com/elis-core/elis-slr`) has been created as a foundation repository. It exists in an empty/population-ready state and is **not yet authorised for content migration, file movement, remote rewriting, history split, or any GitHub write operation**.

This document defines the initial Hermes/Kanban separation only. It does not approve production cutover, gateway activation, GitHub operations, or repository migration — each requires separate PO-authorised governing procedures.

## 2. Canonical Repositories and Kanban Boards

| Artifact | Name | Location / Slug | Status |
|---|---|---|---|
| ELIS Core repository | ELIS Core | `https://github.com/elis-core/elis-core` | ✅ Operational |
| ELIS SLR repository | ELIS SLR | `https://github.com/elis-core/elis-slr` | ✅ Foundation created — awaiting governed population |
| ELIS Core board | `elis-core` | ELIS Core Kanban | ✅ Operational |
| ELIS SLR board | `elis-slr` | ELIS SLR Kanban | ✅ Operational |
| A2A board | `elis-a2a-implementation` | A2A Implementation Kanban | ✅ Operational (historical) |

The `default` board is a Hermes fallback/system board only. It must not be used for ELIS work.

Deprecated/removed board names must not be used:

- `elis-pe-board`
- `elis-core-board`
- `pe-ops-hermes-a2a-triangle-01`

## 3. Ownership Split

| Role | Owns | Does Not Own |
|---|---|---|
| ELIS PM | ELIS Core PE coordination, infrastructure/programming workflow, implementation/validation sequencing | SLR execution, SLR profile creation, SLR board creation, runtime/profile/topology mutation |
| ELIS SLR | SLR research workflow coordination on `elis-slr` | ELIS Core PE work, infra/programming agents, runtime mutation outside its approved scope |
| ELIS Advisor | Governance, risk, readiness review, protocol-boundary review | Runtime execution, profile creation. Formal topology validation, if required, must be assigned to a separate authorised validation role/process and must not be implied by Advisor review |
| ELIS Supervisor | Runtime, Hermes profiles, Kanban board setup, identity/routing topology changes | PE ownership, research conclusions, GitHub remote operations |
| ELIS GitHub | Authorised GitHub/remote repository operations only | Runtime/profile/board changes, local implementation tasks unless explicitly authorised |

## 4. Routing Rules

No cross-board dispatch.

- ELIS PM must not dispatch SLR agents.
- ELIS SLR must not dispatch ELIS Core, programming, or infrastructure agents.
- ELIS Core work goes through `elis-core`.
- SLR research workflow goes through `elis-slr`.
- Existing A2A implementation history remains on `elis-a2a-implementation`.

Cross-domain coordination is allowed only as status/context reporting or through the authorised role for the issue type:

| Issue Type | Route |
|---|---|
| Governance, readiness, risk, protocol deviation | ELIS Advisor |
| Runtime, profile, board, channel, tooling, routing topology | ELIS Supervisor |
| Priority, approval, exception, cutover decision | PO |
| GitHub/remote repository operation | ELIS GitHub after PO approval |

## 5. Execution Boundary

ELIS PM must not create profiles, initialise boards, bind agents, mutate topology, activate gateways, edit secrets, propagate `.env` files, perform runtime/profile changes, or execute production cutover. PM may draft, coordinate, and route evidence only.

Supervisor owns, after PO approval:

- `elis-slr` Hermes profile creation;
- `elis-slr` Kanban board configuration;
- SLR identity/routing topology;
- SLR agent binding/reassignment;
- ELIS Core agent routing confirmation;
- profile/board/tooling changes required by the separation.

Advisor provides governance, risk, and readiness review only. Formal topology validation, if required, must be assigned to a separate authorised validation role/process and must not be implied by Advisor review.

## 6. Security and Secret Boundary

Creating or cloning an `elis-slr` profile must include a secret-scope review.

If `elis-slr` is cloned from `elis-pm`, Supervisor must identify which `.env` entries would be copied, which entries are required, and whether a minimal `.env` can be used instead. Secret values must not be exposed in reports.

A cloned `.env` must be treated as unsafe by default until ELIS Supervisor provides a redacted secret-scope inventory and PO approves either minimal-secret creation or specific propagation. Reports must name secret keys only, never values.

No Discord gateway activation, service creation, channel binding, production cutover, or GitHub operation is included in the initial bounded setup unless separately approved by PO.

## 7. Target Architecture Direction

This is a transitional runtime/governance split.

It must not entrench ELIS SLR inside ELIS Core. Future architecture should support ELIS SLR as a separate repository/platform distinct from ELIS Core when PO approves that work.

The `elis-slr` GitHub repository has been created at `https://github.com/elis-core/elis-slr` in foundation state — an empty repository awaiting governed population. For now, treat `elis-slr` as a population-ready receptacle only.

## 8. Governed Migration Plan — Required Before Any Content Movement

The `elis-slr` repository exists but **is not authorised for content migration, file movement, remote changes, history split, profile rebinding, gateway activation, or production cutover**.

The next required step before any GitHub write operation is a PO-approved governed migration plan defining:

1. **What SLR artefacts belong in `elis-slr`** — which files, directories, configs, and workflows move;
2. **What remains in `elis-core`** — clear boundary of what stays in the Core repo;
3. **Whether history is preserved or migration starts clean** — `git filter-repo`, subtree split, or fresh init;
4. **Who performs GitHub operations** — ELIS GitHub identity only, after explicit PO approval and Advisor governance/readiness review;
5. **Rollback plan** — how the migration is reversed if it fails or produces unacceptable divergence;
6. **Advisor review** — governance, risk, and protocol-boundary assessment of the migration plan before execution;
7. **PO approval** — final sign-off before any push or remote rewrite, with explicit scope and stop conditions.

Each of these elements must be documented in a migration-plan packet, reviewed by ELIS Advisor, and approved by PO before any `git push` to `elis-slr` or remote rewrite in `elis-core`.

## 9. Approval Gates

| Gate | Owner | Output |
|---|---|---|
| A | PM | Corrected charter and review packet |
| B | Advisor | Governance/readiness PASS or corrections |
| C | Supervisor | Execution packet with commands, artefacts, backup, rollback, evidence |
| D | PO | Explicit execution approval |
| E | Supervisor | Bounded setup execution |
| F | Advisor | Governance/readiness review of final evidence |
| G | PO | Closure or further instructions |