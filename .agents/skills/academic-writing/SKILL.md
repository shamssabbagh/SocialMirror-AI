---
name: academic-writing
description: >-
  Operational guidelines and stylistic standards for authoring the SocialMirror-AI preparatory report.
  Covers chapter structural templates, evidence integration protocols, LaTeX macro usage,
  citation syntax, formal academic register, Independent QA routing, and collaborative handoff tracking.
---

# Academic Writing Skill

This skill defines the operational runbook and scientific composition guidelines for the **Academic Writing Agent** authoring the **SocialMirror-AI** preparatory report.

---

## 1. Academic Writing Workflow

The Academic Writing Agent executes every writing task in five distinct phases:

```text
[Research Evidence Dossier]
            │
            ▼
Phase 1: Structural Scoping & Page Budgeting
            │
            ▼
Phase 2: Scholarly Composition & Evidence Synthesis
            │
            ▼
Phase 3: Self-Audit & LaTeX Compliance Check
            │
            ▼
Phase 4: Independent QA Routing & Revision
            │
            ▼
Phase 5: Handoff Documentation & State Logging (Shams -> Malak)
```

---

## 2. Chapter Structure Guidelines

To achieve the targeted ~40-page report depth, every chapter must be composed using standardized academic sub-structures:

### 1. Chapter Opening Protocol
- **Epigraph / Motivator (Optional)**: Brief theoretical touchstone.
- **Introductory Narrative (1–2 paragraphs)**: Situate the chapter in the broader discourse of SocialMirror-AI. State the chapter's objectives, central thesis, and outline the upcoming sections.

### 2. Analytical Section Structure
- **Topic Sentence**: Clear, authoritative declaration of the paragraph's theoretical or technical claim.
- **Evidence Presentation**: Integrate empirical findings or architectural logic (citing primary literature).
- **Critical Evaluation**: Analyze caveats, boundary conditions, or psychological implications.
- **Architectural Translation**: Explicitly connect the finding to SocialMirror-AI's multi-agent mechanisms (e.g., how upward comparison informs `AnalystAgent` heuristics).
- **Transitional Concluding Sentence**: Create logical flow to the subsequent paragraph or section.

### 3. Chapter Closing Protocol
- **Summary of Findings**: Synthesize the core conceptual and technical takeaways established in the chapter.
- **Forward-Looking Transition**: Provide a 1-paragraph bridge leading directly into the questions addressed by the next chapter.

---

## 3. Evidence Integration Rules

1. **Lead with Ideas, Not Author Names**:
   - *Weak*: "Twenge et al. (2018) wrote a paper that showed adolescents are depressed."
   - *Scholarly*: "The rapid proliferation of algorithmic screen time has coincided with marked escalations in depressive affect and self-reported loneliness among young cohorts \cite{twenge2018increases}."
2. **Synthesize Multiple Perspectives**:
   - Cluster complementary or contrasting empirical studies:
     *"While classical comparison theory posits that upward comparisons predominantly trigger contrast effects and self-discrepancy \cite{festinger1954theory, appels2020social}, emerging digital media research demonstrates that source perceived closeness and authenticity can mediate whether the comparison fosters inspiration or acute distress \cite{fardouly2018instagram, lou2019influencer}."*
3. **Statistical Precision**:
   - When citing empirical studies, specify sample size $N$ and design context when relevant to demonstrate academic rigor:
     *"In a cross-sectional investigation of $N = 276$ young women, Fardouly et al. \cite{fardouly2018instagram} identified that appearance comparison to macro-influencer and celebrity targets exerted significantly stronger mediational effects on negative body evaluations than comparisons to familiar peer acquaintances."*
4. **Zero Fabrication**:
   - If an empirical datum (e.g., sample size or effect size) is not explicitly present in the Research Agent's dossier, describe the conceptual finding qualitatively without inventing quantitative metrics.

---

## 4. Citation & LaTeX Formatting Standards

- **Citation Macros**:
  - Parenthetical / Narrative citations: Use standard LaTeX `\cite{key}` or `\cite{key1, key2}`.
  - Author-year phrasing: When citing narrative subjects, write:
    `Festinger \cite{festinger1954theory} originally posited...`
- **System & Agent Macro Consistency**:
  - Always use defined macros from `report/macros.tex`:
    - `\projectname{}` $\rightarrow$ **SocialMirror-AI**
    - `\agentObserver{}` $\rightarrow$ `ObserverAgent`
    - `\agentAnalyst{}` $\rightarrow$ `AnalystAgent`
    - `\agentReflector{}` $\rightarrow$ `ReflectorAgent`
    - `\agentInterventionist{}` $\rightarrow$ `InterventionAgent`
    - `$\wellbeingVector$` $\rightarrow$ $\mathbf{w}_t$
    - `$\comparisonScore$` $\rightarrow$ $\mathcal{S}_{\text{comp}}$
    - `$\exposureIndex$` $\rightarrow$ $\mathcal{E}_{\text{inf}}$
- **Typography & Clean Formatting**:
  - Use em-dashes (`---`) with no surrounding spaces or en-dashes (`--`) with spaces.
  - Enclose mathematical terms within inline math mode (`$...$`).
  - Cross-reference sections and chapters using `\Cref{sec:...}` or `\Cref{chap:...}`.

---

## 5. Scientific Writing Standards

| Dimension | Acceptable Academic Standard | Prohibited Informal Anti-Pattern |
| :--- | :--- | :--- |
| **Tone** | Objective, analytical, formal, authoritative | Conversational, promotional, colloquial ("cool", "game-changer") |
| **Perspective** | Academic third-person or scholarly plural ("we formulate", "the system implements") | First-person singular ("I think", "I built") |
| **Claims** | Nuanced, contingent, empirical ("evidence suggests", "is correlated with") | Sweeping, unhedged absolutes ("social media destroys everyone's brain") |
| **System Status** | Clearly designated as a proposed preparatory framework | Described as an already deployed, commercial product with millions of users |

---

## 6. Review & Revision Checklist (Pre-QA Audit)

Before dispatching drafted prose to the Independent QA Agent:
- [ ] Every scientific claim has an accompanying `\cite{...}` referencing `report/references.bib`.
- [ ] The boundary between existing research findings and the proposed SocialMirror-AI platform is unmistakable.
- [ ] The drafted section adheres to the target word/page count allocated in the master budget.
- [ ] All agent designations, mathematical variables, and project names use the standardized macros.
- [ ] There are no hardcoded bullet dumps; points are developed into complete, cohesive paragraphs.
- [ ] No citations, sample statistics, or author names are fabricated.

---

## 7. Collaboration & Handoff Logging Procedure

At the conclusion of each writing block:
1. Record drafted sections, estimated word count, and paragraph counts in `handoff/task_tracker.md`.
2. Update `handoff/SHAMS_MALAK_HANDOFF.md` with:
   - Specific sub-sections drafted by Shams.
   - Identified gaps or citation needs for subsequent sections.
   - Clear instructions for Malak on which chapter or sub-section to draft next.
