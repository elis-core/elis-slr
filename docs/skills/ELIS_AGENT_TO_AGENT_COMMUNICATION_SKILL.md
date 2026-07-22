---
name: ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL
description: Defines ELIS agent-to-agent communication protocol, Kanban authoritative records, #elis-pe-reports telemetry, PO approval boundaries, GitHub durable publication, and artifact exchange/validation rules
version: 1.0.0
platforms: [linux]
categories: [elis, communication, governance]
---

# ELIS Agent-to-Agent Communication Skill

This skill defines the unified ELIS communication architecture covering A2A agent-to-agent operational messages, Kanban authoritative task/evidence records, #elis-pe-reports append-only PO telemetry, PO approval/escalation boundaries, GitHub durable publication/change records, and artifact handoff/validation rules.

## 1. Communication Hierarchy

The five ELIS communication layers have **distinct authority roles**. This is NOT an evidence-authority hierarchy — A2A carries operational messages, but Kanban remains authoritative for task state and evidence at all times.

```
┌─────────────────────────────────────────────────────────────┐
│  PO Direct Instruction                                      │
│  (approvals, exceptions, escalations)                       │
├─────────────────────────────────────────────────────────────┤
│  A2A (JSON-RPC over HTTP)                                   │
│  agent-to-agent operational message transport layer         │
├─────────────────────────────────────────────────────────────┤
│  Kanban (SQLite DB)                                         │
│  authoritative workflow / task / evidence record            │
├─────────────────────────────────────────────────────────────┤
│  #elis-pe-reports (Discord)                                 │
│  append-only PO-visible telemetry; agents send only         │
├─────────────────────────────────────────────────────────────┤
│  GitHub (git + Issues + PRs)                                │
│  durable publication / change record                        │
└─────────────────────────────────────────────────────────────┘
```

**This diagram shows communication and record layers, not evidence priority. Kanban remains the authoritative workflow and evidence record even when A2A is used for delivery.**

**Rules:**
- PO direct instruction controls approvals, exceptions, and escalations.
- A2A carries agent-to-agent operational messages.
- Kanban remains authoritative for workflow state and evidence.
- #elis-pe-reports provides append-only PO-visible telemetry.
- GitHub records durable source/publication changes.

## 2. Channel Decision Table

| I need to... | Use this channel | Because |
|---|---|---|
| Request validation from Advisor | A2A (PM→Advisor) | A2A is the operational message transport |
| Request implementation from Supervisor | A2A (PM→Supervisor) | A2A is the operational message transport |
| Return a validation verdict | A2A (Advisor→PM) | A2A response stream or PM endpoint |
| Return implementation results | A2A (Supervisor→PM) | A2A response stream or PM endpoint |
| Track task lifecycle state | Kanban | Kanban is authoritative record |
| Record evidence | Kanban (comment / metadata) | Evidence is tied to task lifecycle |
| Notify PO of an event | #elis-pe-reports (send only) | PO-visible telemetry channel |
| Request PO approval | PO direct instruction (Discord @mention) | PO is the only approval authority |
| Escalate a blocked task | PO direct instruction (Discord @ELIS PM) | Escalations need human judgement |
| Publish source-code change | GitHub (PR / commit) | GitHub is the durable change record |
| Store durable task evidence | Kanban board artifacts dir | Scratch workspace is ephemeral |
| Hand off artifact manifest | A2A (result message) | A2A carries manifests; Kanban stores durable artifact |

## 3. Mandatory A2A Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `elis_sender_role` | string | Always | One of: `pm`, `advisor`, `supervisor`, `github` |
| `elis_message_type` | string | Always | One of the approved top-level types |
| `elis_sent_at` | ISO 8601 | Always | UTC timestamp with literal Z |
| `elis_policy_version` | string | Always | Currently `1.0.0` |
| `elis_task_ref` | string | All operational msgs | Kanban task ID. **Mandatory** for all operational A2A messages. May be omitted only if `elis_message_class="diagnostic"` AND no workflow action, validation, implementation, GitHub operation, or production decision is requested |
| `elis_pe_ref` | string | PE-scoped msgs | PE identifier for traceability |
| `elis_reply_requested` | string | When reply needed | `"true"` or `"false"` |
| `elis_reply_endpoint` | string | When reply via A2A | Full A2A URL |
| `elis_reply_channel` | string | When reply via A2A | `"a2a"` |
| `elis_authoritative_record` | string | All result types | Reference to Kanban record, board artifact, PR URL, commit SHA, or evidence file with hash. Required for: `validation_result`, `implementation_result`, `github_result`, `blocked_notice`, `ready_for_po` |

### Additional optional fields

