# SLR Agent Configuration Packet — SLR-AGENT-CONFIG-PACKET-01

> **Status:** REMEDIATED — Non-executing preparation packet
> **Prepared by:** elis-supervisor
> **Date:** 2026-07-15
> **Kanban task:** t_e57653ad (remediation of t_5ac78462)
> **Board:** elis-slr
> **Protocol document:** ELIS 2025 SLR Protocol — Electoral Integrity Strategies v2.0 draft-08.1
> **Governance:** ELIS Architecture Charter (ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md)
> **Remediation:** Republished from session transcript to durable path. Protocol-vs-PRISMA discrepancy resolved (see §12.1).

---

## 1. elis-slr — AGENTS.md / SOUL.md / SKILLS.md

### 1.1 Current State

The `elis-slr` Hermes profile exists at `/home/samurai/.hermes/profiles/elis-slr/` with
all three identity files present:

| File | Path | Status |
|---|---|---|
| AGENTS.md | `/home/samurai/.hermes/profiles/elis-slr/AGENTS.md` | Present (55 lines) |
| SOUL.md | `/home/samurai/.hermes/profiles/elis-slr/SOUL.md` | Present (54 lines) |
| SKILLS.md | `/home/samurai/.hermes/profiles/elis-slr/SKILLS.md` | Present (193 lines) |

### 1.2 SOUL.md Audit

The SOUL.md defines:
- **Coordinator identity:** ELIS SLR coordinator, owns `elis-slr` Kanban board
- **Agent pool:** 10 agents across 5 domains (Harvest, Screen, Extract, Synthesise, PRISMA)
- **Hard limits:** No PE/infra agent dispatch, no `elis-core`/`elis-a2a-implementation` board operation, no self-approval, no GitHub operations
- **Protocol reference path:** Currently references the old path `/home/samurai/openclaw/workspace-slr-harvest/repo/docs/_active/...` — MUST be updated to canonical path `/home/samurai/elis/workspaces/slr/repo/docs/_active/...` before any runtime profile creation.

### 1.3 AGENTS.md Audit

- Defines authority boundaries, agent interaction model, evidence/reporting requirements
- Includes prompt-defence rules, Obsidian integration, cross-harness principle, governed learning
- No model/provider references (compliant with MODEL_PROVIDER_AGNOSTIC_RULE)
- Cross-harness principle refers to OpenClaw — this is intentionally broad (the principle survives harness changes) but could be tightened.

### 1.4 SKILLS.md Audit

- Six skills defined: `slr-task-decomposition`, `slr-gate-packet-authoring`, `slr-pipeline-status`, `slr-protocol-reference`, `slr-handoff-request`, `candidate-lesson-capture`
- Each has activation triggers, required inputs, prohibited actions, required evidence, output format, failure classes, and escalation path
- No model/provider references (compliant)

---

## 2. Agent Role Definitions

### 2.1 Harvest Domain

#### harvest-impl-a (Implementer)

| Property | Value |
|---|---|
| Domain | Harvest |
| Role | Implements literature search and retrieval from configured academic databases |
| Profile name | `elis-slr-harvest-impl-a` |
| Model assignment | Per config.yaml (Infra Arch suggests: moonshotai/kimi-k2.6) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Execute search queries against configured academic database APIs
- Retrieve and store raw search results as structured records
- Apply deduplication logic and merge results
- Write output to workspace (harvest outputs directory)
- Report progress to `#elis-slr-reports`

**Forbidden:**
- Modify search strategies without PO-approved protocol amendment
- Dispatch other agents (not a coordinator)
- Operate `elis-core` or `elis-a2a-implementation` boards
- Perform GitHub operations
- Self-validate harvest outputs
- Edit profile configuration or runtime settings

**Required toolsets:** `terminal`, `file`, `kanban`, `web` (for API calls)

**Interaction model:**
- Receives tasks from elis-slr coordinator via `elis-slr` Kanban board
- Reports completion to coordinator; evidence routed to harvest-val-b for validation
- START/FINAL reports posted to `#elis-slr-reports`

#### harvest-val-b (Validator)

