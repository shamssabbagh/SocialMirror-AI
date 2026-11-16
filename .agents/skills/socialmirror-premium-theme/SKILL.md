---
name: socialmirror-premium-theme
description: >-
  Official visual design system and LaTeX styling guidelines for the SocialMirror-AI academic project
  (Assignment 2, University of Haifa). Enforces a premium academic visual identity blending modern psychology
  and artificial intelligence aesthetics with a dark navy, deep teal, bright cyan, silver, and white palette.
  Provides complete specifications for single-page cover design, Hebrew RTL and English LTR bidirectional typography,
  XeLaTeX compilation, robust callout environments, publication-grade TikZ vector diagrams, and booktabs comparative matrices.
  Activate whenever the user requests "Use the SocialMirror Premium Theme" or "השתמש בעיצוב הקבוע של SocialMirror".
---

# SocialMirror-AI Premium Theme — Permanent Design System

## 1. Visual Identity Philosophy

The **SocialMirror Premium Theme** represents the visual and typographic standard for the **SocialMirror-AI** academic project at the University of Haifa. The theme harmonizes the cognitive, introspective depth of psychological well-being research with the futuristic, precision-oriented clarity of multi-agent artificial intelligence.

### Key Visual Pillars
- **Academic Authority**: Clean lines, generous whitespace, structured typographic hierarchy, and formal university presentation.
- **Cognitive-Technological Dualism**: Deep navy blues and teals anchor human psychological introspection, while vibrant cyan highlights signify autonomous AI perception and algorithmic reflection.
- **Rigor & Transparency**: Publication-ready TikZ diagrams, standardized `booktabs` matrices, and clear demarcation between empirical evidence and proposed architecture.
- **Flawless Bidirectionality**: First-class Hebrew RTL primary discourse with seamlessly isolated English LTR technical notation, author names, formulas, and IEEE citations.

---

## 2. Master Color Palette

All colors are formally defined in `report/preamble.tex` using the `xcolor` package (`dvipsnames, table`).

| Palette Role | LaTeX Color Name | RGB Values | HEX Code | Functional Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Navy** | `NavyBlueDark` | `(10, 40, 95)` | `#0A285F` | Primary titles, university headers, section numerals, outer borders |
| **Secondary Teal** | `AccentTeal` | `(0, 128, 128)` | `#008080` | Subtitles, agent node outlines, subsection titles, secondary emphasis |
| **Accent Cyan** | `AccentCyan` | `(0, 168, 204)` | `#00A8CC` | AI highlights, active focal points, divider line highlights, vector arrows |
| **Slate Gray** | `SlateGray` | `(80, 90, 100)` | `#505A64` | Institutional subheadings, course metadata, student role labels, captions |
| **Silver Accent** | `SilverAccent` | `(218, 224, 233)` | `#DAE0E9` | Subtle divider bars, card outlines, soft separation lines |
| **Light Blue Fill** | `LightBlueBg` | `(238, 244, 252)` | `#EEF4FC` | `agentbox` background fill, TikZ state/process node background |
| **Neutral Fill** | `LightBoxBg` | `(245, 247, 250)` | `#F5F7FA` | `ethicsbox` background fill, table zebra striping, neutral containers |
| **Border Gray** | `BorderGray` | `(200, 210, 225)` | `#C8D2E1` | Image framing, table horizontal rules, subtle box boundaries |
| **Critical Alert** | `BrickRed` | `(182, 42, 42)` | `#B62A2A` | Ethical caveats, privacy constraints, clinical disclaimers |
| **Canvas White** | `white` | `(255, 255, 255)` | `#FFFFFF` | Document background, card interiors, crisp contrast zones |

### LaTeX Color Definitions
```latex
\usepackage[dvipsnames, table]{xcolor}
\definecolor{NavyBlueDark}{RGB}{10, 40, 95}
\definecolor{AccentTeal}{RGB}{0, 128, 128}
\definecolor{AccentCyan}{RGB}{0, 168, 204}
\definecolor{SlateGray}{RGB}{80, 90, 100}
\definecolor{SilverAccent}{RGB}{218, 224, 233}
\definecolor{LightBoxBg}{RGB}{245, 247, 250}
\definecolor{LightBlueBg}{RGB}{238, 244, 252}
\definecolor{BorderGray}{RGB}{200, 210, 225}
```

---

## 3. Typographic & Multilingual Architecture

The document compiles strictly via **XeLaTeX** to support native TrueType/OpenType multilingual fonts and seamless bidirectionality.

### Font Configurations
- **Hebrew Primary**: Windows system `Arial` (`\newfontfamily\hebrewfont{Arial}[Script=Hebrew]`). Provides optimal on-screen clarity and print legibility.
- **Hebrew Sans/Mono**: `\hebrewfontsf{Arial}`, `\hebrewfonttt{Courier New}`.
- **English Terminology**: `Arial` (`\newfontfamily\englishfont{Arial}`) for technical terms, agent labels, and formulas.
- **Line Spacing**: $1.5\times$ line spacing (`\usepackage{setspace}\onehalfspacing`) for academic evaluation standards.
- **Running Headers & Footers**:
  * Running Header Left: `\small\textenglish{\textsc{SocialMirror-AI}}`
  * Running Header Right: `\small\nouppercase{\leftmark}`
  * Footer Center: `\thepage` (Page numbers centered, clean).