| Field | Type | Used In | Description |
|-------|------|---------|-------------|
| `elis_target_role` | string | `request` | Declared recipient |
| `elis_board` | string | `request` | Kanban board slug |
| `elis_requested_action` | string | `request` | Subtype: `provide_validation_report`, `run_implementation`, `perform_github_operation`, `evidence_handoff` |
| `elis_reply_to_role` | string | Result types | Original requester role |
| `elis_result_type` | string | Result types | Subtype: `validation_report`, `implementation_report`, `publication_report`, `blocked`, `gate_packet_ready` |
| `elis_gate_ref` | string | Any | Gate identifier |
| `elis_session_id` | string | Any | Worker session identifier |
| `elis_message_class` | string | Diagnostic only | `"diagnostic"` to exempt from task_ref requirement |
| `elis_correlation_id` | string | Any | OpenTelemetry-style correlation ID for cross-system traceability |
| `elis_parent_task_ref` | string | Any | Parent Kanban task ID for child-task traceability |
| `elis_artifact_id` | string | Result types | Stable artifact identifier for the resulting artifact |

## 4. Approved A2A Message Types

### Top-Level Types (elis_message_type)
- `request` — Request validation or implementation
- `ack` — Acknowledge receipt
- `status` — Status update on in-progress task
- `validation_result` — Validation report return
- `implementation_result` — Implementation result return
- `github_result` — GitHub operation result
- `blocked_notice` — Agent blocked and requires PO/PM input
- `ready_for_po` — Artifact ready for PO decision

### Subtypes (elis_result_type / elis_requested_action)
Subtypes classify the specific action within a top-level type:
- `request` → `elis_requested_action`: `provide_validation_report`, `run_implementation`, `perform_github_operation`, `evidence_handoff`
- `validation_result` → `elis_result_type`: `validation_report`, `packet_review`
- `implementation_result` → `elis_result_type`: `implementation_report`, `diagnostic_report`
- `github_result` → `elis_result_type`: `publication_report`, `pr_status`
- `blocked_notice` → `elis_result_type`: `blocked`, `deferred`
- `ready_for_po` → `elis_result_type`: `gate_packet_ready`, `approval_requested`

## 5. Authorised A2A Routes

| From | To | Status | Notes |
|------|----|--------|-------|
| ELIS PM | ELIS Advisor | ✅ Live | PM→Advisor operational requests |
| ELIS PM | ELIS Supervisor | ✅ Live | PM→Supervisor operational requests |
| ELIS Advisor | ELIS PM | ✅ Live | Validation results, blocked notices, PO-ready notices |
| ELIS Supervisor | ELIS PM | ✅ Live | Implementation results, blocked notices |
| ELIS GitHub | ELIS PM | ⏳ Deferred | PM→GitHub and GitHub→PM become authorised only after the GitHub A2A production activation PE passes and PO approves route enablement. Until then, GitHub A2A routes remain deferred even if implementation code or PRs exist |
| ELIS PM | ELIS GitHub | ⏳ Deferred | PM→GitHub and GitHub→PM become authorised only after the GitHub A2A production activation PE passes and PO approves route enablement. Until then, GitHub A2A routes remain deferred even if implementation code or PRs exist |

**Current live baseline:**
- PM, Advisor, and Supervisor A2A endpoints are live.
- GitHub A2A remains deferred or pending production activation unless separately PO-approved.
- Ideas A2A remains deferred.
- No all-roster A2A production claim is made by this skill.

## 6. Discord Permission Model

- Agents **can send** to #elis-pe-reports (PO-visible telemetry)
- Agents **cannot read** #elis-pe-reports history
- #elis-pe-reports is not memory, evidence, authority, or handoff state

## 7. Artifact Exchange and Validation

### Artifact exchange principle
Agents exchange artifact references and manifests over A2A, not large artifact bodies.

> A2A carries artifact manifests, summaries, verdicts, and handoff notices. Kanban, repository files, board artifact directories, or GitHub PRs store durable artifacts. #elis-pe-reports only notifies PO that an artifact event occurred.

### Durable storage hierarchy
- source code change → Git working tree / branch / PR
- validation report → repo file or Kanban board artifact
- runtime evidence log → durable evidence path referenced in Kanban
- gate packet → Kanban task/comment body
- implementation report → Kanban comment plus optional artifact file
- published docs → GitHub repo
- large logs → artifact file, not A2A or Discord body

> Scratch workspace files are not final durable evidence unless copied/referenced into an authoritative Kanban artifact or repository path.

### Required artifact manifest
Every implementation or validation result MUST include or reference an artifact manifest containing:
- `artifact_id` — Unique identifier
- `artifact_type` — Type of artifact
- `producer_role` — Role that produced the artifact
- `validator_role` — Role that validated (if applicable)
- `kanban_board` — Board slug
- `kanban_task` — Task ID
- `pe_ref` — PE identifier
- `storage_location` — Durable path or reference
- `files` — List with path/status/sha256 where practical
- `summary` — Human-readable summary
- `validation_status` — PASS/FAIL/BLOCKED/PENDING
- `created_at` — ISO 8601 UTC timestamp
- `authoritative_record` — Reference to authoritative Kanban record

