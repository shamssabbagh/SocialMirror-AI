---
name: socialmirror-premium-theme
description: >-
  Official visual design system and LaTeX styling guidelines for the SocialMirror-AI academic project
  (Assignment 2, University of Haifa). Enforces a premium academic visual identity inspired by the dark black-and-purple
  aesthetic: a dark black/deep-violet cover with vibrant purple "Mirror-AI" accents, framed central digital mirror illustration,
  white interior pages with dark purple section headings, purple chapter badges, light lavender callout boxes for objectives/insights/summaries,
  lavender table headers, and publication-grade card-and-arrow TikZ vector diagrams.
  Activate whenever the user requests "Use the SocialMirror Premium Theme" or "השתמש בעיצוב הקבוע של SocialMirror".
---

# SocialMirror-AI Premium Theme — Permanent Design System (Black, Royal Purple & Lavender)

## 1. Visual Identity Philosophy

The **SocialMirror Premium Theme** represents the visual and typographic standard for the **SocialMirror-AI** academic project at the University of Haifa. The theme harmonizes the cognitive, introspective depth of psychological well-being research with the sleek, high-contrast clarity of modern agentic artificial intelligence.

### Key Visual Pillars
- **Dark Elegance & Digital Introspection**: The report opens with an immersive dark cover (deep black-violet `#0B0813`) featuring vibrant purple highlights (`#9D4EDD`) on `Mirror-AI`, framing the central digital mirror illustration that symbolizes the mirror reflection of social comparison.
- **Academic Authority & Interior Clarity**: Interior pages transition to crisp canvas white (`#FFFFFF`) with dark purple (`#2E1065`) headings, subtle lavender dividers, and optimal typographic whitespace ensuring effortless readability on screen and in high-resolution print.
- **Iconic Chapter Badging**: Every chapter opens with a solid royal purple rounded box (`#6D28D9`) displaying the chapter number in crisp white, echoed consistently in the Table of Contents.
- **Structured Lavender Callouts**: Standardized light lavender (`#F5F3FF`) callout environments with lavender borders (`#C4B5FD`) for project objectives (`objectivebox`), metacognitive insights (`insightbox`), chapter summaries (`summarybox`), and ethical safeguards (`ethicsbox`).
- **Card-and-Arrow System Architecture**: Modular agent society diagrams and information-flow architectures designed as clean rounded cards with directed purple arrows, accompanied by lavender-tinted booktabs comparative tables.
- **Rigorous Methodological Labeling**: All UI prototypes, mockups, and simulation parameters are explicitly tagged with illustrative markers ("המחשה" / "Illustrative Prototype").
- **Flawless Bidirectionality**: First-class Hebrew RTL primary discourse with seamlessly isolated English LTR technical notation, author names, formulas, and IEEE citations.

---

## 2. Master Color Palette

All colors are formally defined in `report/preamble.tex` using the `xcolor` package (`dvipsnames, table`).

| Palette Role | LaTeX Color Name | RGB Values | HEX Code | Functional Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Cover Black** | `CoverBlack` | `(11, 8, 19)` | `#0B0813` | Dark cover page background canvas |
| **Dark Purple** | `DarkPurple` | `(46, 16, 101)` | `#2E1065` | Main document headings, section titles, primary table borders |
| **Royal Purple** | `RoyalPurple` | `(109, 40, 217)` | `#6D28D9` | Solid chapter number badges, TOC badges, primary vector arrows |
| **Purple Accent** | `PurpleAccent` | `(157, 78, 221)` | `#9D4EDD` | Title accent on `Mirror-AI`, active focal points, subtle glowing borders |
| **Purple Glow** | `PurpleGlow` | `(192, 132, 252)` | `#C084FC` | Soft neon purple accents, decorative elements |
| **Lavender Light** | `LavenderLight` | `(245, 243, 255)` | `#F5F3FF` | Callout box background fill, table zebra striping |
| **Lavender Card** | `LavenderCard` | `(237, 233, 254)` | `#EDE9FE` | Table headers, secondary card background fill |
| **Lavender Border** | `LavenderBorder` | `(196, 181, 253)` | `#C4B5FD` | Callout borders, running header rule, card outlines |
| **Charcoal Text** | `CharcoalText` | `(31, 41, 55)` | `#1F2937` | High-contrast body text for maximum print & screen legibility |
| **Slate Muted** | `SlateMuted` | `(107, 114, 128)` | `#6B7280` | Running header metadata, captions, secondary annotations |
| **Alert Rose** | `AlertRose` | `(225, 29, 72)` | `#E11D48` | Ethical caveats, downward metric trends, risk matrices |
| **Success Emerald** | `SuccessEmerald` | `(16, 185, 129)` | `#10B981` | Resilience metrics, positive psychological buffers |
| **Canvas White** | `white` | `(255, 255, 255)` | `#FFFFFF` | Interior page background, card interiors |