### Bidirectional Guardrails (RTL / LTR)
1. **Load Order**: `\usepackage{hyperref}` **MUST** be loaded **BEFORE** `\usepackage{polyglossia}` so that `bidi` correctly initializes PDF hyperlink coordinate transformations.
2. **Inline English Terms**: All Latin-character concepts, course names, and agent titles must be wrapped in `\textenglish{...}` or `\engterm{...}` (e.g., `\textenglish{Social Comparison Theory}`).
3. **Period & Punctuation at End of Lines**: Never end an RTL sentence with an isolated LTR term. Always conclude with Hebrew context or enclose within parentheses (e.g., `סוכן הניתוח (\agentAnalyst{}).`).
4. **Bibliography**: All English academic entries must be wrapped inside `\begin{english} ... \end{english}` with `\addto\captionsenglish{\renewcommand{\bibname}{\texthebrew{ביבליוגרפיה}}}` to preserve LTR citation ordering without corrupting the Hebrew title.

---

## 4. Single-Page Cover Design Specification

The cover page must fit **strictly on exactly ONE A4 page** with zero overflow into page 2.

```
+-------------------------------------------------------------+
|                                                             |
|                      אוניברסיטת חיפה                         |
|                                                             |
|                     SocialMirror-AI                         |
|           מראה חברתית בעידן הבינה המלאכותית                 |
|               ----==== [ CYAN ACCENT ] ====----             |
|                                                             |
|             מטלה 2 – דוח מכין לפרויקט עתידי                 |
|            קורס: סוכני AI ו־Vibe Coding                     |
|                                                             |
|                           מגישות:                            |
|        שמס סבאג                      מלאק פרוג׳ה            |
|   סטודנטית לפסיכולוגיה           סטודנטית לתקשורת ושיווק     |
|                                                             |
|   +-----------------------------------------------------+   |
|   |                                                     |   |
|   |             [ FEATURED COVER ARTWORK ]              |   |
|   |         assets/socialmirror-cover.png               |   |
|   |                                                     |   |
|   +-----------------------------------------------------+   |
|                                                             |
+-------------------------------------------------------------+
```

### Cover Page Structural Rules
1. **Vertical Hierarchy**:
   1. Institution: `אוניברסיטת חיפה` (`\Large\bfseries\color{NavyBlueDark}`)
   2. Title: `SocialMirror-AI` (`\fontsize{32pt}{38pt}\selectfont\bfseries\color{NavyBlueDark}`)
   3. Subtitle: `מראה חברתית בעידן הבינה המלאכותית` (`\Large\bfseries\color{AccentTeal}`)
   4. Accent Divider: TikZ line combining `SilverAccent` bar (9cm), `AccentCyan` center segment (2.8cm), and `NavyBlueDark` center pip.
   5. Assignment: `מטלה 2 – דוח מכין לפרויקט עתידי` (`\large\bfseries\color{NavyBlueDark}`)
   6. Course: `קורס: סוכני AI ו־Vibe Coding` (`\normalsize\bfseries\color{SlateGray}`)
   7. Authors Header: `מגישות:` (`\large\bfseries\color{NavyBlueDark}`)
   8. Authors Columns: Two balanced `minipage` blocks (width `0.45\textwidth` each):
      - Right (First read in RTL): **שמס סבאג** / סטודנטית לפסיכולוגיה
      - Left (Second read in RTL): **מלאק פרוג׳ה** / סטודנטית לתקשורת ושיווק
      - *No additional student IDs or extra text.*
   9. Official Cover Image: Centered, width `0.92\linewidth`, height constrained, bordered with `\fcolorbox{BorderGray}{white}{...}`.

---

## 5. Visual Components & Environments

### A. Robust Callout Boxes
Standard `tcolorbox` can emit invalid PDF operators under XeLaTeX `bidi`. This theme implements callout environments via `environ` and `\fcolorbox`:

#### Agent Callout (`agentbox`)
```latex
\NewEnviron{agentbox}[1]{%
    \par\vspace{0.35cm}\noindent
    \begingroup
    \setlength{\fboxsep}{10pt}%
    \setlength{\fboxrule}{1.2pt}%
    \fcolorbox{NavyBlueDark}{LightBlueBg}{%
        \begin{minipage}{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}
            {\large\bfseries\color{NavyBlueDark} #1}\par\vspace{0.2cm}%
            \BODY
        \end{minipage}%
    }%
    \endgroup\par\vspace{0.35cm}%
}
```