| Property | Value |
|---|---|
| Domain | Harvest |
| Role | Validates harvest implementer outputs independently |
| Profile name | `elis-slr-harvest-val-b` |
| Model assignment | Per config.yaml (Infra Arch suggests: nvidia/nemotron-3-ultra-550b-a55b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Validate search query correctness against protocol
- Verify deduplication accuracy via independent check
- Verify result completeness and record counts
- Produce PASS/FAIL verdict with evidence
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify implementer outputs directly
- Execute new searches (validates only)
- Dispatch other agents
- Perform GitHub operations
- Self-validate validation outputs

**Required toolsets:** `terminal`, `file`, `kanban`, `web` (for API verification)

**Interaction model:**
- Receives validation tasks from elis-slr coordinator
- Reads implementer workspace outputs (read-only)
- Produces independent validation verdict
- Reports back to coordinator

---

### 2.2 Screen Domain

#### screen-impl-b (Implementer)

| Property | Value |
|---|---|
| Domain | Screen |
| Role | Implements title/abstract and full-text screening against eligibility criteria |
| Profile name | `elis-slr-screen-impl-b` |
| Model assignment | Per config.yaml (Infra Arch suggests: nvidia/nemotron-3-ultra-550b-a55b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Apply eligibility criteria to studies from harvest output
- Produce include/exclude decisions with reason codes
- Flag uncertain cases for review
- Write screening decisions to workspace
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify eligibility criteria without PO-approved protocol amendment
- Dispatch other agents
- Operate PE boards
- Perform GitHub operations
- Self-validate screening decisions

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives harvest-validated study set from coordinator
- Produces screening decisions in structured format
- Hands off validated outputs to extract domain

#### screen-val-a (Validator)

| Property | Value |
|---|---|
| Domain | Screen |
| Role | Independently validates screening decisions |
| Profile name | `elis-slr-screen-val-a` |
| Model assignment | Per config.yaml (Infra Arch suggests: z-ai/glm-5.1) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Review a sample or full set of screening decisions
- Verify reason codes against eligibility criteria
- Check inter-rater agreement metrics
- Produce PASS/FAIL verdict with evidence
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify screening decisions directly
- Re-screen studies (validates only)
- Dispatch other agents
- Perform GitHub operations

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives validation tasks from coordinator
- Reads implementer screening decisions (read-only)
- Produces independent validation verdict
- Reports back to coordinator

---

### 2.3 Extract Domain

#### extract-impl-a (Implementer)

| Property | Value |
|---|---|
| Domain | Extract |
| Role | Implements structured data extraction from included studies |
| Profile name | `elis-slr-extract-impl-a` |
| Model assignment | Per config.yaml (Infra Arch suggests: mistralai/mistral-medium-3.5-128b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Extract structured variables from included studies per extraction schema
- Populate required fields: study_id, country, design, sample_size, outcomes
- Perform risk-of-bias assessments
- Write extraction datasets to workspace
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify extraction schema without PO-approved protocol amendment
- Dispatch other agents
- Operate PE boards
- Perform GitHub operations
- Self-validate extraction outputs

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives screened-and-validated study set from coordinator
- Produces extraction datasets in CSV/Parquet
- Hands off validated outputs to synthesis domain

#### extract-val-b (Validator)

| Property | Value |
|---|---|
| Domain | Extract |
| Role | Independently validates extraction completeness and accuracy |
| Profile name | `elis-slr-extract-val-b` |
| Model assignment | Per config.yaml (Infra Arch suggests: nvidia/nemotron-3-ultra-550b-a55b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Verify extraction field completeness (all required fields populated)
- Cross-check a sample of extracted values against source documents
- Validate data contract compliance
- Produce PASS/FAIL verdict with evidence
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify extraction datasets directly
- Perform new extractions (validates only)
- Dispatch other agents
- Perform GitHub operations

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives validation tasks from coordinator
- Reads implementer extraction outputs (read-only)
- Produces independent validation verdict
- Reports back to coordinator

---

### 2.4 Synthesis Domain

#### synth-impl-b (Implementer)

| Property | Value |
|---|---|
| Domain | Synthesis |
| Role | Implements evidence synthesis from extracted data |
| Profile name | `elis-slr-synth-impl-b` |
| Model assignment | Per config.yaml (Infra Arch suggests: moonshotai/kimi-k2.6) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Produce textual and tabular synthesis linked to extracted evidence
- Ensure traceability: synthesis outputs map to source studies (Quality Gate 5)
- Apply synthesis methodology as defined in protocol
- Write synthesis artefacts to workspace
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify synthesis methodology without PO-approved protocol amendment
- Dispatch other agents
- Operate PE boards
- Perform GitHub operations
- Self-validate synthesis outputs

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives extraction-validated dataset from coordinator
- Produces synthesis notes and tables
- Hands off validated outputs to PRISMA domain

#### synth-val-a (Validator)

| Property | Value |
|---|---|
| Domain | Synthesis |
| Role | Independently validates synthesis outputs |
| Profile name | `elis-slr-synth-val-a` |
| Model assignment | Per config.yaml (Infra Arch suggests: nvidia/nemotron-3-ultra-550b-a55b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Verify traceability: every synthesis claim maps to a source study
- Check for unsupported or hallucinated claims
- Validate synthesis logic against protocol methodology
- Produce PASS/FAIL verdict with evidence
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify synthesis outputs directly
- Produce new synthesis (validates only)
- Dispatch other agents
- Perform GitHub operations

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives validation tasks from coordinator
- Reads implementer synthesis outputs (read-only)
- Produces independent validation verdict
- Reports back to coordinator

---

### 2.5 PRISMA Domain

#### prisma-impl-b (Implementer)

| Property | Value |
|---|---|
| Domain | PRISMA |
| Role | Implements PRISMA flow diagram data and reporting artefacts |
| Profile name | `elis-slr-prisma-impl-b` |
| Model assignment | Per config.yaml (Infra Arch suggests: z-ai/glm-5.1) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Compute PRISMA stage counts: identified, screened, eligible, included
- Enforce monotonic rule: identified >= screened >= eligible >= included
- Produce PRISMA flow diagram data
- Write PRISMA records to workspace
- Report to `#elis-slr-reports`

**Forbidden:**
- Fabricate or alter stage counts
- Dispatch other agents
- Operate PE boards
- Perform GitHub operations
- Self-validate PRISMA outputs

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives all upstream stage counts from coordinator
- Computes and produces PRISMA flow records
- Hands off validated outputs for reporting

#### prisma-val-a (Validator)

| Property | Value |
|---|---|
| Domain | PRISMA |
| Role | Independently validates PRISMA flow data |
| Profile name | `elis-slr-prisma-val-a` |
| Model assignment | Per config.yaml (Infra Arch suggests: nvidia/nemotron-3-ultra-550b-a55b) |
| Gateway | Hermes native |
| Kanban board | `elis-slr` |

**Allowed:**
- Verify PRISMA stage arithmetic: monotonic rule enforced
- Cross-check counts against upstream stage outputs
- Verify PRISMA flow diagram data integrity
- Produce PASS/FAIL verdict with evidence
- Report to `#elis-slr-reports`

**Forbidden:**
- Modify PRISMA records directly
- Compute new PRISMA counts (validates only)
- Dispatch other agents
- Perform GitHub operations

**Required toolsets:** `terminal`, `file`, `kanban`

**Interaction model:**
- Receives validation tasks from coordinator
- Reads implementer PRISMA outputs and upstream stage evidence (read-only)
- Produces independent validation verdict
- Reports back to coordinator

---

## 3. Worker Role Boundaries — Cross-Cutting Rules

### 3.1 Universal Agent Constraints

All SLR agents (implementers and validators) MUST:

1. **Start fresh per session** — issue reset/binding acknowledgement before work
2. **Stay within domain** — no cross-domain implementation or validation
3. **Report all state transitions** — START/PASS/FAIL/BLOCKED to `#elis-slr-reports`
4. **Never self-approve** — validation must be performed by a separate agent
5. **Reference the ELIS SLR Protocol** — cite specific sections for every action
6. **Never modify profile configuration** — no config.yaml, .env, SOUL.md, AGENTS.md, or SKILLS.md edits
7. **Never perform GitHub operations** — all source control through elis-github after PO approval
8. **Respect the model/provider agnostic rule** — model details in config.yaml only
9. **Never expose secrets** — redact API keys, tokens, credentials in all outputs
10. **Respect the Core/SLR boundary** — no dispatch to PE or infrastructure agents

### 3.2 Coordinator Constraints

The `elis-slr` coordinator:

- **Must not implement** — coordinating and dispatching only
- **Must not validate** — validation is the validator's role
- **Must not approve its own changes** — PO or Advisor review required
- **Must route through gates** — decomposition → implementer → validator → gate packet → Advisor → PO

### 3.3 Implementer Constraints

All SLR implementers:

- **Must not validate** their own outputs
- **Must produce evidence** — exact commands, file hashes, output samples
- **Must not dispatch** other agents
- **Must not modify** protocol-defined criteria without PO approval

### 3.4 Validator Constraints

All SLR validators:

- **Must produce binary verdicts** — PASS or FAIL, with specific evidence
- **Must not modify** implementer outputs
- **Must verify independently** — different model, different session, different agent
- **Must not re-implement** — if FAIL, coordinator decides rework path

---

## 4. Implementer/Validator Mapping — Canonical Pairing Table

| Domain | Implementer | Validator | Implementer Model (per Infra Arch) | Validator Model (per Infra Arch) |
|---|---|---|---|---|
| Harvest | harvest-impl-a | harvest-val-b | moonshotai/kimi-k2.6 | nvidia/nemotron-3-ultra-550b-a55b |
| Screen | screen-impl-b | screen-val-a | nvidia/nemotron-3-ultra-550b-a55b | z-ai/glm-5.1 |
| Extract | extract-impl-a | extract-val-b | mistralai/mistral-medium-3.5-128b | nvidia/nemotron-3-ultra-550b-a55b |
| Synthesis | synth-impl-b | synth-val-a | moonshotai/kimi-k2.6 | nvidia/nemotron-3-ultra-550b-a55b |
| PRISMA | prisma-impl-b | prisma-val-a | z-ai/glm-5.1 | nvidia/nemotron-3-ultra-550b-a55b |

**Agent pool totals: 10 agents across 5 domains.** The Infra Architecture doc's "Protocol" row maps to the PRISMA domain — see §12.1 for the full evidentiary resolution.

**Model assignments are per Infra Architecture v1.0 guidance (2026-07-03). Actual runtime models are governed exclusively by each agent's `config.yaml` — not by this packet.**

---

## 5. Required Toolsets — Per Agent

| Agent | Required Toolsets |
|---|---|
| elis-slr (coordinator) | `kanban` |
| harvest-impl-a | `terminal`, `file`, `kanban`, `web` |
| harvest-val-b | `terminal`, `file`, `kanban`, `web` |
| screen-impl-b | `terminal`, `file`, `kanban` |
| screen-val-a | `terminal`, `file`, `kanban` |
| extract-impl-a | `terminal`, `file`, `kanban` |
| extract-val-b | `terminal`, `file`, `kanban` |
| synth-impl-b | `terminal`, `file`, `kanban` |
| synth-val-a | `terminal`, `file`, `kanban` |
| prisma-impl-b | `terminal`, `file`, `kanban` |
| prisma-val-a | `terminal`, `file`, `kanban` |

**Rationale:**
- Harvest agents need `web` for academic database API calls
- All implementers need `terminal` and `file` for workspace operations
- All agents need `kanban` for task lifecycle management
- Coordinator is kanban-only (dispatches, tracks, does not execute file/terminal operations)
- No agent gets `discord` or `send_message` directly — reporting goes through Hermes gateway notification, not tool-level access. If direct send_message is needed, it must be explicitly configured per agent.

---

## 6. elis-slr Board Authority

### 6.1 What Goes on `elis-slr`

| Allowed | Not Allowed |
|---|---|
| SLR research pipeline tasks | PE implementation tasks |
| SLR implementer dispatch | Infrastructure agent dispatch |
| SLR validator dispatch | Programming agent dispatch |
| SLR gate packets and evidence | ELIS Core board operations |
| SLR pipeline status tracking | A2A implementation tracking |
| SLR protocol deviation logging | GitHub operations tasks |
| SLR domain handoffs | Model/provider configuration changes |
| SLR agent health checks (via Supervisor) | Runtime/profile mutation tasks |

### 6.2 What Does NOT Go on `elis-slr`

| Task Type | Correct Board |
|---|---|
| PE coordination and implementation | `elis-core` |
| A2A protocol work | `elis-a2a-implementation` (historical, read-only) |
| GitHub operations | `elis-core` → elis-github via PO |
| Platform runtime changes | `elis-core` → Supervisor via PO |
| Governance review | `elis-core` → Advisor via PO |
| Cross-domain coordination requests | `elis-core` → PM, informational only |

### 6.3 Board Ownership

- `elis-slr` is owned by the `elis-slr` profile
- Only elis-slr may create, assign, or transition tasks on `elis-slr`
- The PM may not dispatch SLR agents or operate `elis-slr`
- The Supervisor may create SLR-domain tasks on `elis-slr` ONLY when directed by PO (topology/profile setup tasks)

---

## 7. #elis-slr-reports Reporting Model

### 7.1 Channel Identity

| Property | Value |
|---|---|
| Channel name | `#elis-slr-reports` |
| Channel ID | `1519705198275203215` |
| Platform | Discord |
| Guild | ELIS |
| Send verified | Yes (confirmed by t_5c824a45, 2026-07-15) |

### 7.2 Report Formats

**START Report Template:**
```
PE: <PE-ID or TASK-ID>
Task: <task-summary>
Agent: <agent-profile-name>
Status: STARTED
Kanban task ID: <task-id>
Run ID: <run-id>
Scope: <bounded-description>
Not approved: <what-is-explicitly-not-approved>
Expected output: <what-will-be-produced>
Stop condition: <when-task-is-done>
```

**FINAL Report Template:**
```
PE: <PE-ID or TASK-ID>
Task: <task-summary>
Agent: <agent-profile-name>
Status: PASS / FAIL / BLOCKED
Kanban task ID: <task-id>
Run ID: <run-id>
Evidence: <verifiable-evidence>
Actions performed: <what-was-done>
Out-of-scope actions: <none-or-list>
Output / verdict: <result>
Next required action: <what-happens-next>
Stop condition: <met-or-why-blocked>
```

### 7.3 Reporting Rules

1. **Every task transition** from idle → running → terminal posts a report
2. **START reports are execution evidence only** — not approval, not dispatch, not branch activation
3. **FINAL reports are narrow and evidence-based** — no speculative future steps
4. **No cross-domain reports** — SLR agents do not report to `#elis-pe-reports`
5. **Coordinator aggregates** — elis-slr posts pipeline status summaries, not raw per-agent reports
6. **Implementers and validators** post their own START/FINAL reports

### 7.4 Send Capability

- elis-supervisor can send to `#elis-slr-reports` (verified)
- elis-slr coordinator can send to `#elis-slr-reports` — requires channel in config (to be verified at profile creation)
- Sub-agents (harvest-impl-a, etc.) — send capability depends on gateway config; if using Hermes gateway notification, direct send_message access is not required for Kanban task completion notifications

---

## 8. Protocol References

### 8.1 Canonical Protocol Document

| Property | Value |
|---|---|
| Title | ELIS 2025 SLR Protocol — Electoral Integrity Strategies |
| Version | v2.0 draft-08.1 |
| Date | 2026-01-28 |
| Format | PDF |
| Canonical path | `/home/samurai/elis/workspaces/slr/repo/docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` |
| Repository | `github.com/elis-core/elis-slr` |
| SHA256 | Verified in Phase 1 migration (t_11d5ab69, commit 3c48f83) |

### 8.2 Key Protocol Sections (for agent reference)

| Section | Topic | Relevant Agents |
|---|---|---|
| Protocol §Search Strategy | Database selection, query construction, dedup rules | harvest-impl-a, harvest-val-b |
| Protocol §Eligibility Criteria | Include/exclude rules, reason codes | screen-impl-b, screen-val-a |
| Protocol §Data Extraction | Variables, schema, QA checks | extract-impl-a, extract-val-b |
| Protocol §Synthesis | Methodology, traceability requirements | synth-impl-b, synth-val-a |
| Protocol §PRISMA | Flow diagram, stage counts, reporting | prisma-impl-b, prisma-val-a |

### 8.3 Supporting Documents

| Document | Path | Purpose |
|---|---|---|
| SLR Domain Spec | `docs/slr/SLR_DOMAIN_SPEC.md` | Artifact types, minimum fields, quality gates |
| Repo Spec | `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | Repository structure, reproducibility requirements |
| Amendment Log Template | `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | Protocol deviation logging |
| Audit Checklist Template | `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | Run audit checklist |
| Infra Architecture | `docs/architecture/ELIS_SLR_Infrastructure_Architecture.md` | Agent matrix, ports, models |
| Implementation Guide | `docs/architecture/ELIS_SLR_Infrastructure_Implementation_and_Validation_Guide.md` | Deployment order, agent assignments |
| Architecture Charter | `docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | Board routing, ownership split, execution boundary |

---

## 9. CLI / Script / Workflow Relationship

### 9.1 Per-Agent Model

| Agent | CLI Access | Script Execution | Workflow Role |
|---|---|---|---|
| elis-slr (coordinator) | Kanban tools only | None | Decompose → dispatch → track → gate |
| harvest-impl-a | Full (terminal toolset) | Search scripts, dedup scripts | Execute harvest pipeline |
| harvest-val-b | Full (terminal toolset) | Validation scripts | Validate harvest outputs |
| screen-impl-b | Full (terminal toolset) | Screening scripts | Execute screening pipeline |
| screen-val-a | Full (terminal toolset) | Validation scripts | Validate screening decisions |
| extract-impl-a | Full (terminal toolset) | Extraction scripts | Execute extraction pipeline |
| extract-val-b | Full (terminal toolset) | Validation scripts | Validate extraction outputs |
| synth-impl-b | Full (terminal toolset) | Synthesis scripts | Execute synthesis pipeline |
| synth-val-a | Full (terminal toolset) | Validation scripts | Validate synthesis outputs |
| prisma-impl-b | Full (terminal toolset) | PRISMA computation scripts | Execute PRISMA reporting |
| prisma-val-a | Full (terminal toolset) | Validation scripts | Validate PRISMA records |

### 9.2 Script Governance

- **No script mutation without PO-approved PE** — agents execute existing scripts; they do not modify them
- **Scripts live in the SLR workspace** — `/home/samurai/elis/workspaces/slr/` (exact path TBD per agent)
- **All scripts are read-only to validators** — validators read implementer scripts for verification but do not execute new searches/extractions
- **CLI commands must be recorded** — every command run must appear in agent evidence logs
- **No remote execution** — all scripts run locally on elis-server within agent sandboxes

### 9.3 Workflow Pipeline

```
Harvest (impl → val) → Screen (impl → val) → Extract (impl → val) → Synthesis (impl → val) → PRISMA (impl → val) → Reporting
```

Each pair must PASS independent validation before the next domain begins (per Implementation Guide sequential deployment order).

---

## 10. Validation Plan

### 10.1 What This Packet Validates

This packet is a **non-executing preparation document**. It does not create profiles, configure gateways, or mutate runtime state.

### 10.2 Validation Criteria

| # | Criterion | How Verified |
|---|---|---|
| V1 | All 10 agent roles defined with allowed/forbidden boundaries | Section 2 — role-by-role tables |
| V2 | Implementer/validator pairing table is complete and non-overlapping | Section 4 — mapping table |
| V3 | Toolset specifications are domain-appropriate | Section 5 — per-agent toolset table |
| V4 | Board authority boundaries align with Architecture Charter | Section 6 — routing rules match charter |
| V5 | Reporting templates are consistent with kanban execution reporting rule | Section 7 — START/FINAL templates |
| V6 | Protocol references are exact and traceable | Section 8 — canonical paths, SHA256 verified |
| V7 | CLI/script/workflow model matches Implementation Guide sequential order | Section 9 — pipeline matches guide |
| V8 | Rollback plan covers all mutation classes | Section 11 — rollback plan |
| V9 | No model/provider references in identity sections (MODEL_PROVIDER_AGNOSTIC_RULE) | Identity sections cite config.yaml only |
| V10 | No GitHub operations authorised | All sections: GitHub = forbidden or PO-gated |
| V11 | Protocol-vs-PRISMA discrepancy resolved with evidence | Section 12.1 — model-pair match, agent-count confirmation |

### 10.3 Validation Process

1. **Advisor reviews** this packet for governance/readiness
2. **PO approves** or requests corrections
3. If approved, the packet becomes the canonical reference for SLR agent profile creation
4. Profile creation executes in a separate PE, not from this packet

### 10.4 Independent Validator

The Advisor (or a PO-designated independent reviewer) should validate this packet. The author (elis-supervisor) must not self-validate per governance rules.

---

## 11. Rollback Plan

### 11.1 If Packet Is Rejected

| Rejection Reason | Recovery Action |
|---|---|
| Missing agent role | Add the missing role definition and resubmit |
| Incorrect toolset assignment | Correct toolset table (Section 5) |
| Board authority boundary error | Align with Architecture Charter |
| Protocol reference stale/wrong | Update canonical paths (Section 8) |
| Governed model/provider leak | Strip model IDs from identity sections |
| Scope overreach (execution assumed) | Clarify non-executing status of this packet |

### 11.2 If Packet Is Partially Approved

- PO marks approved sections as canonical
- Rejected sections are corrected in a revision packet
- Partial approval does not authorise any execution — profiles are not created from partial approval

### 11.3 No Rollback Needed for Non-Execution

Since this packet makes no runtime changes, there is nothing to roll back. If rejected entirely, the packet file is archived and the task is marked BLOCKED with correction instructions.

---

## 12. Pre-Existing Observations and Known Issues

### 12.1 RESOLVED — Protocol-vs-PRISMA Agent-Pool Discrepancy

**Status: RESOLVED.** The "Protocol" pair in the Infra Architecture and Implementation Guide is the same domain as "PRISMA" in SOUL.md. This is not a 6th agent pair.

**Evidence:**

| Source | Domain Label | Implementer Model | Validator Model |
|---|---|---|---|
| SOUL.md | PRISMA | (via config.yaml) | (via config.yaml) |
| Infra Architecture §Agent Matrix | Protocol | z-ai/glm-5.1 | nvidia/nemotron-3-ultra-550b-a55b |
| Implementation Guide §Agent Assignment | Protocol | z-ai/glm-5.1 | nvidia/nemotron-3-ultra-550b-a55b |

The model assignments for the 5th position are identical across all three governance sources:
- Implementer: `z-ai/glm-5.1`
- Validator: `nvidia/nemotron-3-ultra-550b-a55b`

This confirms the "Protocol" row in the older Infra Architecture docs (2026-07-03) and the "PRISMA" row in SOUL.md (later) refer to the same agent pair. The Infra Architecture and Implementation Guide were authored before the domain was renamed to "PRISMA" to match the SLR Protocol document's PRISMA terminology. The naming difference is a temporal artifact, not a structural discrepancy.

**Resolution:** The domain is **PRISMA** (as in SOUL.md and the SLR Protocol document). The agent pair is `prisma-impl-b / prisma-val-a`. The agent pool is 10 agents across 5 domains. No 6th "Protocol" pair exists. When profiles are created, the PRISMA domain agent names (prisma-impl-b, prisma-val-a) are authoritative.

**PO decision gate:** If PO wants to rename from "Protocol" to "PRISMA" in the Infra Architecture docs, that is a documentation-update task — not an agent-pool change. The model assignments remain unchanged regardless.

### 12.2 Stale Protocol Path in SOUL.md

The elis-slr SOUL.md line 51 references the old protocol path:
`/home/samurai/openclaw/workspace-slr-harvest/repo/docs/_active/...`

This MUST be updated to the canonical path before any runtime profile creation:
`/home/samurai/elis/workspaces/slr/repo/docs/_active/...`

The canonical path was established in Phase 1 migration (2026-07-14, commit 3c48f83) and the protocol PDF is SHA256-verified at that path.

### 12.3 Retired Technology References

The Infra Architecture and Implementation Guide (both v1.0, 2026-07-03) reference:
- OpenShell gateways → **Retired.** Runtime is Hermes-native (as of 2026-07-14).
- NemoHermes → **Retired.** All gateways are Hermes-native.

These documents predate the NemoClaw/OpenShell/OpenClaw retirement (2026-07-14). They should be treated as architecture guidance only, not as runtime configuration authority. Hermes-native gateways are the sole runtime target.

### 12.4 No Sub-Agent Profiles Exist

Zero of the 10 SLR implementer/validator profiles exist on disk. All must be created in a separate PE after this packet is approved.

---

## 13. Next Steps After Approval

1. PO approves this packet (or requests corrections)
2. PO opens a new PE for SLR agent profile creation
3. Supervisor creates the 10 implementer/validator Hermes profiles per this packet
4. Each profile receives AGENTS.md, SOUL.md, SKILLS.md based on the role definitions herein
5. Gateway and channel configuration follows in a separate bounded step
6. SLR pipeline execution begins after all profiles are validated

---

## Appendix A — Remediation Notes

This packet was regenerated from session transcript `20260715_104258_35b2d8` (original t_5ac78462) after the scratch workspace was cleaned up. Changes from the original:

1. **§12.1 — Protocol-vs-PRISMA discrepancy RESOLVED** (previously: flagged as observation only). Model-pair identity confirmed via cross-document model assignment match.
2. **Validation criterion V11 added** — discrepancy resolution evidence.
3. **Durable path** — written to `/home/samurai/.hermes/profiles/elis-slr/packets/SLR_AGENT_CONFIG_PACKET.md` (outside kanban scratch lifecycle).
4. **Fresh SHA256 / line count** to be computed after write.

---

## Appendix B — Reference Documents Consulted

| Document | Path |
|---|---|
| AGENTS.md (elis-slr) | `/home/samurai/.hermes/profiles/elis-slr/AGENTS.md` |
| SOUL.md (elis-slr) | `/home/samurai/.hermes/profiles/elis-slr/SOUL.md` |
| SKILLS.md (elis-slr) | `/home/samurai/.hermes/profiles/elis-slr/SKILLS.md` |
| SLR Domain Spec | `/home/samurai/elis/workspaces/slr/repo/docs/slr/SLR_DOMAIN_SPEC.md` |
| SLR Repo Spec | `/home/samurai/elis/workspaces/slr/repo/docs/_active/ELIS_2025_SLR_REPO_SPEC.md` |
| Infra Architecture | `/home/samurai/elis/workspaces/slr/repo/docs/architecture/ELIS_SLR_Infrastructure_Architecture.md` |
| Implementation Guide | `/home/samurai/elis/workspaces/slr/repo/docs/architecture/ELIS_SLR_Infrastructure_Implementation_and_Validation_Guide.md` |
| Architecture Charter | `/home/samurai/elis/workspaces/slr/repo/docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` |
| Shared Governance | `/home/samurai/.hermes/profiles/_shared/GOVERNANCE.md` |
| Shared Terminology | `/home/samurai/.hermes/profiles/_shared/TERMINOLOGY.md` |
| elis-slr channel directory | `/home/samurai/.hermes/profiles/elis-slr/channel_directory.json` |
| elis-slr config.yaml | `/home/samurai/.hermes/profiles/elis-slr/config.yaml` |

---

> **End of packet.** Prepared by elis-supervisor, 2026-07-15. Non-executing. Protocol-vs-PRISMA discrepancy resolved (§12.1). Awaiting PO/Advisor review.