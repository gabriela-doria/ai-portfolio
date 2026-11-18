# Conteúdo do portfólio. Cada texto tem a versão em português e em inglês: t('pt', 'en').
# O molde (build/gerar.py) monta a página duas vezes, uma por idioma.

GH = "https://github.com/gabriela-doria"
LI = "https://www.linkedin.com/in/gabriela-vs-doria/"
ATUALIZADO = {"pt": "17/11/2026", "en": "17 Nov 2026"}


def page(L):
    pt = L == "pt"

    def t(a, b):
        return a if pt else b

    sid = "" if pt else "-en"
    other = t('<a href="#en" lang="en">English</a>', '<a href="#pt" lang="pt-BR">Português</a>')

    def bar(label, pct, value, amb=False, goal=None):
        g = f'<span class="goal" style="left:{goal}%"></span>' if goal is not None else ""
        return (f'<div class="bar"><span>{label}</span><span class="trk"><span class="fill{" amb" if amb else ""}" '
                f'style="width:{pct}%"></span>{g}</span><span class="v">{value}</span></div>')

    def nums(items, cls=""):
        return f'<div class="nums {cls}">' + "".join(f"<div><b>{a}</b><small>{b}</small></div>" for a, b in items) + "</div>"

    def flow(p, f, r):
        return (f'<div class="flow"><div class="box"><span class="k">{t("Problema","Problem")}</span>{p}</div>'
                f'<div class="box"><span class="k">{t("O que eu fiz","What I did")}</span>{f}</div>'
                f'<div class="box res"><span class="k">{t("Resultado","Result")}</span>{r}</div></div>')

    def chips(on, off=()):
        return '<div class="chips">' + "".join(f'<span class="chip on">{c}</span>' for c in on) + "".join(f'<span class="chip">{c}</span>' for c in off) + "</div>"

    def case(cid, meta_b, meta, tag, h3, body):
        return (f'<article class="case" id="{cid}{sid}"><div class="meta"><b>{meta_b}</b>{meta}<span class="tag">{tag}</span></div>'
                f'<div><h3>{h3}</h3>{body}</div></article>')

    # ---------- matriz competências x casos ----------
    cols = [t("Diretoria", "Director"), t("Edital", "Selection"), t("Inovação", "Innovation"), "Palavras de Paz",
            "Areia Viva", "Personal OS", "Campus", "Rota", "QGIS", "Megève"]
    rows = [
        (t("Gestão por indicadores (OKRs e KPIs)", "Managing by metrics (OKRs and KPIs)"), "●○○●●○○○○○"),
        (t("Liderança de pessoas", "Leading people"), "●○●●○○○○○○"),
        (t("Decisão com critério explícito", "Decisions on explicit criteria"), "○●●○●○●●○○"),
        (t("Diagnóstico e resolução de problemas", "Diagnosis and problem solving"), "●●●●●●●●●○"),
        (t("Dados, planilhas e dashboards", "Data, spreadsheets and dashboards"), "●●○●●○●●●○"),
        (t("Automação e agentes de IA", "Automation and AI agents"), "○○○○●●○○○○"),
        (t("Ferramenta em uso por outras pessoas", "Tool used by other people"), "●○○●●○○○○○"),
        (t("Código com agente de IA", "Coding with an AI agent"), "○○○○●○●●○○"),
        (t("Visão de ponta a ponta", "End-to-end view"), "●○○○●●○●○●"),
    ]
    mx = "".join(
        "<tr><td>%s</td>%s</tr>" % (r, "".join('<td>%s</td>' % ('<span class="d"></span>' if c == "●" else '<span class="o"></span>') for c in m))
        for r, m in rows)

    return f"""
<section id="{L}" lang="{t('pt-BR','en')}" class="page">
<div class="ruler" aria-hidden="true"></div>
<nav class="lang">{other}</nav>

<header class="mast">
  <div class="who">
    <img src="assets/foto-gabriela.jpg" width="104" height="104" alt="{t('Foto de Gabriela Dória','Photo of Gabriela Dória')}">
    <div>
      <p class="eyebrow">{t('Portfólio','Portfolio')} · <b>{t('gestão por indicadores, dados e IA aplicada','managing by metrics, data and applied AI')}</b> · {t('nov 2026','Nov 2026')}</p>
      <h1>Gabriela <em>Dória</em></h1>
      <p class="lede">{t('Engenharia Ambiental na Poli-USP e três anos de consultoria de gestão, de consultora a diretora. <b>Encontro o gargalo, construo a solução e meço se funcionou</b>: com metas e indicadores na gestão, e com dados, automação e IA nas ferramentas.','Environmental Engineering at Poli-USP, São Paulo, and three years of management consulting, from consultant to director. <b>I find the bottleneck, build the fix and measure whether it worked</b>: with goals and metrics in management, and with data, automation and AI in the tools.')}</p>
    </div>
  </div>
  <div class="contact">{t('Poli-USP · formatura dez/2028','Poli-USP · graduating Dec 2028')}<br>São Paulo · SP<br><a href="mailto:gabrielavsdoria@gmail.com">gabrielavsdoria@gmail.com</a><br><a href="{LI}">linkedin.com/in/gabriela-vs-doria</a><br><a href="{GH}">github.com/gabriela-doria</a></div>
</header>

<section class="figures" aria-label="{t('Números','Figures')}">
  <div class="fig"><b>94,9<span>%</span></b><small>{t('atingimento médio dos 14 resultados-chave da área de Projetos que dirigi (2025)','average attainment of the 14 key results in the Projects area I led (2025)')}</small></div>
  <div class="fig"><b>30 <span>/ 14</span></b><small>{t('reuniões com a ONG atendida: realizado / meta','meetings with the client NGO: actual / target')}</small></div>
  <div class="fig"><b>25</b><small>{t('pessoas usam o app que programei com Claude Code','people use the app I built with Claude Code')}</small></div>
  <div class="fig"><b>16</b><small>{t('agentes de IA que desenhei e opero','AI agents I designed and run')}</small></div>
</section>

<nav class="toc" aria-label="{t('Nesta página','On this page')}">
  <a href="#gestao{sid}"><b>1</b> {t('Gestão por indicadores','Managing by metrics')}</a>
  <a href="#ia{sid}"><b>2</b> {t('Dados, automação e IA','Data, automation and AI')}</a>
  <a href="#empreender{sid}"><b>3</b> {t('Empreendedorismo e repertório','Entrepreneurship and background')}</a>
  <a href="#ferramentas{sid}"><b>4</b> {t('Ferramentas e formação','Tools and education')}</a>
</nav>

<h2><b>{t('Como eu trabalho','How I work')}</b> · {t('o mesmo ciclo na gestão e na tecnologia','the same loop in management and in technology')}</h2>
<div class="cycle">
<svg viewBox="0 0 880 170" role="img" aria-label="{t('Ciclo: 1 Encontrar o gargalo, 2 Construir a solução, 3 Medir, e volta ao início','Loop: 1 Find the bottleneck, 2 Build the fix, 3 Measure, and back to the start')}">
  <defs><marker id="ah{sid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrh"/></marker></defs>
  <rect class="node" x="4" y="10" width="270" height="100" rx="5"/>
  <text class="num" x="20" y="42">1</text><text class="ttl" x="44" y="40">{t('Encontrar o gargalo','Find the bottleneck')}</text>
  <text class="sub" x="20" y="66">{t('diagnóstico, pesquisa, dados','diagnosis, surveys, data')}</text><text class="sub" x="20" y="82">{t('o que trava e por quê','what is stuck and why')}</text><text class="sub" x="20" y="98">{t('métrica antes da ferramenta','metric before the tool')}</text>
  <rect class="node" x="304" y="10" width="270" height="100" rx="5"/>
  <text class="num" x="320" y="42">2</text><text class="ttl" x="344" y="40">{t('Construir a solução','Build the fix')}</text>
  <text class="sub" x="320" y="66">{t('OKRs, processos, pessoas','OKRs, processes, people')}</text><text class="sub" x="320" y="82">{t('apps, automações, agentes de IA','apps, automations, AI agents')}</text><text class="sub" x="320" y="98">{t('feita para durar sem mim','built to last without me')}</text>
  <rect class="node hi" x="604" y="10" width="272" height="100" rx="5"/>
  <text class="num" x="620" y="42">3</text><text class="ttl" x="644" y="40">{t('Medir','Measure')}</text>
  <text class="sub" x="620" y="66">{t('realizado × meta, NPS, adesão','actual vs. target, NPS, adoption')}</text><text class="sub" x="620" y="82">{t('testes automáticos e contagens','automated tests and counts')}</text><text class="sub" x="620" y="98">{t('estimativa dita como estimativa','estimates labeled as estimates')}</text>
  <path class="arr" d="M276 60 H300" marker-end="url(#ah{sid})"/>
  <path class="arr" d="M576 60 H600" marker-end="url(#ah{sid})"/>
  <path class="arr" d="M740 112 V140 H140 V114" marker-end="url(#ah{sid})"/>
  <text class="loop" x="440" y="158" text-anchor="middle">{t('→ volto ao passo 1 com o que a medição mostrou','→ back to step 1 with what the measurement showed')}</text>
</svg>
<ol class="cyclist">
  <li><b>1 · {t('Encontrar o gargalo','Find the bottleneck')}</b>{t('diagnóstico, pesquisa e dados: o que trava e por quê','diagnosis, surveys and data: what is stuck and why')}</li>
  <li><b>2 · {t('Construir a solução','Build the fix')}</b>{t('OKRs, processos e pessoas; apps, automações e agentes de IA','OKRs, processes and people; apps, automations and AI agents')}</li>
  <li class="hi"><b>3 · {t('Medir','Measure')}</b>{t('realizado × meta, NPS, adesão, testes e contagens','actual vs. target, NPS, adoption, tests and counts')}</li>
  <li class="loop">{t('↺ volto ao passo 1 com o que a medição mostrou','↺ back to step 1 with what the measurement showed')}</li>
</ol>
</div>

<h2>{t('Trajetória','Path')} · 2020 – 2026</h2>
<div class="tl">
<svg viewBox="0 0 880 96" role="img" aria-label="{t('Linha do tempo de 2020 a 2026','Timeline from 2020 to 2026')}">
  <line class="axis" x1="20" y1="32" x2="860" y2="32"/>
  <circle cx="45" cy="32" r="6" class="hi"/><text class="y hi" x="45" y="18" text-anchor="middle">{t('out/2020','Oct 2020')}</text><text class="hi" x="45" y="52" text-anchor="middle">Megève</text><text x="45" y="65" text-anchor="middle">{t('fundadora','founder')}</text>
  <circle cx="160" cy="32" r="5"/><text class="y" x="160" y="18" text-anchor="middle">2022</text><text x="160" y="52" text-anchor="middle">Summer@INSEAD</text>
  <circle cx="275" cy="32" r="6" class="hi"/><text class="y hi" x="275" y="18" text-anchor="middle">{t('mar/2023','Mar 2023')}</text><text class="hi" x="275" y="52" text-anchor="middle">Poli Social</text><text x="275" y="65" text-anchor="middle">{t('consultora','consultant')}</text>
  <circle cx="390" cy="32" r="6" class="hi"/><text class="y hi" x="390" y="18" text-anchor="middle">{t('nov/2023','Nov 2023')}</text><text class="hi" x="390" y="52" text-anchor="middle">{t('Gerente','Manager')}</text><text x="390" y="65" text-anchor="middle">{t('time de 5','team of 5')}</text>
  <circle cx="505" cy="32" r="6" class="hi"/><text class="y hi" x="505" y="18" text-anchor="middle">{t('nov/2024','Nov 2024')}</text><text class="hi" x="505" y="52" text-anchor="middle">{t('Diretora','Director')}</text><text x="505" y="65" text-anchor="middle">{t('OKRs da área','area OKRs')}</text>
  <circle cx="620" cy="32" r="6" class="hi"/><text class="y hi" x="620" y="18" text-anchor="middle">{t('set/2026','Sep 2026')}</text><text class="hi" x="620" y="52" text-anchor="middle">Areia Viva</text><text x="620" y="65" text-anchor="middle">Personal OS</text>
  <circle cx="735" cy="32" r="6" class="hi"/><text class="y hi" x="735" y="18" text-anchor="middle">{t('out/2026','Oct 2026')}</text><text class="hi" x="735" y="52" text-anchor="middle">Rota do</text><text x="735" y="65" text-anchor="middle">Excedente</text>
  <circle cx="845" cy="32" r="6" class="hi"/><text class="y hi" x="845" y="18" text-anchor="end">{t('nov/2026','Nov 2026')}</text><text class="hi" x="845" y="52" text-anchor="end">{t('app em uso','app in use')}</text><text x="845" y="65" text-anchor="end">Campus</text>
</svg>
<ul class="tlist">
  <li class="hi"><b>{t('out/2020','Oct 2020')}</b>Chocolates Megève · {t('fundadora','founder')}</li>
  <li><b>2022</b>Summer@INSEAD</li>
  <li class="hi"><b>{t('mar/2023','Mar 2023')}</b>Poli Social · {t('consultora','consultant')}</li>
  <li class="hi"><b>{t('nov/2023','Nov 2023')}</b>{t('Gerente de Projetos, time de 5','Project Manager, team of 5')}</li>
  <li class="hi"><b>{t('nov/2024','Nov 2024')}</b>{t('Diretora de Projetos, OKRs da área','Director of Projects, area OKRs')}</li>
  <li class="hi"><b>{t('set/2026','Sep 2026')}</b>Areia Viva · Personal OS</li>
  <li class="hi"><b>{t('out/2026','Oct 2026')}</b>Rota do Excedente</li>
  <li class="hi"><b>{t('nov/2026','Nov 2026')}</b>{t('App do Areia Viva em uso · Campus de energia','Areia Viva app in use · Campus de energia')}</li>
</ul>
</div>

<h2><b>{t('Competências × casos','Skills × cases')}</b> · {t('onde está a prova de cada uma','where the proof of each one is')}</h2>
<div class="mxwrap">
<table class="mx">
<thead><tr><th></th>{''.join(f'<th><span>{c}</span></th>' for c in cols)}</tr></thead>
<tbody>{mx}</tbody>
<tfoot><tr><td colspan="11"><span class="d"></span> {t('exercitada no caso','used in the case')} &nbsp; <span class="o"></span> {t('não é o foco','not the focus')}</td></tr></tfoot>
</table>
</div>

<!-- ===================== PARTE 1 ===================== -->
<div class="part" id="gestao{sid}"><span>1</span><div><h2 class="ph">{t('Gestão por indicadores','Managing by metrics')}</h2><p>{t('Poli Social, a consultoria de gestão pro bono da Poli-USP para ONGs. Três anos, de consultora a diretora de Projetos.','Poli Social, Poli-USP\'s pro bono management consulting group for NGOs. Three years, from consultant to Director of Projects.')}</p></div></div>
<div class="cases">

{case('diretoria','Poli Social · 2025', t('Diretora de Projetos<br>nov/2024 – nov/2025','Director of Projects<br>Nov 2024 – Nov 2025'), t('OKRs e KPIs','OKRs and KPIs'),
 t('Gerir uma área inteira por indicadores','Running a whole area by metrics'),
 flow(t('Responder pelo método, pelas pessoas, pelo portfólio de projetos e pela relação com a ONG atendida.','Answer for the method, the people, the project portfolio and the relationship with the client NGO.'),
      t('Desenhei os OKRs da área: 3 objetivos e 15 resultados-chave. Acompanhamento quinzenal e revisão do plano a cada quadrimestre.','I designed the area\'s OKRs: 3 objectives and 15 key results. Fortnightly tracking and a plan review every four months.'),
      t('Indicadores, relacionamento e NPS da ONG acima da meta no fim do ano.','Metrics, relationship and NGO NPS above target at year end.'))
 + '<div class="okr">'
 + f'<div class="o1"><span class="k">OKR 1 · {t("pessoas","people")}</span>{t("Pertencimento e desenvolvimento dos consultores","Belonging and growth of the consultants")}</div>'
 + f'<div class="o1 hi"><span class="k">OKR 2 · {t("cliente","client")}</span>{t("Impacto notório na realidade da ONG","Visible impact on the NGO")}</div>'
 + f'<div class="o1"><span class="k">OKR 3 · {t("processo","process")}</span>{t("Profissionalizar a área com planejamento e conhecimento compartilhado","Professionalize the area with planning and shared knowledge")}</div>'
 + '</div>'
 + '<div class="bars">'
 + bar(t('14 resultados-chave · atingimento médio','14 key results · average attainment'), 94.9, '94,9%')
 + bar(t('Reuniões com a ONG · meta 14','Meetings with the NGO · target 14'), 100, '30', goal=46.7)
 + bar(t('Encontros presenciais · meta 4','In-person visits · target 4'), 100, '5', goal=80)
 + bar(t('NPS da ONG · 3 ciclos','NGO NPS · 3 cycles'), 93.3, '100·80·100')
 + bar(t('Reuniões de planejamento das OKRs','OKR planning meetings'), 100, '4 / 4')
 + '</div>'
 + f'<figure class="shot wide"><a href="assets/okr-projetos-2025-planilha.jpg"><img src="assets/okr-projetos-2025-planilha.jpg" width="2250" height="458" loading="lazy" alt="{t("Print da planilha de OKRs da área de Projetos da Poli Social em 2025, com objetivos, resultados-chave, valores inicial, atual e esperado e percentual","Screenshot of the Poli Social Projects area OKR spreadsheet for 2025, with objectives, key results, starting, current and target values and percentage")}"></a><figcaption><b>{t("A ferramenta","The tool")}</b> · {t("planilha de OKRs da área de Projetos, 2025: cada resultado-chave com valor inicial, atual e esperado (clique para ampliar)","Projects area OKR spreadsheet, 2025: each key result with starting, current and target value (click to enlarge)")}</figcaption></figure>'
 + chips([t('OKRs','OKRs'), 'KPIs', 'NPS'], ['Excel', 'Google Sheets', t('rituais quinzenais','fortnightly check-ins')])
 + f'<p class="how">{t("Como medi: média do atingimento dos 14 resultados-chave da área de Projetos, cada um como valor atual ÷ valor esperado, sem limitar a 100% (meta superada conta acima de 100%, como as 30 reuniões contra 14). A coluna Percentual da planilha limita cada um a 100%. Fonte: planilha de OKRs da área e relatório de atividades 2025 da Poli Social.","How I measured: the average attainment of the Projects area's 14 key results, each as current ÷ target value, not capped at 100% (an exceeded target counts above 100%, like 30 meetings against 14). The spreadsheet's Percentage column caps each one at 100%. Source: the area OKR spreadsheet and the Poli Social 2025 activity report.")}</p>')}

{case('edital','Poli Social · 2025', t('Edital de consultoria<br>condução do processo','Consulting call<br>ran the process'), t('decisão com critério','criteria-based decision'),
 t('Escolher o cliente do ano com critério, não com intuição','Choosing the year\'s client on criteria, not gut feeling'),
 flow(t('Escolher, entre as inscritas, a ONG que receberia a consultoria do ano.','Choose, among the applicants, the NGO that would receive the year\'s consulting.'),
      t('Edital e contrato; análise da documentação institucional, financeira e jurídica; entrevistas; avaliação multicritério.','Call and contract; review of institutional, financial and legal documents; interviews; multi-criteria assessment.'),
      t('Escolha defendida por critérios explícitos, de 18 inscrições para 1 ONG.','A choice backed by explicit criteria, from 18 applications to 1 NGO.'))
 + '<div class="funnel">'
 + f'<div class="fun"><span>{t("Inscrições analisadas","Applications reviewed")}</span><span class="seg" style="width:100%">18</span></div>'
 + f'<div class="fun"><span>{t("Entrevistas","Interviews")}</span><span class="seg l2" style="width:33.3%">6</span></div>'
 + f'<div class="fun"><span>{t("Selecionada","Selected")}</span><span class="seg l3" style="width:9%">1</span></div>'
 + '</div>'
 + chips([t('avaliação multicritério','multi-criteria assessment')], [t('análise financeira','financial analysis'), t('análise jurídica','legal review')]))}

{case('inovacao','Poli Social · 2025', t('Grupo de Inovação<br>criado do zero','Innovation Group<br>built from scratch'), t('inovação','innovation'),
 t('Dar dono às ideias que surgiam e morriam na entidade','Giving an owner to ideas that came up and died'),
 flow(t('Ideias surgiam nas reuniões e morriam sem dono, sem método e sem prazo.','Ideas came up in meetings and died with no owner, method or deadline.'),
      t('Desenhei o modelo do Grupo de Inovação, levei a uma assembleia de 40 membros e liderei 7 pessoas do diagnóstico à solução, priorizada por matriz impacto-esforço.','I designed the Innovation Group model, took it to a 40-member assembly and led 7 people from diagnosis to solution, prioritized with an impact-effort matrix.'),
      t('Modelo aprovado por 84,2%; 4 propostas levadas à votação e proposta final aprovada por 83,3%, em cerca de 8 meses.','Model approved by 84.2%; 4 proposals put to a vote and the final proposal approved by 83.3%, in about 8 months.'))
 + '<div class="eq">'
 + f'<div class="box"><span class="k">{t("1 · modelo","1 · model")}</span>{t("papéis, ritos e regras","roles, rituals and rules")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("2 · assembleia","2 · assembly")}</span>{t("40 membros votam","40 members vote")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("3 · diagnóstico","3 · diagnosis")}</span>{t("time de 7 levanta problemas","team of 7 maps problems")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("4 · priorização","4 · prioritization")}</span>{t("matriz impacto-esforço","impact-effort matrix")}</div><span class="op">→</span>'
 + f'<div class="box res"><span class="k">{t("5 · proposta","5 · proposal")}</span>{t("aprovada em assembleia","approved by the assembly")}</div>'
 + '</div>'
 + '<div class="bars">'
 + bar(t('Modelo aprovado em assembleia','Model approved by the assembly'), 84.2, '84,2%', amb=True)
 + bar(t('Proposta final aprovada','Final proposal approved'), 83.3, '83,3%', amb=True)
 + '</div>'

 + '<div class="gallery2">'
 + f'<figure class="shot"><a href="assets/inovacao-problematica.jpg"><img src="assets/inovacao-problematica.jpg" width="1100" height="619" loading="lazy" alt="{t("Slide: a dificuldade de inovar dentro de estruturas que priorizam eficiência, e a proposta de criar estruturas de experimentação","Slide: the difficulty of innovating inside structures built for efficiency, and the proposal to create structures for experimentation")}"></a><figcaption><b>{t("O problema","The problem")}</b> · {t("Institucionalização da Inovação, 2025","Institutionalizing Innovation, 2025")}</figcaption></figure>'
 + f'<figure class="shot"><a href="assets/inovacao-metodologia-sociagil.jpg"><img src="assets/inovacao-metodologia-sociagil.jpg" width="1100" height="619" loading="lazy" alt="{t("Slide: metodologia SociÁgil, com ciclos de MVP até a inovação consolidada nos processos","Slide: the SociÁgil method, with MVP cycles until the innovation is built into the processes")}"></a><figcaption><b>{t("O método","The method")}</b> · {t("ciclos curtos de MVP até virar processo","short MVP cycles until it becomes a process")}</figcaption></figure>'
 + f'<figure class="shot"><a href="assets/inovacao-criterios-de-decisao.jpg"><img src="assets/inovacao-criterios-de-decisao.jpg" width="1100" height="619" loading="lazy" alt="{t("Slide: critérios de decisão para escolher uma proposta: prioridade, viabilidade e resiliência, potencial de impacto","Slide: decision criteria to choose a proposal: priority, feasibility and resilience, impact potential")}"></a><figcaption><b>{t("Os critérios","The criteria")}</b> · {t("como a assembleia escolheu entre as propostas","how the assembly chose between proposals")}</figcaption></figure>'
 + f'<figure class="shot"><a href="assets/inovacao-proposta-pontos-de-atencao.jpg"><img src="assets/inovacao-proposta-pontos-de-atencao.jpg" width="1100" height="619" loading="lazy" alt="{t("Slide: proposta Pontos de Atenção, com objetivo, problema, o que será feito, prazo e responsável","Slide: the Points of Attention proposal, with goal, problem, what will be done, deadline and owner")}"></a><figcaption><b>{t("Uma das 4 propostas","One of the 4 proposals")}</b> · {t("problema, ação, prazo e responsável","problem, action, deadline and owner")}</figcaption></figure>'
 + '</div>'

 + f'<h4 class="sub">{t("Da proposta à implementação","From proposal to implementation")}</h4>'
 + '<div class="gantt">'
 + ''.join(f'<span style="flex:{w}" class="{c}"><b>{lab}</b><small>{w} {t("sem","wk")}</small></span>' for w,c,lab in [(2,'g0',t('preparo','prep')),(4,'g1',t('ciclo 0','cycle 0')),(6,'g2',t('ciclo 1','cycle 1')),(6,'g2',t('ciclo 2','cycle 2')),(6,'g2',t('ciclo 3','cycle 3')),(4,'g1',t('finalização','wrap-up')),(4,'g3','feedbacks')])
 + '</div>'
 + f'<p class="how">{t("Cronograma planejado do projeto-piloto: mar a dez/2025, cerca de 30 reuniões semanais do grupo, descontadas as semanas de prova e os feriados.","Planned pilot timeline: Mar to Dec 2025, about 30 weekly group meetings, net of exam weeks and holidays.")}</p>'
 + '<div class="eq">'
 + f'<div class="box"><span class="k">{t("4 propostas","4 proposals")}</span>{t("apresentadas à entidade","presented to the organization")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("feedback","feedback")}</span>{t("respostas do formulário agrupadas por tema e frequência","form answers grouped by theme and frequency")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("escolha","choice")}</span>{t("Pontos de Atenção","Points of Attention")}</div><span class="op">→</span>'
 + f'<div class="box res"><span class="k">{t("versão 1.1","version 1.1")}</span>{t("tabela de pontos, fluxogramas e planilha de acompanhamento","points table, flowcharts and tracking sheet")}</div>'
 + '</div>'
 + '<div class="gallery3">'
 + f'<figure class="shot c1"><a href="assets/inovacao-proposta-implementacao-capa.jpg"><img src="assets/inovacao-proposta-implementacao-capa.jpg" width="1100" height="807" loading="lazy" alt="{t("Primeira página do documento Proposta de Implementação: Pontos de atenção","First page of the document Implementation Proposal: Points of Attention")}"></a><figcaption><b>{t("O documento","The document")}</b> · {t("proposta de implementação, versão 1.1","implementation proposal, version 1.1")}</figcaption></figure>'
 + f'<figure class="shot c2"><a href="assets/inovacao-fluxograma-pontuacao.jpg"><img src="assets/inovacao-fluxograma-pontuacao.jpg" width="920" height="342" loading="lazy" alt="{t("Fluxograma: da infração à advertência, feedback 1:1 com o líder, feedback com a diretoria de RH e desligamento, conforme a pontuação","Flowchart: from infraction to warning, 1:1 feedback with the leader, feedback with the HR director and dismissal, by points")}"></a><figcaption><b>{t("Regra clara","A clear rule")}</b> · {t("o que acontece a cada faixa de pontos","what happens at each points band")}</figcaption></figure>'
 + f'<figure class="shot c3"><a href="assets/inovacao-fluxograma-registro.jpg"><img src="assets/inovacao-fluxograma-registro.jpg" width="990" height="317" loading="lazy" alt="{t("Fluxograma do registro de faltas: antes do evento e no dia do evento, tudo vai para a planilha","Absence logging flowchart: before the event and on the day, everything goes to the sheet")}"></a><figcaption><b>{t("Registro","Logging")}</b> · {t("antes e no dia de cada reunião","before and on the day of each meeting")}</figcaption></figure>'
 + '</div>'
 + chips([t('matriz impacto-esforço','impact-effort matrix')], [t('facilitação','facilitation'), t('gestão de pessoas','people management'), t('RACI para as tarefas do grupo','RACI for the group tasks'), t('fluxogramas','flowcharts')]))}

{case('palavras-de-paz','Poli Social · 2024', t('Gerente de Projetos<br>time de 5 · 10 meses','Project Manager<br>team of 5 · 10 months'), t('dados de gestão','management data'),
 t('Dar números a uma ONG grande em alcance e pequena em estrutura','Giving numbers to an NGO that is large in reach and small in structure'),
 flow(t('A ONG Palavras de Paz tinha cerca de 250 voluntários e atendia de 6 a 13 mil pessoas por ano, sem dados de gestão para decidir.','The NGO Palavras de Paz had about 250 volunteers and served 6,000 to 13,000 people a year, with no management data to decide on.'),
      t('Liderei 5 consultores do diagnóstico à entrega: pesquisa com voluntários, nova Missão, Visão e Valores, metas em OKRs, pesquisa de clima mensal e dashboard em Power BI com 2021 a 2024.','I led 5 consultants from diagnosis to delivery: a volunteer survey, new Mission, Vision and Values, OKR goals, a monthly climate survey and a Power BI dashboard covering 2021 to 2024.'),
      t('19 entregáveis no prazo, NPS da ONG de 100 e uma linha de base para medir a evolução.','19 deliverables on time, NGO NPS of 100 and a baseline to measure progress.'))
 + '<div class="bars">'
 + bar(t('Voluntários que conheciam os objetivos do ano','Volunteers who knew the year\'s goals'), 21.9, '21,9%', amb=True)
 + bar(t('NPS da ONG no fim do projeto','NGO NPS at project end'), 100, '100')
 + '</div>'
 + nums([('250', t('voluntários na ONG','volunteers at the NGO')), ('32', t('respostas na pesquisa de diagnóstico','responses to the diagnosis survey')), ('19', t('entregáveis','deliverables')), ('2021–24', t('anos no dashboard','years in the dashboard'))])
 + chips(['Power BI', t('pesquisa de clima','climate survey'), 'OKRs'], [t('diagnóstico','diagnosis'), 'MVV'])
 + f'<p class="how">{t("O diagnóstico mostrou que só 21,9% dos voluntários conheciam os objetivos do ano: foi o ponto de partida das metas em OKRs.","The diagnosis showed only 21.9% of volunteers knew the year\'s goals: that was the starting point for the OKR goals.")}</p>')}

{case('novos-valores','Poli Social · 2023', t('Consultora de Projetos<br>mar – nov/2023','Project Consultant<br>Mar – Nov 2023'), t('receita','revenue'),
 t('Diversificar a receita de uma ONG que dependia de dois doadores','Diversifying revenue for an NGO that relied on two donors'),
 flow(t('No Instituto Novos Valores, 90% dos custos vinham de dois doadores.','At Instituto Novos Valores, 90% of costs came from two donors.'),
      t('Criei a identidade de marca (manual de 24 páginas) para a captação, e mapeei as exigências e acompanhei o cadastro na Nota Fiscal Paulista.','I created the brand identity (24-page manual) for fundraising, and mapped the requirements and followed the registration in the Nota Fiscal Paulista program.'),
      t('Marca usada na captação de investidores e voluntários e uma nova fonte de receita em cadastro.','A brand used to attract investors and volunteers, and a new revenue source in registration.'))
 + nums([('90%', t('dos custos vinham de 2 doadores','of costs came from 2 donors')), ('24', t('páginas no manual de marca','pages in the brand manual'))], 'two'))}
</div>

<!-- ===================== PARTE 2 ===================== -->
<div class="part" id="ia{sid}"><span>2</span><div><h2 class="ph">{t('Dados, automação e IA','Data, automation and AI')}</h2><p>{t('O mesmo ciclo levado para a tecnologia: um app em uso, agentes que trabalho todo dia e demos com dados fictícios.','The same loop applied to technology: an app in use, agents I work with every day and demos with fictitious data.')}</p></div></div>
<div class="cases">

{case('areia-viva','Areia Viva · 2026', t('extensão USP, voluntária<br>Drive set/2026 · app nov/2026','USP extension project, volunteer<br>Drive Sep 2026 · app Nov 2026'), t('em uso','in use'),
 t('Um app de gestão que 25 pessoas usam, programado com Claude Code','A management app 25 people use, built with Claude Code'),
 flow(t('As horas eram registradas no computador, muitas vezes meses depois; tarefas sem dono e um Drive sem regra de nome, pasta nem acesso.','Hours were logged on a computer, often months later; tasks had no owner and the Drive had no rule for names, folders or access.'),
      t('Reestruturei o Drive com matriz de decisão e scripts que simulam antes de rodar. Construí o app: horas pelo celular, tarefas com dono e prazo, eventos e mapa do Drive, com login Google e acesso por papel.','I restructured the Drive with a decision matrix and scripts that simulate before running. I built the app: hours from the phone, tasks with owner and deadline, events and a Drive map, with Google sign-in and role-based access.'),
      t('App em uso por 25 pessoas desde 13/11/2026. As horas passaram a ser registradas no mesmo dia.','App used by 25 people since 13 Nov 2026. Hours are now logged the same day.'))
 + '<div class="eq">'
 + f'<div class="box"><span class="k">{t("set/2026","Sep 2026")}</span>{t("Drive reestruturado","Drive restructured")}</div><span class="op">→</span>'
 + f'<div class="box"><span class="k">{t("1ª versão","1st version")}</span>{t("Mapa do Drive em Apps Script","Drive Map on Apps Script")}</div><span class="op">→</span>'
 + f'<div class="box res"><span class="k">{t("nov/2026","Nov 2026")}</span>{t("App em Firebase: painel, tarefas, horas, eventos","Firebase app: dashboard, tasks, hours, events")}</div>'
 + '</div>'
 + nums([('25', t('pessoas usam o app','people use the app')), ('32', t('testes das regras de acesso','access-rule tests')), ('124', t('arquivos renomeados','files renamed')), ('33', t('contas com acesso por papel','role-based accounts')), ('62', t('pastas na nova estrutura','folders in the new structure'))])
 + '<div class="gallery">'
 + f'<figure class="shot g1"><a href="assets/app-areia-viva-painel.jpg"><img src="assets/app-areia-viva-painel.jpg" width="1100" height="760" loading="lazy" alt="{t("Painel pessoal do app: próxima tarefa, horas que faltam para a meta e próximo evento","App personal dashboard: next task, hours left to the goal and next event")}"></a><figcaption><b>{t("Meu painel","My dashboard")}</b> · {t("o que fazer agora, horas e próximo evento","what to do now, hours and next event")}</figcaption></figure>'
 + f'<figure class="shot g2"><a href="assets/app-areia-viva-tarefas.jpg"><img src="assets/app-areia-viva-tarefas.jpg" width="1100" height="760" loading="lazy" alt="{t("Lista de tarefas do app com frente, responsável, prazo e estado","App task list with workstream, owner, deadline and status")}"></a><figcaption><b>{t("Tarefas","Tasks")}</b> · {t("dono, prazo e estado; lista, quadro e cronograma","owner, deadline and status; list, board and timeline")}</figcaption></figure>'
 + f'<figure class="shot g3"><a href="assets/app-areia-viva-horas.jpg"><img src="assets/app-areia-viva-horas.jpg" width="1100" height="620" loading="lazy" alt="{t("Tela de horas: quanto falta para a meta e ritmo por semana","Hours screen: how much is left to the goal and weekly pace")}"></a><figcaption><b>{t("Horas","Hours")}</b> · {t("meta, ritmo semanal e lançamentos","goal, weekly pace and entries")}</figcaption></figure>'
 + f'<figure class="shot g4 phone"><a href="assets/app-areia-viva-celular.jpg"><img src="assets/app-areia-viva-celular.jpg" width="390" height="844" loading="lazy" alt="{t("O app no celular","The app on a phone")}"></a><figcaption><b>{t("No celular","On the phone")}</b> · {t("onde as horas são lançadas","where hours are logged")}</figcaption></figure>'
 + '</div>'
 + f'<p class="how">{t("Telas no modo de demonstração, com dados fictícios. Como medi: as contagens saem dos registros dos scripts; a mudança no dia a dia ainda não tem número.","Screens in demo mode, with fictitious data. How I measured: the counts come from the scripts\' logs; the day-to-day change has no number yet.")}</p>'
 + chips(['Claude Code', 'Firebase'], ['Google Apps Script', t('API do Drive','Drive API'), t('4 prompts reutilizáveis','4 reusable prompts')])
 + f'<div class="link"><a href="{GH}/student-project-ops-ai">{t("repositório","repository")} · student-project-ops-ai</a></div>')}

{case('personal-os','Personal OS · 2026', t('projeto pessoal<br>desde set/2026','personal project<br>since Sep 2026'), t('agentes','agents'),
 t('16 agentes de IA que organizam faculdade, extensão e busca de estágio','16 AI agents that run coursework, extension work and the internship search'),
 flow(t('Informação espalhada em vários sistemas. O gargalo era coordenar: o que vence primeiro e onde está cada arquivo.','Information spread across systems. The bottleneck was coordination: what is due first and where each file is.'),
      t('Escrevi 16 skills do Claude que leem as fontes e propõem ações, mais um radar que dá nota de 0 a 100 a cada vaga.','I wrote 16 Claude skills that read the sources and propose actions, plus a radar that scores each opening from 0 to 100.'),
      t('273 e-mails arquivados e 163 arquivos renomeados na primeira rodada.','273 emails archived and 163 files renamed in the first run.'))
 + '<div class="arch">'
 + f'<div class="col"><span class="k">{t("Fontes","Sources")}</span><ul><li>Gmail</li><li>{t("Google Agenda","Google Calendar")}</li><li>Drive · Docs · Sheets</li><li>Moodle · Classroom</li><li>{t("Portais de vagas","Job boards")}</li></ul></div>'
 + '<div class="ar">→</div>'
 + f'<div class="col hi"><span class="k">{t("16 agentes (skills)","16 agents (skills)")}</span><ul><li>{t("Radar de estágios","Internship radar")}</li><li>{t("Preparar processo seletivo","Selection process prep")}</li><li>{t("Resumo da manhã","Morning brief")}</li><li>{t("Proposta da semana","Weekly plan")}</li><li>Moodle → Drive + {t("Agenda","Calendar")}</li><li>…</li></ul></div>'
 + '<div class="ar">→</div>'
 + f'<div class="col"><span class="k">{t("Saídas","Outputs")}</span><ul><li>{t("Planilha de prioridade das vagas","Openings priority sheet")}</li><li>{t("Agenda em blocos de 25 min","Calendar in 25-min blocks")}</li><li>{t("Docs de preparação","Prep docs")}</li><li>{t("Painel diário","Daily dashboard")}</li></ul></div>'
 + '</div>'
 + f'<div class="archfoot"><span class="me">{t("Eu valido cada proposta antes de virar ação","I approve each proposal before it becomes an action")}</span><span>{t("Mapa do Sistema: 275 peças e 252 mudanças registradas","System Map: 275 parts and 252 logged changes")}</span><span>{t("2 rotinas agendadas: resumo (seg–sex 6h) e proposta da semana (dom 18h)","2 scheduled routines: brief (Mon–Fri 6am) and weekly plan (Sun 6pm)")}</span></div>'
 + nums([('273', t('e-mails arquivados','emails archived')), ('163', t('arquivos renomeados','files renamed')), ('~80 min', t('por semana na coleta de aulas (estimativa)','a week on course materials (estimate)')), ('275', t('peças no Mapa do Sistema','parts in the System Map'))])
 + chips([t('Claude (skills, MCP, tarefas agendadas)','Claude (skills, MCP, scheduled tasks)')], ['Google Apps Script', 'Python'])
 + f'<p class="how">{t("Como medi: contagem nos registros de execução (29/10/2026). O tempo poupado é estimativa minha, sem linha de base.","How I measured: counts from the run logs (29 Oct 2026). Time saved is my own estimate, with no baseline.")}</p>'
 + f'<div class="link"><a href="{GH}/personal-os-claude">{t("repositório","repository")} · personal-os-claude</a> · <a href="{GH}/personal-os-claude/tree/main/skills/radar-estagios">{t("radar de estágios","internship radar")}</a></div>')}

{case('campus','Campus de energia', t('exercício pessoal<br>nov/2026','personal exercise<br>Nov 2026'), t('dados fictícios','fictitious data'),
 t('Qual cliente aproveita a energia que a rede não recebe','Which customer uses the energy the grid can\'t take'),
 flow(t('Um parque eólico e solar gera mais do que cabe na linha de conexão.','A wind and solar park produces more than its grid connection can carry.'),
      t('Simulação hora a hora com programação linear, preço-sombra e matriz de decisão para 3 clientes. Problema e critérios meus; código com o Claude.','Hour-by-hour simulation with linear programming, shadow prices and a decision matrix for 3 customers. Problem and criteria mine; code with Claude.'),
      t('Com um data center ao lado, o parque aproveita toda a energia e a receita da semana sobe 96%.','With a data center next door, the park uses all its energy and weekly revenue rises 96%.'))
 + '<div class="bars">'
 + bar(t('Sem cliente ao lado','No customer next door'), 64.1, '64,1%', amb=True)
 + bar(t('Com data center','With a data center'), 100, '100%')
 + '</div>'
 + f'<figure class="shot wide"><a href="assets/campus-destino-da-energia.jpg"><img src="assets/campus-destino-da-energia.jpg" width="1100" height="757" loading="lazy" alt="{t("Gráfico de áreas: para onde vai a energia de cada hora, sem cliente (64,1% aproveitada) e com data center (100%)","Area chart: where each hour\'s energy goes, with no customer (64.1% used) and with a data center (100%)")}"></a><figcaption><b>{t("Para onde vai a energia de cada hora","Where each hour\'s energy goes")}</b> · {t("sem cliente, a parte cinza é energia cortada; com o data center, ela some (3 primeiros dias, dados fictícios)","with no customer, the grey area is curtailed energy; with the data center, it disappears (first 3 days, fictitious data)")}</figcaption></figure>'
 + f'<figure class="shot wide"><a href="assets/campus-nota-dos-clientes.jpg"><img src="assets/campus-nota-dos-clientes.jpg" width="1100" height="317" loading="lazy" alt="{t("Barras: nota final de cada cliente na matriz de decisão: data center 0,72, indústria de turno diurno 0,36, eletrolisador de hidrogênio 0,29","Bars: final score of each customer in the decision matrix: data center 0.72, day-shift industry 0.36, hydrogen electrolyzer 0.29")}"></a><figcaption><b>{t("Matriz de decisão","Decision matrix")}</b> · {t("nota final de cada cliente, de 0 a 1","final score of each customer, from 0 to 1")}</figcaption></figure>'
 + chips([t('Claude (agente de código)','Claude (coding agent)')], ['Python', 'SciPy', t('programação linear','linear programming')])
 + f'<p class="how">{t("Como medi: 6 testes automáticos, entre eles a conta à mão contra o modelo e o preço-sombra com 1 MW a mais e a menos.","How I measured: 6 automated tests, including a hand calculation against the model and the shadow price at ±1 MW.")}</p>'
 + f'<div class="link"><a href="{GH}/campus-de-energia">{t("repositório","repository")} · campus-de-energia</a></div>')}

{case('rota','Rota do Excedente', t('case de desafio de IA<br>out/2026','AI challenge case<br>Oct 2026'), t('dados fictícios','fictitious data'),
 t('Comida que sobra em restaurantes até cozinhas solidárias','Surplus restaurant food to community kitchens'),
 flow(t('Restaurantes têm comida sobrando e as cozinhas não têm como buscar. Hipótese: falta transporte.','Restaurants have surplus food and kitchens can\'t collect it. Hypothesis: transport is missing.'),
      t('Algoritmo que agrupa restaurantes em rotas, calcula o custo por kg e descarta rota que não se paga. Página com premissas editáveis.','An algorithm that groups restaurants into routes, computes cost per kg and drops routes that don\'t pay off. A page with editable assumptions.'),
      t('No exemplo, 128 kg resgatados a R$ 1,64 por kg, contra R$ 12,00 para comprar.','In the example, 128 kg rescued at R$ 1.64 per kg, versus R$ 12.00 to buy.'))
 + '<div class="funnel">'
 + f'<div class="fun"><span>{t("Restaurantes","Restaurants")}</span><span class="seg" style="width:100%">16</span></div>'
 + f'<div class="fun"><span>{t("Rotas","Routes")}</span><span class="seg l2" style="width:37.5%">6</span></div>'
 + f'<div class="fun"><span>{t("Resgatados","Rescued")}</span><span class="seg l3" style="width:60%">128 kg</span></div>'
 + '</div><div class="bars">'
 + bar(t('Custo por kg, pela rota','Cost per kg, by route'), 13.7, 'R$ 1,64')
 + bar(t('Custo por kg, comprando','Cost per kg, buying'), 100, 'R$ 12,00', amb=True)
 + '</div>'
 + f'<figure class="shot wide"><a href="https://gabriela-doria.github.io/rota-do-excedente/"><img src="assets/rota-do-excedente-demo.jpg" width="1100" height="739" loading="lazy" alt="{t("Tela da demo: resultado do dia (128 kg, 6 rotas, 16,3 km, R$ 1,64 por kg) e mapa com as rotas até duas cozinhas","Demo screen: the day\'s result (128 kg, 6 routes, 16.3 km, R$ 1.64 per kg) and a map with routes to two kitchens")}"></a><figcaption><b>{t("A demo","The demo")}</b> · {t("resultado do dia, rotas e mapa; clique para abrir a versão ao vivo (dados fictícios)","the day\'s result, routes and map; click to open the live version (fictitious data)")}</figcaption></figure>'
 + chips([t('Claude (agente de código)','Claude (coding agent)')], ['JavaScript', 'Leaflet · OpenStreetMap'])
 + f'<p class="how">{t("Os valores em reais são hipóteses; proponho um piloto de 4 semanas para medir em campo.","The amounts are hypotheses; I propose a 4-week field pilot.")}</p>'
 + f'<div class="link"><a href="https://gabriela-doria.github.io/rota-do-excedente/">{t("demo ao vivo","live demo")}</a> · <a href="{GH}/rota-do-excedente">{t("repositório","repository")}</a></div>')}

{case('qgis', t('Análise espacial','Spatial analysis'), t('Geoprocessamento, Poli-USP<br>1º sem/2026 · grupo de 3','Geoprocessing, Poli-USP<br>1st sem 2026 · group of 3'), t('dados públicos','public data'),
 t('Metrô, renda e área construída em São Paulo, no QGIS','Metro, income and built area in São Paulo, in QGIS'),
 flow(t('A renda dos distritos acompanha o acesso ao metrô? Onde a cidade mais cresceu de 2010 a 2022?','Does district income follow metro access? Where did the city grow most from 2010 to 2022?'),
      t('Cruzei Censo 2022, Pesquisa OD 2023 e IPTU com raios de 800 m nas 94 estações. Claude como guia de método e código.','I combined the 2022 census, 2023 travel survey and property tax data with 800 m buffers around 94 stations. Claude as a method and code guide.'),
      t('Em 46 dos 96 distritos, nenhum morador está a até 800 m de uma estação.','In 46 of 96 districts, no resident lives within 800 m of a station.'))
 + '<div class="bars">'
 + bar(t('Distritos sem metrô a 800 m','Districts with no metro within 800 m'), 47.9, '46 / 96', amb=True)
 + bar(t('Área construída, Lapa','Built area, Lapa'), 100, '+25,5%')
 + bar(t('Área construída, Capela do Socorro','Built area, Capela do Socorro'), 66.7, '+17,0%')
 + '</div>'
 + chips([t('Claude (guia de método)','Claude (method guide)')], ['QGIS', 'Python · geopandas', 'Google Earth Engine'])
 + f'<p class="how">{t("Trabalho em grupo; os mapas citados são os que eu fiz.","Group work; the maps cited are the ones I made.")}</p>'
 + f'<div class="link"><a href="{GH}/analise-espacial-qgis-sp">{t("repositório com os mapas","repository with the maps")}</a></div>')}
</div>

<!-- ===================== PARTE 3 ===================== -->
<div class="part" id="empreender{sid}"><span>3</span><div><h2 class="ph">{t('Empreendedorismo e repertório','Entrepreneurship and background')}</h2><p>{t('Onde aprendi a ser responsável pelo resultado, do produto à entrega.','Where I learned to own the result, from product to delivery.')}</p></div></div>
<div class="cases">
{case('megeve','Chocolates Megève', t('fundadora · MEI<br>out/2020 – ago/2023','founder · sole proprietor<br>Oct 2020 – Aug 2023'), t('ponta a ponta','end to end'),
 t('Operar uma marca do produto à entrega, sozinha','Running a brand from product to delivery, on my own'),
 '<div class="eq">'
 + f'<div class="box"><span class="k">{t("Portfólio","Portfolio")}</span>{t("28 itens em 5 linhas","28 items in 5 lines")}</div><span class="op">+</span>'
 + f'<div class="box"><span class="k">{t("Fornecimento","Sourcing")}</span>{t("cacau do programa Cocoa Horizons, embalagem com menos plástico","cocoa from the Cocoa Horizons program, less plastic packaging")}</div><span class="op">+</span>'
 + f'<div class="box"><span class="k">{t("Venda e entrega","Sales and delivery")}</span>{t("site próprio, marketing digital, frete negociado","own website, digital marketing, negotiated shipping")}</div><span class="op">=</span>'
 + f'<div class="box res"><span class="k">{t("Resultado","Result")}</span>{t("quase 3 anos de operação; lucro doado a projeto social","almost 3 years of operation; profit donated to a social project")}</div>'
 + '</div>')}

{case('insead','Summer@INSEAD', t('Fontainebleau, França<br>jul – ago/2022','Fontainebleau, France<br>Jul – Aug 2022'), t('negócios','business'),
 t('COO numa simulação de aquisição de empresa','COO in a company acquisition simulation'),
 f'<div class="flow two"><div class="box"><span class="k">{t("Admissão","Admission")}</span>{t("processo seletivo com personal statement, carta de recomendação e entrevista em vídeo.","selection with a personal statement, a recommendation letter and a video interview.")}</div>'
 + f'<div class="box res"><span class="k">{t("O que eu fiz","What I did")}</span>{t("No time de 5, analisei os 3 documentos da transação e montei a matriz de negociação em 5 variáveis.","In a team of 5, I analyzed the 3 deal documents and built the negotiation matrix on 5 variables.")}</div></div>'
 + chips([], [t('estratégia','strategy'), t('decisão sob incerteza','decision under uncertainty'), t('excelência operacional','operational excellence'), t('negociação','negotiation')]))}
</div>

<!-- ===================== PARTE 4 ===================== -->
<div class="part" id="ferramentas{sid}"><span>4</span><div><h2 class="ph">{t('Ferramentas e formação','Tools and education')}</h2></div></div>
<div class="cols">
  <div>
    <span class="t">{t('Gestão','Management')}</span>
    {chips(['OKRs', 'KPIs', 'NPS'], [t('mapeamento de processos','process mapping'), t('matriz impacto-esforço','impact-effort matrix'), t('avaliação multicritério','multi-criteria assessment'), 'SIPOC', 'RACI', t('pesquisa de clima','climate survey')])}
    <span class="t sp">{t('Dados e tecnologia','Data and technology')}</span>
    {chips(['Claude Code', t('agentes de IA (skills, MCP)','AI agents (skills, MCP)'), 'Google Apps Script', 'Firebase'], ['Excel', 'Google Sheets', 'Power BI', 'QGIS', t('Python (básico)','Python (basic)'), 'JavaScript', 'Git · GitHub'])}
  </div>
  <div>
    <span class="t">{t('Formação','Education')}</span>
    <div class="edu">
      <span class="yy">2023–28</span><span><b>Poli-USP</b> · {t('Engenharia Ambiental, formatura em dez/2028','Environmental Engineering, graduating Dec 2028')}</span>
      <span class="yy">2022</span><span><b>Summer@INSEAD</b> · {t('negócios e liderança','business and leadership')}</span>
      <span class="yy">2024</span><span><b>Bureau Veritas</b> · {t('ESG aplicado à estratégia do negócio','ESG applied to business strategy')}</span>
    </div>
    <p class="langs">{t('Português nativo · inglês fluente · francês intermediário','Portuguese native · English fluent · French intermediate')}</p>
  </div>
</div>

<h2 id="proximos{sid}">{t('Próximos projetos','Next projects')} · {t('planejados, ainda sem resultado','planned, no results yet')}</h2>
<div class="next">
  <div class="box dashed"><span class="k">Make + Gemini</span>{t('Ata de reunião vira lista de tarefas com responsável e prazo.','Meeting minutes become a task list with owners and deadlines.')}</div>
  <div class="box dashed"><span class="k">Claude + Gemini</span>{t('O Claude divide o trabalho e confere; o Gemini lê o PDF longo.','Claude splits the work and checks; Gemini reads the long PDF.')}</div>
  <div class="box dashed"><span class="k">Apps Script</span>{t('A planilha do Areia Viva serve dados ao app por um endpoint JSON.','The Areia Viva spreadsheet serves data to the app through a JSON endpoint.')}</div>
</div>

<footer class="foot">
  <a href="{LI}">LinkedIn</a> · <a href="{GH}">GitHub</a> · <a href="mailto:gabrielavsdoria@gmail.com">gabrielavsdoria@gmail.com</a><br>
  {t('Atualizado em','Updated on')} {ATUALIZADO[L]}. {t('Os números vêm de documentos dos projetos e dos repositórios; dado fictício e estimativa estão marcados como tais.','Numbers come from project documents and the repositories; fictitious data and estimates are labeled as such.')}
</footer>
</section>
"""
