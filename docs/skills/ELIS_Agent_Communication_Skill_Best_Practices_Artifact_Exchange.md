# ELIS Agent-to-Agent Communication Skill — Best Practices and Artifact Exchange Model

**Purpose:** Define the best-practice and standards-aligned requirements that `ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL` should comply with, including how ELIS agents should exchange implemented and validated artifacts.

**Context:** This document extends the proposed ELIS agent-to-agent communication skill by adding standards-aligned requirements for A2A protocol use, Kanban authority, artifact manifests, validation handoffs, traceability, and safe publication workflows.

---

## 1. Standards and Best-Practice Anchors

The skill should comply with protocol, governance, security, traceability, and software-delivery best practices. The implementation packet is already directionally strong, but the final skill should be stricter about artifact exchange and authority boundaries.

### 1.1 A2A Protocol Model

The skill should follow A2A's distinction between **messages**, **tasks**, and **artifacts**. A2A is designed around clients sending messages to initiate tasks that may produce artifacts; artifacts are tangible deliverables and may contain parts such as text, files, or structured data.

For ELIS, that means:

```text
A2A message = request/result transport
Kanban task = authoritative work state
Artifact = durable implementation/validation output
```

The skill should not treat the A2A message itself as the durable artifact unless the message contains only a reference to a durable artifact.

### 1.2 Kanban as Authoritative Workflow and Evidence

The packet correctly states that Kanban is the single source of truth for task lifecycle and evidence, and that every operational A2A exchange must reference a Kanban task.

This should remain a hard rule:

```text
No Kanban task reference → no operational A2A action.
```

### 1.3 OpenTelemetry-Style Traceability

Agent exchanges should use consistent correlation identifiers so requests, results, logs, artifacts, and validation can be linked across systems. OpenTelemetry's context propagation model exists to correlate traces, metrics, and logs across process and network boundaries.

For ELIS, use:

```text
elis_pe_ref
elis_board
elis_task_ref
elis_parent_task_ref
elis_message_id
elis_context_id
elis_artifact_id
elis_authoritative_record
elis_correlation_id
```

The skill should require these identifiers for any artifact-producing exchange.

### 1.4 Security and Policy Enforcement

The skill should encode zero-trust assumptions:

```text
Every message is authenticated by role metadata.
Every route is allowlisted.
Every action is scoped to a Kanban task.
Every artifact is referenced, validated, and versioned.
```

ELIS should keep explicit route allowlists, rejection codes, timestamp governance, and evidence validation.

### 1.5 Risk-Management Documentation

The skill should support systematic documentation, monitoring, accountability, and continual risk management.

For ELIS, every artifact exchange should produce:

```text
who requested it
who produced it
who validated it
what changed
where evidence lives
what risks remain
who approved next action
```

---

## 2. Best-Practice Artifact Exchange Model

For ELIS, agents should **not exchange large artifacts directly inside A2A messages** except for very small structured summaries. The best practice is:

```text
A2A carries artifact manifests and handoff notices.
Kanban, repository files, or artifact directories store the artifact.
Validator reads the artifact from a durable location.
#elis-pe-reports notifies PO that an artifact event occurred.
```

### 2.1 Recommended Artifact Lifecycle

```text
1. PM creates/assigns Kanban task.
2. Implementer produces artifact in durable location.
3. Implementer records artifact manifest in Kanban.
4. Implementer sends implementation_result to PM via A2A.
5. PM creates validation task.
6. Validator validates artifact from durable location.
7. Validator records validation verdict in Kanban.
8. Validator sends validation_result to PM via A2A.
9. Agent posts compact event to #elis-pe-reports.
10. PO approves closeout/GitHub/publication if needed.
```

### 2.2 Artifact Exchange Rule

Add this rule to the skill:

```text
ELIS agents must exchange implemented or validated artifacts by reference, not by pasting large artifact contents into A2A or Discord. The artifact must be stored in a durable location and accompanied by an artifact manifest. A2A messages carry the manifest reference, summary, verdict, and next action.
```

---

## 3. Artifact Storage Locations

Use this hierarchy:

| Artifact Type | Preferred Storage |
|---|---|
| Source code change | Git working tree / branch / PR |
| Validation report | Repo file or Kanban board artifact |
| Runtime evidence log | Durable evidence path referenced in Kanban |
| Gate packet | Kanban task/comment body |
| Implementation report | Kanban comment plus optional artifact file |
| Published docs | GitHub repo |
| Temporary smoke output | Evidence file path + hash + summary |
| Large logs | Artifact file, not A2A/Discord body |

Avoid scratch-only storage. Scratch workspace files are not durable evidence unless copied or referenced into an authoritative Kanban artifact or repository path.

---

## 4. Required Artifact Manifest

Every implementation or validation result should include an `artifact_manifest` object or a durable reference to one:

