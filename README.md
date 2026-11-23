# SocialMirror-AI

**AI-Powered Social Media and Psychological Well-Being – Preparatory Academic Report**  
*Course: "AI Agents & Vibe Coding" (Assignment 2) · University of Haifa*  
*Authors: Shams Sabbagh (Psychology) & Malak Farouja (Communication & Marketing)*  
*Equal Co-Authorship & Collaborative Academic Development*

---

## 1. Project Overview

**SocialMirror-AI** is a proposed AI-powered multi-agent research platform designed to investigate, model, and mitigate the adverse psychological impacts of algorithmic social media feeds on young adults (ages 15–26). 

The platform specifically addresses:
- **Algorithmic feed curation** and the systematic distortion toward idealized upward social comparison.
- **Influencer marketing mechanics**, commercial persuasion, and parasocial relationship dynamics.
- **Social comparison processes** (Festinger's Social Comparison Theory, upward vs. downward comparison, Higgins' Self-Discrepancy Theory).
- **Psychological well-being indicators** (State Self-Esteem [RSES], positive/negative affect balance [PANAS], digital burnout, and doomscrolling).

Rather than relying on primitive temporal restrictions (e.g., rigid screen-time limits that trigger psychological reactance), **SocialMirror-AI** introduces a collaborative multi-agent society (`ObserverAgent`, `AnalystAgent`, `ReflectorAgent`, and `InterventionAgent`) operating locally at the edge (`Local-First Privacy`) to provide metacognitive transparency and autonomy-supportive reflective scaffolding.

---

## 2. Multi-Agent System Architecture (.agents)

The academic report and system design were created through the orchestration of four specialized autonomous agents, each guided by dedicated skills and operating guidelines located in `.agents/`:

### 🤖 1. Academic Coordinator Agent (`academic-coordinator`)
- **Role**: Lead workflow coordinator and academic supervisor.
- **Responsibilities**: Orchestrates the multi-agent academic pipeline, enforces strict empirical evidence standards, monitors the page budget, ensures an equal collaborative voice across the entire document (without any internal division of writing), and coordinates handoffs and review loops.
- **Skill**: `.agents/skills/coordinator-workflow/SKILL.md`

### 🔍 2. Academic Research Agent (`academic-researcher`)
- **Role**: Evidence discovery, scientific audit, and psychometrics specialist.
- **Responsibilities**: Curates and audits peer-reviewed academic literature across social psychology, computational social science, and multi-agent AI. Formulates empirical dossiers, verifies 29 BibTeX citations with complete DOIs, and strictly differentiates correlation from causation (addressing the Twenge vs. Orben/Przybylski debate).
- **Skill**: `.agents/skills/academic-research/SKILL.md`

### ✍️ 3. Academic Writing Agent (`academic-writer`)
- **Role**: Scholarly multilingual author and mathematical modeling specialist.
- **Responsibilities**: Drafts rigorous academic text in formal scientific Hebrew with accurate English academic terminology. Enforces conceptual demarcation between established literature and our proposed architecture, and formalizes mathematical state vector dynamics ($\mathbf{w}(t) = \langle S(t), \mathbf{A}(t), D(t) \rangle$).
- **Skill**: `.agents/skills/academic-writing/SKILL.md`

### 🎨 4. Design & Typesetting Agent (`design-agent`)
- **Role**: Visual design system and LaTeX typesetter.
- **Responsibilities**: Implements the **SocialMirror Premium Theme** across all 53 pages. Designs publication-grade TikZ vector diagrams (Figures 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 4.1, 4.2, 5.1, 6.1), booktabs comparative matrices (Tables 2.1, 2.2, 3.1, 5.1, 6.1), and ensures bidirectional typography harmony (Hebrew RTL with English LTR).
- **Skill**: `.agents/skills/socialmirror-premium-theme/SKILL.md`

---

## 3. Academic Report Structure (53 Pages)

The compiled preparatory academic report (`report/main.pdf`) spans **53 pages** and contains:

