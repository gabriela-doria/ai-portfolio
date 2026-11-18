# Gabriela Dória's AI portfolio

[Português](README.md) · **English**

**Page:** https://gabriela-doria.github.io/ai-portfolio/#en (Portuguese: https://gabriela-doria.github.io/ai-portfolio/)

A single page with my portfolio in two parts: managing by metrics at Poli Social (OKRs, a client selection call, an Innovation Group, consulting for NGOs) and data, automation and AI (an app in daily use by the team of a university extension project, agents built with Claude and demos built from scratch). Each case shows the problem, what I did and the result, and how I measured it.

## What is here

| File | What it is |
|---|---|
| [`index.html`](index.html) | The whole page: text, CSS and JavaScript in one file, no external libraries |
| `assets/` | Photo, screens of the Areia Viva app (demo mode, fictitious data) , a screenshot of the Poli Social Projects area OKR spreadsheet, 2025, , Innovation Group slides, flowcharts and implementation document (2025), Campus de energia charts and a screen of the Rota do Excedente demo |
| `build/conteudo.py` | All page text, with Portuguese and English side by side |
| `build/gerar.py` | Page styles; builds `index.html` from `conteudo.py` |
| `README.md` and `README.en.md` | This text, in Portuguese and English |
| `LICENSE` | MIT license |

## How to update

1. Edit the text in `build/conteudo.py` (each sentence has its Portuguese and English versions side by side) and run `python3 build/gerar.py` from the repository root. You can also edit `index.html` directly: Portuguese lives in the `id="pt"` block and English in the `id="en"` block; change both together.
2. Keep the rule for numbers: only numbers with a source; fictional data and estimates labelled as such.
3. Change the date in "Atualizado em" in the page footer.
4. Save with a short commit message, for example `docs: add case X`.
5. GitHub Pages republishes on its own in 1 to 2 minutes, at the same link. To check, open the Actions tab until `pages build and deployment` turns green and reload the page with `Ctrl+F5`.

## Repositories linked from the page

- [personal-os-claude](https://github.com/gabriela-doria/personal-os-claude)
- [student-project-ops-ai](https://github.com/gabriela-doria/student-project-ops-ai)
- [campus-de-energia](https://github.com/gabriela-doria/campus-de-energia)
- [rota-do-excedente](https://github.com/gabriela-doria/rota-do-excedente)

---

By [Gabriela Dória](https://github.com/gabriela-doria) · Environmental Engineering, Poli-USP, São Paulo · [LinkedIn](https://www.linkedin.com/in/gabriela-vs-doria/) · [MIT](LICENSE) license
