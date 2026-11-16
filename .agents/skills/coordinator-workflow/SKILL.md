---
name: coordinator-workflow
description: >-
  Orchestrates the multi-agent academic workflow for SocialMirror-AI Assignment 2 (University of Haifa).
  Use this skill to delegate tasks among specialized agents, track task state and milestones, require
  empirical evidence for scientific claims, route drafts through independent QA, manage handoffs between
  Shams and Malak, and enforce strict execution truthfulness and Git safety.
---

# Coordinator Workflow Skill

This skill defines the operational runbook for the **Coordinator Agent** in orchestrating the 7-agent academic team for the **SocialMirror-AI** preparatory report.

---

## 1. Principles & Inviolable Rules

1. **Execution Truthfulness**: Never state or imply that an agent has executed or completed work unless it genuinely ran and its output was verified.
2. **Evidence Gate**: Every claim regarding psychological effects, algorithmic mechanics, or empirical trends must cite primary literature from `report/references.bib`.
3. **Mandatory QA Gate**: No drafted chapter or section may be marked complete without passing review by the Independent QA Agent.
4. **Handoff Accountability**: All work done by Shams must be tracked, and next steps for Malak must have clear acceptance criteria in `handoff/SHAMS_MALAK_HANDOFF.md`.
5. **Git Safety**: Never push to remote or create remote repositories without explicit user instruction.

---

## 2. Multi-Agent Roster & Delegation Protocol

The Coordinator delegates work according to the defined specializations:

| Agent Name | Primary Responsibility | Input Requirements | Output Deliverable |
| :--- | :--- | :--- | :--- |
| **Research Agent** | Literature search, empirical findings, BibTeX entries | Topic / RQ focus | Verified citations, summaries, BibTeX keys |
| **Academic Writing Agent** | Scholarly narrative, drafting sections | Research evidence, outline | Polished LaTeX prose adhering to page targets |
| **System Architecture Agent** | Agent society topology, math models, pipelines | System philosophy, RQs | Formal specs, state equations, flow diagrams |
| **LaTeX Agent** | Typesetting, table/figure layout, compilation | Approved draft content | Clean compilation (0 errors, 0 warnings) |
| **Requirements Verification Agent** | Assignment 2 rubric check, page-budget audit | Report draft, course rubric | Compliance scorecard, missing item alerts |
| **Independent QA Agent** | Adversarial review, fact-checking, citation audit | Section drafts | QA Audit report: Pass / Revise with notes |

*Detailed agent contracts are documented in [agent_roster.md](./references/agent_roster.md).*

---

## 3. Step-by-Step Coordination Procedure

### Step 1: Task Scoping & Planning
1. Identify the active deliverable (e.g., Chapter 1, Chapter 2, Architecture Diagram, etc.).
2. Determine page target allocation based on the 40-page master budget in `README.md`.
3. Log the task as `IN_PROGRESS` in `handoff/task_tracker.md`.

### Step 2: Research Evidence Retrieval
1. Task the **Research Agent** with retrieving empirical studies (e.g., Festinger, Twenge, Primack, Lou & Yuan, Park et al.).
2. Verify that all returned citations are real, peer-reviewed, and added to `report/references.bib`.
3. *Evidence Rule*: Reject any draft relying on unverified assertions or synthetic citations.

### Step 3: Drafting & Technical Formulation
1. Dispatch the researched brief to the **Academic Writing Agent** (for theoretical/contextual chapters) or **System Architecture Agent** (for technical/mathematical chapters).
2. Ensure mathematical formulations (e.g., well-being state vector $\mathbf{w}_t$, comparison score $\mathcal{S}_{\text{comp}}$) match notation defined in `report/macros.tex`.

### Step 4: Independent QA Review Routing
1. Forward the raw draft to the **Independent QA Agent**.
2. Require QA evaluation on three criteria:
   - **Citation & Fact Accuracy**: Does every claim point to a valid BibTeX reference?
   - **Theoretical Rigor**: Are Festinger's SCT and psychological constructs correctly applied?
   - **Tone & Redundancy**: Is the prose academic, concise, and non-repetitive?
3. If QA returns `REVISION_REQUIRED`, send feedback to the drafting agent before accepting.

### Step 5: LaTeX Integration & Build Audit
1. Direct the **LaTeX Agent** to incorporate the approved section into the modular chapter file in `report/chapters/`.
2. Execute the verification build via `report/compile.ps1` (or multi-pass `pdflatex` + `bibtex`).
3. Ensure exit code is 0, references are resolved, and no critical warnings or overfull boxes exist.

### Step 6: Shams-to-Malak Handoff Update
1. Update `handoff/task_tracker.md` to reflect completed items.
2. Update `handoff/SHAMS_MALAK_HANDOFF.md` with:
   - What Shams completed in the current session.
   - Current compilation state (page count, exit code).
   - Specific tasks queued for Malak with clear guidelines and prerequisites.

---

## 4. Verification & Health Checks

To verify that the Coordinator workflow is healthy:
1. Verify `handoff/task_tracker.md` reflects current status.
2. Verify `report/main.pdf` compiles cleanly with exit code 0.
3. Verify that `git status` shows clean local tracking without unapproved pushes.
