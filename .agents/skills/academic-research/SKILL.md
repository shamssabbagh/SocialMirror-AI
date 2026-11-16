---
name: academic-research
description: >-
  Operational runbook for conducting rigorous academic literature research for SocialMirror-AI.
  Covers query formulation, peer-reviewed source vetting, empirical evidence extraction,
  correlation vs. causation differentiation, DOI verification, structured evidence dossier creation,
  and BibTeX curation under the supervision of the Academic Coordinator.
---

# Academic Research Skill

This skill defines the operational runbook and quality protocols for the **Academic Research Agent** supporting **SocialMirror-AI**.

---

## 1. Research Protocol Overview

The Research Agent operates in four sequential phases:

```text
[Coordination Brief] 
       │
       ▼
1. Query Formulation & Academic Search
       │
       ▼
2. Source Vetting & Epistemic Audit (Peer-review, N, Methodology)
       │
       ▼
3. Evidence Synthesis & Dossier Construction
       │
       ▼
4. BibTeX Verification & Quality Checklist Sign-Off
       │
       ▼
[Submission to Independent QA / Coordinator]
```

---

## 2. Source Quality Criteria & Hierarchy

Every source selected must be audited against the following hierarchy:

| Tier | Category | Accepted Publication Venues | Weight / Role |
| :--- | :--- | :--- | :--- |
| **Tier 1A** | Seminal Classical Literature | Canonical books, classic foundations (e.g., Festinger 1954, Rosenberg 1965) | Foundational theory |
| **Tier 1B** | High-Impact Peer-Reviewed Journals | APA, Elsevier, Sage, Springer, Wiley, Taylor & Francis journals (*JPSP*, *CPS*, *CHB*, *JIA*) | Primary empirical evidence |
| **Tier 1C** | Flagship AI / HCI Proceedings | ACM (CHI, UIST, CSCW), AAAI, NeurIPS, ACL | Agent architecture & simulation |
| **Tier 2** | Institutional & Policy Reports | WHO, American Psychological Association, US Surgeon General, Pew Research | Macro demographic context |
| **Rejected** | Non-Academic / Unvetted | Medium posts, commercial blogs, unverified preprints, marketing agency releases | Strictly Prohibited |

---

## 3. Epistemic Classification Standards

When summarizing research findings, the agent must categorize claims into one of four distinct epistemic classes:

1. **`[ESTABLISHED EMPIRICAL]`**: Robust, meta-analyzed or widely replicated findings across multiple independent cohorts.
2. **`[CORRELATIONAL]`**: Observed statistical associations from cross-sectional surveys (e.g., Pearson's $r$, odds ratios). **Constraint**: Never state or imply causation (e.g., "social media causes depression" is invalid; "higher daily Instagram usage is correlated with increased depressive symptoms among adolescent girls" is valid).
3. **`[CAUSAL EXPERIMENT]`**: Findings derived from randomized controlled trials (RCTs), lab experiments with control groups, or longitudinal cross-lagged panel models.
4. **`[THEORETICAL HYPOTHESIS]`**: Conceptual frameworks, models, or hypotheses proposed by authors without definitive empirical proof.

---

## 4. Citation & DOI Verification Workflow

Before any reference is added to `report/references.bib`, follow this 4-step verification:

1. **Title & Author Verification**: Confirm the exact author spelling and full publication title against publisher databases (Crossref, PubMed, ACM Digital Library, Google Scholar).
2. **Venue & Date Audit**: Ensure the journal/conference name is written in full (or standard ISO abbreviation) and publication year is accurate.
3. **DOI Cross-Check**: Verify the Digital Object Identifier (DOI) format (`10.xxxx/...`) and verify that resolving `https://doi.org/<DOI>` leads to the authentic publisher landing page.
4. **Unique BibTeX Key**: Generate a clean, semantic key matching the format `[FirstAuthorLastName][Year][FirstMeaningfulTitleWord]` (e.g., `festinger1954theory`, `twenge2018increases`, `park2023generative`).

---

## 5. Output Templates

### Template A: Structured Evidence Dossier

```markdown
### Evidence Dossier: [Short Title / Topic]

- **Citation**: [Full APA citation]
- **DOI**: [Link or DOI string]
- **Publication Venue**: [Journal / Conference Name] (Peer-Reviewed: Yes/No)
- **Epistemic Class**: [ESTABLISHED EMPIRICAL | CORRELATIONAL | CAUSAL EXPERIMENT | THEORETICAL HYPOTHESIS]

#### 1. Study Methodology & Sample
- **Design**: [Longitudinal panel / Randomized lab experiment / Cross-sectional survey]
- **Sample**: $N = [Count]$, [Demographic details: age, gender, geographic location]
- **Instruments Used**: [e.g., Rosenberg Self-Esteem Scale (RSES), PANAS, Daily Diary method]

#### 2. Key Empirical Findings
- [Specific finding 1 with statistics, effect sizes, or confidence intervals if available]
- [Specific finding 2]

#### 3. Limitations & Biases
- [e.g., Self-report bias, Western-centric sample (WEIRD), lack of long-term tracking]

#### 4. Application to SocialMirror-AI
- **Relevant Chapter**: [e.g., Chapter 2 (Literature Review) / Chapter 3 (Architecture)]
- **Architectural Contribution**: [e.g., Defines the threshold for upward comparison salience $\mathcal{S}_{\text{comp}}$ in the AnalystAgent]

#### 5. Verified BibTeX Entry
```bibtex
@article{key,
  author = {...},
  title = {...},
  journal = {...},
  year = {...},
  doi = {...}
}
```
```

---

## 6. Error Handling & Edge Cases

| Scenario | Agent Response / Protocol |
| :--- | :--- |
| **DOI Not Found / Pre-digital paper** | Note `DOI: Unavailable (Pre-digital publication)`. Verify volume, issue, and page numbers via library catalog. |
| **Conflicting Empirical Evidence** | Do not hide the conflict. Present both perspectives explicitly (e.g., "While Twenge et al. report strong negative correlations, Orben & Przybylski argue effect sizes are minimal when controlling for covariates"). |
| **Paywalled Paper / Abstract Only** | Clearly note: `[Audited from Publisher Abstract and Indexing Metadata]`. Do not extrapolate detailed methodology beyond published abstracts. |
| **Suspected AI Hallucination in Prompt** | If asked to verify a citation that does not exist, explicitly reply: `[UNVERIFIED: Citation appears non-existent in academic databases. Do not use.]` |

---

## 7. Quality Checklist (Pre-QA Audit)

Before delivering research output to the Academic Coordinator or Independent QA, the agent must check:
- [ ] Every included source is from a peer-reviewed or authoritative academic source.
- [ ] No citation details, statistics, or quotes are fabricated.
- [ ] Correlational claims are explicitly distinguished from causal mechanisms.
- [ ] Complete BibTeX entry contains valid syntax (no missing braces, unescaped ampersands).
- [ ] The finding has a direct, concrete mapping to SocialMirror-AI's system design.
- [ ] The research dossier is logged for the Shams $\rightarrow$ Malak handoff record.
