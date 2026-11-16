# BibTeX Verification & Formatting Guide

This guide ensures that all entries added to `report/references.bib` adhere to IEEE and academic BibTeX standards, preventing build breaks during `bibtex main` execution.

---

## 1. Syntax Rules

1. **Escape Special Characters**:
   - Ampersands (`&`) in journal or publisher names must be escaped as `\&` (e.g., `publisher = {John Wiley \& Sons}`).
   - Percentage signs (`%`) and underscores (`_`) in titles or URLs must be escaped (`\%`, `\_`).
2. **Author Name Formatting**:
   - Use `Last, First and Last, First` format to ensure proper bibtex parsing:
     `author = {Twenge, Jean M. and Joiner, Thomas E. and Rogers, Megan L.}`
3. **Preserve Capitalization**:
   - Acronyms, proper nouns, and framework names in titles must be protected by double braces:
     `title = {Testing the {RSES} and {PANAS} Scales in {Instagram} Feed Simulations}`
4. **Standard Fields Required**:
   - `@article`: `author`, `title`, `journal`, `volume`, `number`, `pages`, `year`, `publisher`, `doi`.
   - `@inproceedings`: `author`, `title`, `booktitle`, `pages`, `year`, `organization` / `publisher`, `doi`.
   - `@book`: `author` (or `editor`), `title`, `publisher`, `year`, `address`.

---

## 2. Verification Checklist Before Inserting into `references.bib`
- [ ] Run a test build or syntax check to ensure braces balance.
- [ ] Verify that no duplicate BibTeX keys exist in `report/references.bib`.
- [ ] Ensure the DOI resolves to the official publication.