| Section / Chapter | Title | Scope & Key Figures / Tables |
| :--- | :--- | :--- |
| **Title Page** | Single-Page Academic Cover | Verified University of Haifa header, co-authors, and framed artwork |
| **Front Matter** | Executive Summary & Acronyms | Executive summary, terminology dictionary, TOC, LOF (12 figures), LOT (5 tables) |
| **Chapter 1** | מבוא, הגדרת הבעיה והקשר חברתי-טכנולוגי | Socio-technological context, stakeholders ecosystem (**Fig. 1.1**), mediating pathway (**Fig. 1.2**), research questions & agent mapping (**Fig. 1.3**) |
| **Chapter 2** | סקירת ספרות ומסגרת תיאורטית | Festinger's SCT (**Fig. 2.1**), self-discrepancy, multivariate model (**Fig. 2.2**), psychometric conversion (**Tab. 2.1**), triple feedback loop (**Fig. 2.3**), literature matrix (**Tab. 2.2**) |
| **Chapter 3** | פערי מחקר, ביקורת כלים קיימים והמסגרת המושגית | Empirical controversy, effect size comparison chart (**Fig. 3.1**), digital wellbeing tool critique (**Tab. 3.1**), MAS paradigm, information-flow architecture (**Fig. 3.2**) |
| **Chapter 4** | ארכיטקטורה מפורטת ועיצוב סוכני ה־AI | Core principles, 3-layer topology (**Fig. 4.1**), JSON-RPC protocol, agent specifications, mathematical state dynamics, Cognitive Mirror Dashboard wireframe (**Fig. 4.2**) |
| **Chapter 5** | מתודולוגיית מחקר, מערך סימולציה ומדדי הערכה | Controlled simulation justification, 20 personas matrix (**Tab. 5.1**), 3 feed conditions, simulation pipeline flowchart (**Fig. 5.1**), DMR/reactance metrics, IRB ethics |
| **Chapter 6** | היתכנות טכנולוגית, מפת דרכים ומטריצת סיכונים | Local SLM stack (Llama-3/Phi-3, LangGraph, ChromaDB), 5-phase Gantt chart (**Fig. 6.1**), engineering risk matrix (**Tab. 6.1**), Haifa computational resources |
| **Chapter 7** | סיכום, תובנות ומבט לעתיד | Integrative synthesis, computational social science contributions, human agency and algorithmic responsibility |
| **Appendices** | נספחים מחקריים | App. A: System prompts for all 4 agents; App. B: Validated Hebrew RSES & PANAS scales; App. C: IRB ethics compliance checklist |
| **Bibliography** | רשימת מקורות אקדמיים | 29 peer-reviewed citations formatted in IEEE style |

---

## 4. Repository Structure

```text
SocialMirror-AI/
├── .agents/
│   ├── agents/
│   │   ├── academic-coordinator.md
│   │   ├── academic-researcher.md
│   │   ├── academic-writer.md
│   │   └── design-agent.md
│   └── skills/
│       ├── coordinator-workflow/SKILL.md
│       ├── academic-research/SKILL.md
│       ├── academic-writing/SKILL.md
│       └── socialmirror-premium-theme/SKILL.md
├── report/
│   ├── main.tex                    # Master XeLaTeX document
│   ├── preamble.tex                # Color palette, fonts, polyglossia, TikZ & tcolorbox styling
│   ├── macros.tex                  # Notation, mathematical operators, agent role macros
│   ├── references.bib              # 29 peer-reviewed academic citations
│   ├── compile.ps1                 # Automated 4-pass compilation script (XeLaTeX + BibTeX)
│   ├── assets/
│   │   └── socialmirror-cover.png  # Official project cover illustration
│   └── chapters/
│       ├── 00_frontmatter.tex      # Abstract, glossary, TOC, LOF, LOT
│       ├── 01_introduction.tex     # Chapter 1
│       ├── 02_literature_review.tex# Chapter 2
│       ├── 03_research_gaps_and_conceptual_system.tex # Chapter 3
│       ├── 04_system_architecture.tex # Chapter 4
│       ├── 05_methodology.tex      # Chapter 5
│       ├── 06_implementation_roadmap.tex # Chapter 6
│       ├── 07_conclusion.tex       # Chapter 7
│       └── 08_appendices.tex       # Appendices A, B, C
├── .gitignore                      # Git ignore rules for LaTeX auxiliary files
└── README.md                       # Collaborative project documentation
```

---

## 5. How to Compile the LaTeX Report

### Prerequisites
- **XeLaTeX**: Required for bidirectional Unicode support (Hebrew RTL with English LTR) and native system fonts (Arial, Courier New).
- **BibTeX**: Required for IEEEtran academic citation processing.
- Recommended distribution: **MiKTeX** (Windows) or **TeX Live** (Cross-platform).

### Compilation Command
From PowerShell, execute the included compilation helper:
```powershell
cd report
powershell -ExecutionPolicy Bypass -File compile.ps1
```

The script runs a robust 4-pass build sequence:
1. `xelatex main.tex` (initial parse and label extraction)
2. `bibtex main` (process all 29 citations)
3. `xelatex main.tex` (resolve cross-references, TOC, LOF, LOT)
4. `xelatex main.tex` (finalize layout and page numbering)

The compiled PDF is generated at `report/main.pdf` (~625 KB, 53 pages).

---

## 6. Academic & Version Control Integrity

- **Strict Git Constraint**: Per project protocol, no commits, branches, or pushes to remote GitHub repositories are made without explicit co-author approval.
- **Collaborative Voice**: The report reflects the equal, joint intellectual contribution of both students—Shams Sabbagh and Malak Farouja—bridging cognitive psychology, social communication, and artificial intelligence.