### LaTeX Color Definitions
```latex
\usepackage[dvipsnames, table]{xcolor}
\definecolor{CoverBlack}{RGB}{11, 8, 19}
\definecolor{DarkPurple}{RGB}{46, 16, 101}
\definecolor{RoyalPurple}{RGB}{109, 40, 217}
\definecolor{PurpleAccent}{RGB}{157, 78, 221}
\definecolor{PurpleGlow}{RGB}{192, 132, 252}
\definecolor{LavenderLight}{RGB}{245, 243, 255}
\definecolor{LavenderCard}{RGB}{237, 233, 254}
\definecolor{LavenderBorder}{RGB}{196, 181, 253}
\definecolor{CharcoalText}{RGB}{31, 41, 55}
\definecolor{SlateMuted}{RGB}{107, 114, 128}
\definecolor{AlertRose}{RGB}{225, 29, 72}
\definecolor{SuccessEmerald}{RGB}{16, 185, 129}
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
5. **Chapter Headings Alignment & Badging**:
   - All Hebrew chapter headings are strictly aligned to the **right margin** of the body text.
   - The purple chapter number badge (`[ \thechapter ]` in `RoyalPurple`) is positioned to the **right** of the Hebrew heading text.
   - When a chapter title wraps across multiple lines, all lines are aligned to the **exact same right vertical line** (hanging indent) adjacent to the badge.
   - English terms embedded in titles (e.g. `SocialMirror-AI`, `AI`) maintain strict LTR character ordering and natural spacing without awkward hyphenation or line stretching (using `\projectname{}` with internal `\mbox`).
   - Unnumbered headings (`\@makeschapterhead`) align flush to the right margin.

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
1. **Dark Canvas**: `\pagecolor{CoverBlack}` on the cover page, cleanly returning to `\pagecolor{white}` on interior pages.
2. **Vertical Hierarchy**:
   1. Institution: `אוניברסיטת חיפה` (`\Large\bfseries\color{white}`)
   2. Title: `SocialMirror-AI` with `Mirror-AI` highlighted in vibrant purple (`{\fontsize{34pt}{40pt}\selectfont\bfseries\textcolor{white}{Social}\textcolor{PurpleAccent}{Mirror-AI}}`)
   3. Subtitle: `מראה חברתית בעידן הבינה המלאכותית` (`\Large\bfseries\color{LavenderLight}`)
   4. Accent Divider: TikZ line combining `LavenderBorder` bar, `PurpleAccent` center segment, and glowing center pip.
   5. Assignment: `מטלה 2 – דוח מכין לפרויקט עתידי` (`\large\bfseries\color{white}`)
   6. Course: `קורס: סוכני AI ו־Vibe Coding` (`\normalsize\bfseries\color{LavenderLight!85}`)
   7. Authors Header: `מגישות:` (`\large\bfseries\color{PurpleAccent}`)
   8. Authors Columns: Two balanced `minipage` blocks (width `0.45\textwidth` each):
      - Right (First read in RTL): **שמס סבאג** (`\color{white}`) / סטודנטית לפסיכולוגיה (`\color{LavenderLight!75}`)
      - Left (Second read in RTL): **מלאק פרוג׳ה** (`\color{white}`) / סטודנטית לתקשורת ושיווק (`\color{LavenderLight!75}`)
      - *No additional student IDs or extra text.*
   9. Official Cover Image: Centered, width `0.88\linewidth`, height constrained, bordered with glowing purple/lavender accent container `\fcolorbox{PurpleAccent}{CoverBlack}{...}`.

---

## 5. Visual Components & Environments

### A. Robust Lavender Callout Boxes
Standard `tcolorbox` can emit invalid PDF operators under XeLaTeX `bidi`. This theme implements callout environments via `environ` and `\fcolorbox`:
- `objectivebox`: Lavender background (`LavenderLight`), lavender border (`LavenderBorder`), royal purple bullet, dark purple heading.
- `insightbox`: Lavender background (`LavenderLight`), royal purple border (`RoyalPurple`), royal purple bullet, dark purple heading.
- `summarybox`: Lavender background (`LavenderLight`), lavender border (`LavenderBorder`), royal purple bullet, dark purple heading.
- `agentbox`: Lavender background (`LavenderLight`), royal purple border (`RoyalPurple`), dark purple heading.
- `ethicsbox`: Lavender background (`LavenderLight`), alert rose border (`AlertRose`), alert rose heading.

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
