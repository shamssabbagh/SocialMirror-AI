# Quality Gates & Verification Standards

To guarantee that the **SocialMirror-AI** preparatory report meets publication and university standards, every contribution must satisfy three strict Quality Gates before inclusion in the final deliverable.

---

## Quality Gate 1: Empirical Evidence Gate (Research Verification)
Every section incorporating factual, psychological, or empirical claims must satisfy:
1. **Primary Source Requirement**: Claims must reference peer-reviewed academic literature (journal articles, conference proceedings, or seminal texts).
2. **BibTeX Verification**: Every referenced work must be present in `report/references.bib` with verified metadata (authors, title, journal/venue, year, volume/pages).
3. **No Phantom Citations**: Synthetic or hallucinated citations are strictly prohibited. The Research Agent must verify that each cited work actually exists.
4. **Contextual Fidelity**: Research findings must not be misrepresented (e.g., distinguishing between correlation and causation in social media studies).

---

## Quality Gate 2: Independent QA Gate (Adversarial Review)
Before any draft is merged into `report/chapters/`, it must undergo independent review:
1. **Fact-Checking**: The Independent QA Agent checks each paragraph against the verified literature.
2. **Mathematical Consistency**: Formulas and notation must strictly adhere to definitions established in `report/macros.tex`.
3. **Completeness & Depth**: Shallow bullet points must be expanded into rigorous analytical discourse appropriate for an advanced AI course.
4. **Sign-Off Protocol**: The QA Agent must explicitly issue:
   - `STATUS: APPROVED` — Proceed to LaTeX integration.
   - `STATUS: REVISION_REQUIRED` — Return to drafting agent with actionable feedback points.

---

## Quality Gate 3: LaTeX Compilation Gate (Build Verification)
Every merged chapter must pass automated build verification:
1. **Zero Fatal Errors**: Compilation must complete with exit code 0.
2. **Clean Auxiliary Resolution**: `main.aux`, `main.toc`, `main.bbl`, `main.out` must resolve with zero undefined reference warnings.
3. **Typography & Layout**: No unhandled overfull `\hbox` warnings (>10pt) or broken table margins.
4. **Page Budget Adherence**: Chapter length must remain consistent with the ~40-page master allocation plan.
