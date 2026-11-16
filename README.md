# SocialMirror-AI

**AI-Powered Social Media and Psychological Well-Being – Preparatory Project Report**  
*AI Agents Course (Assignment 2) · University of Haifa*  
*Author: Shams Sabbagh*

---

## 1. Project Overview

**SocialMirror-AI** is a proposed AI-powered multi-agent research platform designed to investigate, model, and mitigate the adverse psychological impacts of algorithmic social media feeds. The system specifically explores the intersection of:
- **Algorithmic feed curation** and continuous lifestyle exposure.
- **Influencer marketing mechanics**, commercial persuasion, and parasocial relationship dynamics.
- **Social comparison processes** (Festinger's Social Comparison Theory, upward vs. downward comparison, self-discrepancy).
- **Psychological well-being indicators** (self-esteem, positive/negative affect balance, digital fatigue).

Rather than relying on primitive temporal interventions (e.g., rigid screen-time limits), **SocialMirror-AI** introduces a collaborative multi-agent architecture (\agentObserver{}, \agentAnalyst{}, \agentReflector{}, and \agentInterventionist{}) that provides context-aware, metacognitive awareness and non-intrusive reflective scaffolding for users.

---

## 2. Workspace Organization

The workspace is structured to support the research, drafting, and compilation of a professional **40-page preparatory academic report** in LaTeX:

```text
SocialMirror-AI/
├── .gitignore                      # Comprehensive LaTeX, OS, and Python ignore rules
├── README.md                       # Project documentation and workspace guide
└── report/                         # 40-page LaTeX preparatory report workspace
    ├── main.tex                    # Master LaTeX document combining all chapters
    ├── preamble.tex                # Package configurations, typography, hyperlinks, callout boxes
    ├── macros.tex                  # Project metadata, notation, and agent role definitions
    ├── references.bib              # BibTeX database with foundational psychology and AI citations
    ├── compile.ps1                 # Automated PowerShell script for local compilation
    ├── chapters/                   # Modular chapter source files
    │   ├── 00_abstract.tex         # Abstract & Executive Summary (~2 pages)
    │   ├── 01_introduction.tex     # Introduction & Problem Formulation (~5 pages)
    │   ├── 02_literature_review.tex# Literature Review & Foundations (~8 pages)
    │   ├── 03_system_architecture.tex # Architecture & Multi-Agent Design (~10 pages)
    │   ├── 04_methodology.tex      # Methodology & Simulation Design (~7 pages)
    │   ├── 05_implementation_roadmap.tex # Feasibility & Tech Roadmap (~5 pages)
    │   ├── 06_conclusion.tex       # Conclusion & Future Outlook (~2 pages)
    │   └── 07_appendices.tex       # Prompts, Scales, Ethics Protocol (~3-4 pages)
    ├── figures/                    # Diagrams, architecture flowcharts, and plots (.gitkeep)
    └── tables/                     # Standalone LaTeX tables and matrices (.gitkeep)
```

---

## 3. Preparatory Report Structure & Page Budget

The preparatory report is planned for a standard **40–45 page** academic deliverable:

| Section / Chapter | Title | Estimated Target | Core Content / Scope |
| :--- | :--- | :---: | :--- |
| **Front Matter** | Title Page, Abstract, ToC, LoF, LoT, Acronyms | ~3–4 pages | Academic formatting, executive summary, notation table |
| **Chapter 1** | Introduction & Problem Formulation | ~5 pages | Digital media context, influencer economy, problem statement, RQs |
| **Chapter 2** | Literature Review & Foundations | ~8 pages | Festinger's SCT, influencer persuasion, well-being scales, agent literature |
| **Chapter 3** | System Architecture & Agent Design | ~10 pages | Multi-agent society, Observer, Analyst, Reflector, Interventionist |
| **Chapter 4** | Methodological Framework & Simulation | ~7 pages | Synthetic personas, feed generation, evaluation metrics, IRB ethics |
| **Chapter 5** | Implementation Roadmap & Feasibility | ~5 pages | Tech stack (LLMs, vector DB, orchestration), risk matrix, timeline |
| **Chapter 6** | Conclusion & Future Outlook | ~2 pages | Synthesis, expected impact, future perspectives |
| **Back Matter** | References & Appendices | ~3–4 pages | BibTeX references, prompt templates, psychological scales |
| **Total** | **Target Scope** | **~40–45 pages** | **Comprehensive Academic Preparatory Report** |

---

## 4. How to Compile the LaTeX Report

### Option A: Local Compilation (Windows with MiKTeX / TeX Live)
Run the included PowerShell compilation helper from the `report/` folder:
```powershell
cd report
.\compile.ps1
```
Or directly using standard `latexmk` / `pdflatex`:
```powershell
latexmk -pdf -interaction=nonstopmode main.tex
```

### Option B: Visual Studio Code (LaTeX Workshop Extension)
1. Open the `SocialMirror-AI` folder in VS Code.
2. Open `report/main.tex`.
3. Use the LaTeX Workshop extension to Build (`Ctrl+Alt+B`) and View PDF (`Ctrl+Alt+V`).

### Option C: Overleaf
1. Compress the `report/` directory into a `.zip` archive.
2. Upload the `.zip` directly into [Overleaf](https://www.overleaf.com).
3. Set `main.tex` as the root document and compile with PDFLaTeX.

---

## 5. Next Steps

1. **Section-by-Section Drafting**: Begin drafting Chapter 1 (Introduction) and Chapter 2 (Literature Review) using the structured outlines provided in `chapters/`.
2. **Architecture Diagramming**: Generate high-level multi-agent architectural diagrams and place the assets into `report/figures/`.
3. **Bibliography Expansion**: Add course-specific or lecture-recommended readings to `report/references.bib`.
4. **Git Version Control**: Commit the preparatory workspace structure to local Git tracking when ready.
