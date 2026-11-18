# Portfólio de IA de Gabriela Dória

**Português** · [English](README.en.md)

**Página:** https://gabriela-doria.github.io/ai-portfolio/ (em inglês: https://gabriela-doria.github.io/ai-portfolio/#en)

Página única com meus projetos de IA aplicada: automações, um app em uso pela equipe de um projeto de extensão, agentes com Claude e demos feitas do zero. Cada caso mostra o problema, o que eu fiz e o resultado, com a IA usada e como medi.

## O que tem aqui

| Arquivo | O que é |
|---|---|
| [`index.html`](index.html) | A página inteira: texto, CSS e JavaScript no mesmo arquivo, sem bibliotecas externas |
| `assets/` | Foto e tela do app do Areia Viva (modo de demonstração, dados fictícios) |
| `build/gerar.py` | Gera o `index.html` em português e inglês a partir de um molde só |
| `README.md` e `README.en.md` | Este texto, em português e em inglês |
| `LICENSE` | Licença MIT |

## Como atualizar

1. Edite o texto em `build/gerar.py` (cada frase tem a versão em português e em inglês lado a lado) e rode `python3 build/gerar.py` na raiz do repositório. Também dá para editar o `index.html` direto: o português fica no bloco `id="pt"` e o inglês no bloco `id="en"`; mude os dois juntos.
2. Mantenha a regra dos números: só número com fonte; dado fictício e estimativa marcados como tais.
3. Mude a data em "Atualizado em", no rodapé da página.
4. Salve com uma mensagem de commit curta, por exemplo `docs: novo caso X`.
5. O GitHub Pages publica sozinho em 1 a 2 minutos, no mesmo link. Para conferir, abra a aba Actions até `pages build and deployment` ficar verde e recarregue a página com `Ctrl+F5`.

## Repositórios citados na página

- [personal-os-claude](https://github.com/gabriela-doria/personal-os-claude)
- [student-project-ops-ai](https://github.com/gabriela-doria/student-project-ops-ai)
- [campus-de-energia](https://github.com/gabriela-doria/campus-de-energia)
- [rota-do-excedente](https://github.com/gabriela-doria/rota-do-excedente)

---

Feito por [Gabriela Dória](https://github.com/gabriela-doria) · Engenharia Ambiental, Poli-USP, São Paulo · [LinkedIn](https://www.linkedin.com/in/gabriela-vs-doria/) · Licença [MIT](LICENSE)
