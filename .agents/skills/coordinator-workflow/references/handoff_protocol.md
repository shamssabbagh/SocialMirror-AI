# Shams-Malak Collaborative Handoff Protocol

This protocol defines the collaboration structure between **Shams** and **Malak** on the **SocialMirror-AI** project for Assignment 2.

---

## 1. Objectives of the Handoff Protocol
- Ensure seamless continuity between team members across asynchronous working sessions.
- Maintain a single source of truth regarding completed milestones, active drafting, and upcoming tasks.
- Eliminate duplicated effort and prevent contradictory modifications to LaTeX source files.

---

## 2. Central Artifacts
The Coordinator maintains two persistent documents in the `handoff/` directory:
1. `handoff/task_tracker.md`: The live status board categorized into:
   - `BACKLOG`: Scoped tasks awaiting assignment.
   - `IN_PROGRESS`: Currently active work, assigned to a specific author and agent.
   - `QA_REVIEW`: Drafts undergoing independent QA review.
   - `COMPLETED`: Finished and verified sections merged into LaTeX.
2. `handoff/SHAMS_MALAK_HANDOFF.md`: The formal session handoff log updated at the end of every work turn.

---

## 3. Handoff Structure & Required Fields
At the conclusion of any session led by Shams, the Coordinator must update `handoff/SHAMS_MALAK_HANDOFF.md` with the following structure:

```markdown
# Session Handoff: Shams -> Malak
- **Timestamp**: YYYY-MM-DD HH:MM
- **Current Milestone**: (e.g., M1 - Preparatory Architecture Specification)
- **Overall Page Count**: X pages (Compiled main.pdf)

### 1. Work Completed by Shams
- [List of concrete achievements, reviewed files, or merged sections]

### 2. Current State of the Workspace
- **Compilation Status**: Clean (Exit code 0) / Issues noted
- **Git Status**: Clean working tree, unpushed local changes only
- **Key Files Modified**: [List of modified files]

### 3. Immediate Next Tasks for Malak
- **Task A**: [Task description, target chapter/section, page budget]
  - *Prerequisites*: [Dependencies or references needed]
  - *Assigned Agents*: [e.g., Research Agent + Academic Writing Agent]
  - *Acceptance Criteria*: [Measurable standards for QA sign-off]
- **Task B**: [...]

### 4. Open Questions & Academic Decisions for the Team
- [Any design choices, instructor feedback, or notation decisions requiring joint review]
```