```json
{
  "artifact_id": "artifact-uuid-or-task-derived-id",
  "artifact_type": "implementation|validation_report|evidence_log|github_pr|gate_packet|runtime_check",
  "producer_role": "supervisor",
  "validator_role": "advisor",
  "kanban_board": "elis-a2a-implementation",
  "kanban_task": "t_xxxxxxxx",
  "pe_ref": "PE-...",
  "storage_location": "kanban://board/task/comment or file path or PR URL",
  "files": [
    {
      "path": "elis/a2a/pm/executor.py",
      "status": "modified",
      "sha256": "optional-if-file"
    }
  ],
  "summary": "What the artifact contains",
  "validation_status": "PENDING|PASS|FAIL|BLOCKED",
  "created_at": "2026-07-02T12:00:00Z",
  "authoritative_record": "Kanban task/comment or PR URL"
}
```

### 4.1 Required Manifest Fields

| Field | Required | Purpose |
|---|---:|---|
| `artifact_id` | Yes | Stable artifact identifier |
| `artifact_type` | Yes | Classifies the artifact |
| `producer_role` | Yes | Identifies who created it |
| `validator_role` | When applicable | Identifies who validated it |
| `kanban_board` | Yes | Board context |
| `kanban_task` | Yes | Authoritative task context |
| `pe_ref` | When PE-scoped | Governance traceability |
| `storage_location` | Yes | Durable artifact location |
| `files` | When file-based | Exact file manifest |
| `summary` | Yes | Compact artifact description |
| `validation_status` | Yes | Current validation state |
| `created_at` | Yes | UTC timestamp |
| `authoritative_record` | Yes | Kanban/GitHub evidence reference |

---

## 5. A2A Message Patterns for Artifacts

### 5.1 Implementer → PM

Metadata pattern:

```json
{
  "elis_sender_role": "supervisor",
  "elis_message_type": "implementation_result",
  "elis_task_ref": "t_123",
  "elis_pe_ref": "PE-OPS-...",
  "elis_authoritative_record": "kanban://elis-a2a-implementation/t_123/comment/45",
  "artifact_manifest_ref": "kanban://elis-a2a-implementation/t_123/artifacts/manifest.json"
}
```

Compact message text:

```text
Implementation complete. Artifact manifest recorded at <reference>. Ready for Advisor validation.
```

### 5.2 Advisor → PM

Metadata pattern:

```json
{
  "elis_sender_role": "advisor",
  "elis_message_type": "validation_result",
  "elis_task_ref": "t_456",
  "elis_pe_ref": "PE-OPS-...",
  "elis_result_type": "validation_report",
  "elis_authoritative_record": "kanban://elis-a2a-implementation/t_456/comment/78",
  "validated_artifact_ref": "kanban://elis-a2a-implementation/t_123/artifacts/manifest.json",
  "verdict": "PASS"
}
```

Compact message text:

```text
Validation PASS. Artifact validated against acceptance criteria. See authoritative record <reference>.
```

---

## 6. Rules for Implemented Artifacts

When an agent implements something, it must report:

```text
implementation task ID
parent PE/task
files changed
files explicitly not changed
commands/checks run
evidence path
artifact manifest
known deviations
rollback/cleanup state
next required actor
```

The implementer must **not**:

```text
validate its own artifact
push to GitHub unless acting as ELIS GitHub under PO-approved handoff
paste large logs into A2A or Discord
use scratch files as final evidence
claim production without validation
```

---

## 7. Rules for Validated Artifacts

When Advisor validates, it must report:

```text
validated artifact reference
validation task ID
verdict
evidence inspected
acceptance criteria mapping
defects/blockers
out-of-scope actions
residual risks
next required action
```

Advisor must **not**:

```text
fix the artifact
mutate implementation files
approve merge unless explicitly authorised
infer evidence from #elis-pe-reports
treat A2A message content as sufficient if durable artifact is missing
```

---

## 8. Recommended Artifact States

Use a small state model:

```text
DRAFT
IMPLEMENTED
IMPLEMENTATION_EVIDENCE_READY
VALIDATION_READY
VALIDATED_PASS
VALIDATED_FAIL
BLOCKED
SUPERSEDED
PUBLISHED
ROLLED_BACK
```

### 8.1 State Semantics

| State | Meaning |
|---|---|
| `DRAFT` | Artifact is being prepared and is not ready for validation |
| `IMPLEMENTED` | Implementation exists but evidence may not yet be complete |
| `IMPLEMENTATION_EVIDENCE_READY` | Implementation evidence and manifest are ready |
| `VALIDATION_READY` | Validator can inspect artifact and evidence |
| `VALIDATED_PASS` | Independent validation passed |
| `VALIDATED_FAIL` | Validation found defects |
| `BLOCKED` | Missing prerequisite, evidence, permission, or decision |
| `SUPERSEDED` | Replaced by later artifact or task |
| `PUBLISHED` | Published through GitHub or other approved durable channel |
| `ROLLED_BACK` | Rolled back or deactivated under approved rollback path |

---

## 9. Checklist for the Skill