### Implementation-result handoff
Implementer must report: task ID, parent PE/task, files changed, files explicitly NOT changed, commands/checks run, evidence path, artifact manifest reference, known deviations, rollback/cleanup state, next required actor.

**Implementer must not validate its own artifact.**

### Validation-result handoff
Advisor must report: validated artifact reference, validation task ID, verdict (PASS/FAIL/BLOCKED), evidence inspected, acceptance criteria mapping, defects/blockers, out-of-scope actions, residual risks, next required action, authoritative Kanban record.

**Advisor must validate from durable artifacts, not from Discord or uncited A2A message content.**

### Artifact states
`DRAFT` → `IMPLEMENTED` → `IMPLEMENTATION_EVIDENCE_READY` → `VALIDATION_READY` → `VALIDATED_PASS` / `VALIDATED_FAIL` / `BLOCKED` → `SUPERSEDED` / `PUBLISHED` / `ROLLED_BACK`

### Forbidden artifact practices
- Pasting large logs into A2A
- Pasting large logs into #elis-pe-reports
- Treating Discord as evidence
- Treating A2A message body as the artifact when a durable artifact is required
- Using scratch-only files as final evidence
- Self-validation
- GitHub publication without PO-approved ELIS GitHub handoff
- Production claims without validation and PO approval
- Treating #elis-pe-reports as memory, evidence, handoff, or authority source

### GitHub publication handoff
GitHub publication is a separate step after validation and PO approval. Required fields: target repo, target branch, exact file manifest, excluded files, commit message, PR title/body, evidence references, diff-bound checks, no-merge-without-PO rule.

### Recommended artifact lifecycle
1. PM creates/assigns Kanban task
2. Implementer produces artifact in durable location
3. Implementer records artifact manifest in Kanban
4. Implementer sends `implementation_result` to PM via A2A
5. PM creates validation task
6. Validator validates artifact from durable location
7. Validator records validation verdict in Kanban
8. Validator sends `validation_result` to PM via A2A
9. Agent posts compact event to #elis-pe-reports
10. PO approves closeout/GitHub/publication if needed

### Reference document
For the full best-practices standards and rationale — including A2A protocol model, OpenTelemetry-style traceability, security assumptions, risk-management documentation, and detailed A2A message patterns — see the standalone supporting document:

`ELIS_Agent_Communication_Skill_Best_Practices_Artifact_Exchange.md`

**Two-document model:**
- **`ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL.md`** — mandatory operational skill containing the enforceable rules agents must follow.
- **`ELIS_Agent_Communication_Skill_Best_Practices_Artifact_Exchange.md`** — separate supporting standards/rationale document. Not the active skill. Not a replacement for `SKILL.md`. Mandatory rules are duplicated/condensed into `SKILL.md`.

This skill file contains the mandatory operating rules. The best-practices document provides the rationale, extended examples, and standards alignment.

Recommended paths:
- Skill: `/home/samurai/.hermes/profiles/_shared/skills/ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL.md`
- Best-practices: `/home/samurai/.hermes/profiles/_shared/standards/ELIS_Agent_Communication_Skill_Best_Practices_Artifact_Exchange.md`
or `docs/operations/ELIS_Agent_Communication_Skill_Best_Practices_Artifact_Exchange.md`

## 8. Forbidden Actions via A2A or Discord

- Agent implementing AND validating the same artifact
- PM writing code or running implementation commands
- Advisor dispatching tasks to implementers
- Supervisor authoring governance packets
- GitHub performing validation or approval
- Scratch workspace as authoritative evidence store
- 0.0.0.0 or public host bindings
- Agents reading #elis-pe-reports history
- Treating #elis-pe-reports as memory, evidence, handoff, or authority source
- Agent-to-agent communication via Discord (Discord is human-facing)
- No GitHub operation is authorised by this skill installation packet
- No all-roster A2A production claim is made by this skill

## 9. Role Summary

| Role | A2A Capability | Kanban Authority | GitHub Authority |
|------|---------------|-----------------|------------------|
| PM | Sends requests, receives results | Creates/decomposes/tracks tasks | None |
| Advisor | Receives requests, sends results | Records verdicts in comments | None |
| Supervisor | Receives requests, sends results | Updates task state, records evidence | None |
| GitHub | Receives/sends (deferred) | References Kanban for coordination | Commits, PRs, merges (PO-approved) |
| Ideas | None (deferred) | Captures ideas via Kanban | None |