#### Ethics & Governance Callout (`ethicsbox`)
```latex
\NewEnviron{ethicsbox}[1][הערת אתיקה וממשל אחראי בבינה מלאכותית]{%
    \par\vspace{0.35cm}\noindent
    \begingroup
    \setlength{\fboxsep}{10pt}%
    \setlength{\fboxrule}{1.2pt}%
    \fcolorbox{BrickRed}{LightBoxBg}{%
        \begin{minipage}{\dimexpr\linewidth-2\fboxsep-2\fboxrule\relax}
            {\large\bfseries\color{BrickRed} #1}\par\vspace{0.2cm}%
            \BODY
        \end{minipage}%
    }%
    \endgroup\par\vspace{0.35cm}%
}
```

### B. TikZ Conceptual Diagrams
- **Coordinate Safety**: Always encapsulate TikZ code within `\begin{LTR} ... \end{LTR}` to ensure that direction flips do not invert vector coordinates or arrowhead geometries.
- **Node Styling**:
  * Process / Core States: `rectangle, draw=NavyBlueDark, fill=LightBlueBg, rounded corners=2.5mm, line width=1pt`
  * AI Agent Monitors: `rectangle, draw=AccentTeal, fill=white, rounded corners=2mm, line width=1.1pt`
  * Process Flow: `draw=NavyBlueDark, line width=1.1pt, -{Latex[length=2.8mm]}`
  * Agent Observation/Intervention: `draw=AccentTeal, dashed, line width=1.0pt, -{Latex[length=2.2mm]}`
- **Dimensions**: Maintain total diagram width $\le 14.5\,\text{cm}$ (`scale \approx 0.85`) to avoid `Overfull \hbox`.

### C. Academic Comparative Matrices
- Tables must utilize `booktabs` (`\toprule`, `\midrule`, `\bottomrule`) and `tabularx`.
- In RTL mode, fixed `p{...}` columns must be prefixed with `>{\raggedleft\arraybackslash}` to prevent bad word-spacing and underfull warnings.
- Authors, study citations, and English journal names must be wrapped in `\textenglish{...}`.

```latex
\begin{table}[H]
\centering
\caption{מטריצת ניתוח ספרות מחקרית אמפירית}
\label{tab:literature_matrix}
\small
\begin{tabularx}{\textwidth}{>{\raggedleft\arraybackslash}p{2.7cm} >{\raggedleft\arraybackslash}p{2.2cm} X >{\raggedleft\arraybackslash}p{3.2cm}}
\toprule
\textbf{מחקר ומקור} & \textbf{מתודולוגיה ומדגם} & \textbf{ממצאים אמפיריים מרכזיים} & \textbf{תרומה ישירה ל-\projectname{}} \\
\midrule
% ... entries ...
\bottomrule
\end{tabularx}
\end{table}
```

---

## 6. Multi-Agent Roles & Enforcement

| Agent | Responsibility Under SocialMirror Premium Theme |
| :--- | :--- |
| **`academic-writer`** | **Default Designer**: Applies the theme by default to all chapter drafting, front matter, subheadings, callouts, and mathematical notation. Ensures clean LTR English isolation within Hebrew text. |
| **`academic-coordinator`** | **Visual Gatekeeper**: Audits whole-document consistency, verifies page budgets, confirms the cover page occupies exactly one A4 page, and checks that every visual element conforms to theme palette. |
| **`academic-researcher`** | **Visual Data Formatter**: Formats literature reviews, meta-analytic matrices, and empirical evidence dossiers to match the `booktabs` matrix specifications and color schemes. |

---

## 7. Activation & Reusability

### Trigger Phrases
The agent system automatically activates this skill upon detecting any of the following phrases:
- `"Use the SocialMirror Premium Theme"`
- `"השתמש בעיצוב הקבוע של SocialMirror"`
- `"Apply SocialMirror theme"`
- `"החל את ערכת העיצוב הרשמית של SocialMirror"`

### Explicit Overrides
If the user explicitly specifies a different design direction (e.g., *"Use a minimalist black-and-white theme"* or *"Use IEEE conference format"*), the agents will respect the new instruction for that specific task without deleting, overwriting, or corrupting this stored skill.

---

## 8. Quality Assurance & Verification Standards

Before considering any report draft complete, verify:
1. **Compilation**: `compile.ps1` runs XeLaTeX cleanly with exit code `0` and no critical warnings.
2. **Single-Page Cover**: Page 1 contains the full cover; Chapter 1 begins immediately on Page 2.
3. **No PDF Stream Corruption**: Zero `Syntax Error: Restoring state when no valid states to pop` or `No current point in closepath`.
4. **Image Fidelity**: Cover artwork aspect ratio preserved; no clipping, stretching, or pixelation.
5. **Bidirectional Correctness**:
   - Numbers and years appear in correct sequence (e.g., `2018`, not `8102`).
   - English terms do not flip trailing Hebrew punctuation.
   - Bibliography entries follow standard IEEE format.