The final `ELIS_AGENT_TO_AGENT_COMMUNICATION_SKILL` should comply with these requirements:

| Area | Requirement |
|---|---|
| A2A | Use v1.0 header, `SendMessage`, valid metadata, role allowlists |
| Kanban | Every operational A2A message references a task |
| Discord | `#elis-pe-reports` is append-only telemetry only |
| Artifacts | Exchange manifests/references, not large payloads |
| Validation | Independent validator, no self-validation |
| Traceability | Correlation IDs and authoritative record references |
| Security | No secrets, no external exposure, no unauthorised routes |
| GitHub | Only ELIS GitHub acts after PO-approved handoff |
| PO control | PO approves gates, exceptions, production claims, merge |
| Observability | Compact event reports plus durable evidence |
| Cleanup | Rollback and residual-risk reporting |

---

## 10. Recommended Correction to the Packet

Add a new section:

```text
16. Artifact Exchange and Validation
```

with these subsections:

```text
16.1 Artifact exchange principle
16.2 Durable storage locations
16.3 Required artifact manifest
16.4 Implementation-result handoff
16.5 Validation-result handoff
16.6 Artifact states
16.7 Forbidden artifact practices
16.8 GitHub publication handoff
```

Then renumber the current `AGENTS.md Cross-References` and `Install Location` sections.

---

## 11. Proposed Section Text for `SKILL.md`

### 16. Artifact Exchange and Validation

ELIS agents must exchange implemented or validated artifacts by reference, not by pasting large artifact contents into A2A or Discord. The artifact must be stored in a durable location and accompanied by an artifact manifest.

A2A carries artifact manifests, summaries, verdicts, and handoff notices. Kanban, repository files, board artifact directories, or GitHub PRs store durable artifacts. `#elis-pe-reports` only notifies PO that an artifact event occurred.

#### 16.1 Durable Storage Locations

- Source code change → Git working tree / branch / PR.
- Validation report → repo file or Kanban board artifact.
- Runtime evidence log → durable evidence path referenced in Kanban.
- Gate packet → Kanban task/comment body.
- Implementation report → Kanban comment plus optional artifact file.
- Published docs → GitHub repo.
- Large logs → artifact file, not A2A or Discord body.

Scratch workspace files are not final durable evidence unless copied or referenced into an authoritative Kanban artifact or repository path.

#### 16.2 Required Artifact Manifest

Every implementation or validation result must include or reference an artifact manifest with:

- `artifact_id`
- `artifact_type`
- `producer_role`
- `validator_role`, if applicable
- `kanban_board`
- `kanban_task`
- `pe_ref`
- `storage_location`
- `files`
- `summary`
- `validation_status`
- `created_at`
- `authoritative_record`

For file artifacts, include path, status, and SHA-256 where practical.

#### 16.3 Implementation-Result Handoff

Supervisor or an implementer must report:

- implementation task ID;
- parent PE/task;
- files changed;
- files explicitly not changed;
- commands/checks run;
- evidence path;
- artifact manifest reference;
- known deviations;
- rollback/cleanup state;
- next required actor.

Implementers must not validate their own artifacts.

#### 16.4 Validation-Result Handoff

Advisor must report:

- validated artifact reference;
- validation task ID;
- verdict;
- evidence inspected;
- acceptance criteria mapping;
- defects/blockers;
- out-of-scope actions;
- residual risks;
- next required action;
- authoritative Kanban record.

Advisor must validate from durable artifacts, not from Discord or uncited A2A message content.

#### 16.5 Artifact States

Use this state model:

- `DRAFT`
- `IMPLEMENTED`
- `IMPLEMENTATION_EVIDENCE_READY`
- `VALIDATION_READY`
- `VALIDATED_PASS`
- `VALIDATED_FAIL`
- `BLOCKED`
- `SUPERSEDED`
- `PUBLISHED`
- `ROLLED_BACK`

#### 16.6 Forbidden Artifact Practices

Prohibited:

- pasting large logs into A2A;
- pasting large logs into `#elis-pe-reports`;
- treating Discord as evidence;
- treating A2A message body as the artifact when a durable artifact is required;
- using scratch-only files as final evidence;
- self-validation;
- GitHub publication without PO-approved ELIS GitHub handoff;
- production claims without validation and PO approval.

#### 16.7 GitHub Publication Handoff

GitHub publication is a separate step after validation and PO approval.

Required handoff fields:

- target repo;
- target branch;
- exact file manifest;
- excluded files;
- commit message;
- PR title/body;
- evidence references;
- diff-bound checks;
- no-merge-without-PO rule.

---

## 12. Bottom Line

The best-practice approach is:

```text
Agents exchange artifact references and manifests over A2A.
Kanban stores authoritative task/evidence state.
Repo/GitHub stores durable source artifacts.
Advisor validates from durable artifacts, not from chat.
#elis-pe-reports tells PO what happened, without becoming evidence.
```

That should be a central section of the skill before implementation.

