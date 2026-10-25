# HCMUT LaTeX templates

LaTeX templates for reports and slides at the Faculty of Computer Science and Engineering, Ho Chi Minh City University of Technology (HCMUT).

| Folder | Kind | Main file | Sample output |
|---|---|---|---|
| `report-assignment/` | Short report / course assignment (`article`, HCMUT header and footer on every page) | `template.tex` | `template.pdf` |
| `report-thesis/` | Long report: internship report, thesis proposal, thesis (`book`, Vietnamese, title page with frame, chapter headers) | `main.tex` | `main.pdf` |
| `slides/` | Beamer slides 16:9, HCMUT background | `main.tex` | `main.pdf` |

## Build

Needs TeX Live (or MacTeX) with `vntex`.

```sh
# report-thesis and slides: output goes to out/ (set in .latexmkrc)
cd report-thesis && latexmk main.tex
cd slides && latexmk main.tex

# report-assignment
cd report-assignment && latexmk -pdf template.tex
```

On Overleaf, upload one folder and set the main document to `main.tex` (or `template.tex`).

## report-thesis

```
main.tex              preamble, page layout, chapter style, order of parts
settings_custom.tex   extra packages, captions, paragraph spacing
frontmatter/          title page, acknowledgements, abstracts (VI/EN), declaration, abbreviations, profile
chapter/ch1..ch5.tex  chapters
appendix/             appendices (label "Phụ lục")
references/           refs.bib + IEEEtran.bst
Images/               figures (\graphicspath points here)
```

- Fill in the `[...]` placeholders in `frontmatter/titlepage.tex`, `acknowledgements.tex`, `commitment.tex`.
- Add or remove chapters with `\include{chapter/chN}` in `main.tex`.
- Theorem environments (`proposition`, `lemma`, `definition`, `remark`) and `algorithmic` keywords are already in Vietnamese.
- The profile page (`frontmatter/profile.tex`) is only needed for a thesis; uncomment it at the end of `main.tex`.

## slides

- Edit the title block (`\title`, `\author`, `\institute`) at the top of `main.tex`.
- The footer counts frames up to the `\label{endmain}` on the last main slide; backup slides after `\appendix` are not counted.
- A table-of-contents frame appears at the start of each section; remove the `\AtBeginSection` block to turn it off.
