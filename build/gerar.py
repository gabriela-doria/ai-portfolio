# Gera o index.html do portfólio de IA (PT e EN) a partir de um único molde.
# Uso: python3 build/gerar.py  (na raiz do repositório)
import pathlib

ATUALIZADO = {"pt": "17/11/2026", "en": "17 Nov 2026"}

GH = "https://github.com/gabriela-doria"
LI = "https://www.linkedin.com/in/gabriela-vs-doria/"


def page(L):
    pt = L == "pt"

    def t(a, b):
        return a if pt else b

    sid = "" if pt else "-en"
    other = t('<a href="#en" lang="en">English</a>', '<a href="#pt" lang="pt-BR">Português</a>')

    # ---------- matriz vaga x prova ----------
    cols = [t("Areia Viva", "Areia Viva"), "Personal OS", "Campus", "Rota", "QGIS"]
    rows = [
        (t("Automação que economiza horas", "Automation that saves hours"), "●●○○○"),
        (t("Ferramenta no ar, usada por outras pessoas", "Live tool used by other people"), "●○○○○"),
        (t("Agente que resolve um problema", "Agent that solves a problem"), "○●○○○"),
        (t("Dashboard", "Dashboard"), "○○○●○"),
        (t("Demo feita do zero", "Demo built from scratch"), "○○●●○"),
        (t("Prompt engineering", "Prompt engineering"), "●●○○○"),
        (t("Orquestração de agentes (Claude)", "Agent orchestration (Claude)"), "○●○○○"),
        (t("Código com agente de IA (vibe coding)", "Coding with an AI agent (vibe coding)"), "●○●●○"),
        (t("API sem backend próprio", "API with no backend of its own"), "●○○○○"),
        (t("Análise de dados com IA", "Data analysis with AI"), "○○●○●"),
    ]
    planned = [
        t("Automação com n8n, Make ou Zapier", "Automation with n8n, Make or Zapier"),
        t("Orquestração entre modelos (Claude + Gemini)", "Orchestration across models (Claude + Gemini)"),
    ]
    mx = "".join(
        "<tr><td>%s</td>%s</tr>" % (
            r,
            "".join('<td>%s</td>' % ('<span class="d" title="%s"></span>' % t("prova publicada", "published proof") if c == "●" else '<span class="o"></span>') for c in marks),
        )
        for r, marks in rows
    )
    mx += "".join(
        '<tr class="pl"><td>%s</td><td colspan="5"><span class="chip dash">%s</span></td></tr>' % (p, t("planejado", "planned"))
        for p in planned
    )

    return f"""
<section id="{L}" lang="{t('pt-BR','en')}" class="page">
<div class="ruler" aria-hidden="true"></div>
<nav class="lang">{other}</nav>

<header class="mast">
  <div class="who">
    <img src="assets/foto-gabriela.jpg" width="104" height="104" alt="{t('Foto de Gabriela Dória','Photo of Gabriela Dória')}">
    <div>
      <p class="eyebrow">{t('Portfólio de IA','AI portfolio')} · <b>{t('dados, automação e IA aplicada','data, automation and applied AI')}</b> · {t('nov 2026','Nov 2026')}</p>
      <h1>Gabriela <em>Dória</em></h1>
      <p class="lede">{t('Engenharia Ambiental na Poli-USP. <b>Encontro o gargalo, construo a solução e meço se funcionou</b>, com dados e IA no trabalho de todo dia.','Environmental Engineering at Poli-USP, São Paulo. <b>I find the bottleneck, build the fix and measure whether it worked</b>, with data and AI in my everyday work.')}</p>
    </div>
  </div>
  <div class="contact">{t('Poli-USP · formatura dez/2028','Poli-USP · graduating Dec 2028')}<br>São Paulo · SP<br><a href="mailto:gabrielavsdoria@gmail.com">gabrielavsdoria@gmail.com</a><br><a href="{LI}">linkedin.com/in/gabriela-vs-doria</a><br><a href="{GH}">github.com/gabriela-doria</a></div>
</header>

<section class="figures" aria-label="{t('Números','Figures')}">
  <div class="fig"><b>25</b><small>{t('pessoas usam o app que programei com Claude Code','people use the app I built with Claude Code')}</small></div>
  <div class="fig"><b>16</b><small>{t('agentes de IA que desenhei e opero','AI agents I designed and run')}</small></div>
  <div class="fig"><b>64<span>%</span> → 100<span>%</span></b><small>{t('energia aproveitada na simulação (dados fictícios)','energy used in the simulation (fictitious data)')}</small></div>
  <div class="fig"><b>94,9<span>%</span></b><small>{t('atingimento médio dos KPIs da área que dirigi','average KPI attainment in the area I led')}</small></div>
</section>

<h2><b>{t('Como eu trabalho','How I work')}</b> · {t('o mesmo ciclo em todos os casos','the same loop in every case')}</h2>
<div class="cycle">
<svg viewBox="0 0 880 170" role="img" aria-label="{t('Ciclo: 1 Encontrar o gargalo, 2 Construir com IA, 3 Medir, e volta ao início','Loop: 1 Find the bottleneck, 2 Build with AI, 3 Measure, and back to the start')}">
  <defs><marker id="ah{sid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="arrh"/></marker></defs>
  <rect class="node" x="4" y="10" width="270" height="100" rx="5"/>
  <text class="num" x="20" y="42">1</text><text class="ttl" x="44" y="40">{t('Encontrar o gargalo','Find the bottleneck')}</text>
  <text class="sub" x="20" y="66">{t('mapeio o processo','I map the process')}</text><text class="sub" x="20" y="82">{t('e escolho a métrica','and pick the metric')}</text><text class="sub" x="20" y="98">{t('antes da ferramenta','before the tool')}</text>
  <rect class="node" x="304" y="10" width="270" height="100" rx="5"/>
  <text class="num" x="320" y="42">2</text><text class="ttl" x="344" y="40">{t('Construir com IA','Build with AI')}</text>
  <text class="sub" x="320" y="66">Claude Code · {t('agentes','agents')} · Apps Script</text><text class="sub" x="320" y="82">{t('a IA propõe, eu decido','AI proposes, I decide')}</text><text class="sub" x="320" y="98">{t('nada sai sem o meu ok','nothing goes out without my ok')}</text>
  <rect class="node hi" x="604" y="10" width="272" height="100" rx="5"/>
  <text class="num" x="620" y="42">3</text><text class="ttl" x="644" y="40">{t('Medir','Measure')}</text>
  <text class="sub" x="620" y="66">{t('testes automáticos e contagens','automated tests and counts')}</text><text class="sub" x="620" y="82">{t('estimativa dita como estimativa','estimates labeled as estimates')}</text><text class="sub" x="620" y="98">{t('dado fictício marcado','fictitious data flagged')}</text>
  <path class="arr" d="M276 60 H300" marker-end="url(#ah{sid})"/>
  <path class="arr" d="M576 60 H600" marker-end="url(#ah{sid})"/>
  <path class="arr" d="M740 112 V140 H140 V114" marker-end="url(#ah{sid})"/>
  <text class="loop" x="440" y="158" text-anchor="middle">{t('→ volto ao passo 1 com o que a medição mostrou','→ back to step 1 with what the measurement showed')}</text>
</svg>
<ol class="cyclist">
  <li><b>1 · {t('Encontrar o gargalo','Find the bottleneck')}</b>{t('mapeio o processo e escolho a métrica antes da ferramenta','I map the process and pick the metric before the tool')}</li>
  <li><b>2 · {t('Construir com IA','Build with AI')}</b>Claude Code · {t('agentes','agents')} · Apps Script. {t('A IA propõe, eu decido.','AI proposes, I decide.')}</li>
  <li class="hi"><b>3 · {t('Medir','Measure')}</b>{t('testes automáticos e contagens; estimativa e dado fictício marcados','automated tests and counts; estimates and fictitious data flagged')}</li>
  <li class="loop">{t('↺ volto ao passo 1 com o que a medição mostrou','↺ back to step 1 with what the measurement showed')}</li>
</ol>
</div>

<h2>{t('Trajetória','Path')} · 2020 – 2026</h2>
<div class="tl">
<svg viewBox="0 0 880 96" role="img" aria-label="{t('Linha do tempo de 2020 a 2026','Timeline from 2020 to 2026')}">
  <line class="axis" x1="20" y1="32" x2="860" y2="32"/>
  <circle cx="45" cy="32" r="5"/><text class="y" x="45" y="18" text-anchor="middle">2020</text><text x="45" y="52" text-anchor="middle">Megève</text><text x="45" y="65" text-anchor="middle">{t('fundadora','founder')}</text>
  <circle cx="165" cy="32" r="5"/><text class="y" x="165" y="18" text-anchor="middle">2022</text><text x="165" y="52" text-anchor="middle">Summer@INSEAD</text>
  <circle cx="285" cy="32" r="5"/><text class="y" x="285" y="18" text-anchor="middle">2023</text><text x="285" y="52" text-anchor="middle">Poli-USP</text><text x="285" y="65" text-anchor="middle">Poli Social</text>
  <circle cx="405" cy="32" r="5"/><text class="y" x="405" y="18" text-anchor="middle">{t('nov/2024','Nov 2024')}</text><text x="405" y="52" text-anchor="middle">{t('Diretora','Director')}</text><text x="405" y="65" text-anchor="middle">{t('de Projetos','of Projects')}</text>
  <circle cx="525" cy="32" r="7" class="hi"/><text class="y hi" x="525" y="18" text-anchor="middle">{t('set/2026','Sep 2026')}</text><text class="hi" x="525" y="52" text-anchor="middle">{t('Drive Areia Viva','Areia Viva Drive')}</text><text class="hi" x="525" y="65" text-anchor="middle">Personal OS</text>
  <circle cx="645" cy="32" r="7" class="hi"/><text class="y hi" x="645" y="18" text-anchor="middle">{t('out/2026','Oct 2026')}</text><text class="hi" x="645" y="52" text-anchor="middle">Rota do Excedente</text>
  <circle cx="765" cy="32" r="7" class="hi"/><text class="y hi" x="765" y="18" text-anchor="middle">{t('nov/2026','Nov 2026')}</text><text class="hi" x="765" y="52" text-anchor="middle">{t('App Areia Viva','Areia Viva app')}</text><text class="hi" x="765" y="65" text-anchor="middle">Campus de energia</text>
</svg>
<ul class="tlist">
  <li><b>2020</b>Chocolates Megève · {t('fundadora','founder')}</li>
  <li><b>2022</b>Summer@INSEAD</li>
  <li><b>2023</b>Poli-USP · Poli Social</li>
  <li><b>{t('nov/2024','Nov 2024')}</b>{t('Diretora de Projetos','Director of Projects')}</li>
  <li class="hi"><b>{t('set/2026','Sep 2026')}</b>{t('Drive do Areia Viva · Personal OS','Areia Viva Drive · Personal OS')}</li>
  <li class="hi"><b>{t('out/2026','Oct 2026')}</b>Rota do Excedente</li>
  <li class="hi"><b>{t('nov/2026','Nov 2026')}</b>{t('App do Areia Viva · Campus de energia','Areia Viva app · Campus de energia')}</li>
</ul>
</div>

<h2 id="vaga{sid}"><b>{t('O que uma vaga de IA pede','What an AI role asks for')}</b> · {t('e onde está a prova','and where the proof is')}</h2>
<table class="mx">
<thead><tr><th></th>{''.join(f'<th>{c}</th>' for c in cols)}</tr></thead>
<tbody>{mx}</tbody>
<tfoot><tr><td colspan="6"><span class="d"></span> {t('prova publicada no caso','proof published in the case')} &nbsp; <span class="o"></span> {t('não se aplica','not applicable')} &nbsp; <span class="chip dash">{t('planejado','planned')}</span> {t('ainda sem prova','no proof yet')}</td></tr></tfoot>
</table>

<h2 id="casos{sid}"><b>{t('Cinco casos','Five cases')}</b> · {t('problema → o que eu fiz → resultado','problem → what I did → result')}</h2>
<div class="cases">

<article class="case" id="areia-viva{sid}">
  <div class="meta"><b>Areia Viva · 2026</b>{t('extensão USP, voluntária','USP extension project, volunteer')}<br>{t('Drive set/2026 · app nov/2026','Drive Sep 2026 · app Nov 2026')}<span class="tag">{t('em uso','in use')}</span></div>
  <div>
    <h3>{t('Um app de horas que 25 pessoas usam, programado com Claude Code','An hours app 25 people use, built with Claude Code')}</h3>
    <div class="flow">
      <div class="box"><span class="k">{t('Problema','Problem')}</span>{t('As horas eram registradas no computador, muitas vezes meses depois. O Drive não tinha regra de nome, pasta nem acesso.','Hours were logged on a computer, often months later. The Drive had no rule for names, folders or access.')}</div>
      <div class="box"><span class="k">{t('O que eu fiz','What I did')}</span>{t('Reestruturei o Drive com matriz de decisão e scripts que simulam antes de rodar. Construí o app: celular, login Google, acesso por papel.','I restructured the Drive with a decision matrix and scripts that simulate before running. I built the app: phone, Google sign-in, role-based access.')}</div>
      <div class="box res"><span class="k">{t('Resultado','Result')}</span>{t('App em uso por 25 pessoas desde 13/11/2026. As horas passaram a ser registradas no mesmo dia.','App used by 25 people since 13 Nov 2026. Hours are now logged the same day.')}</div>
    </div>
    <div class="eq">
      <div class="box"><span class="k">{t('set/2026','Sep 2026')}</span>{t('Drive reestruturado','Drive restructured')}</div><span class="op">→</span>
      <div class="box"><span class="k">{t('1ª versão','1st version')}</span>{t('Mapa do Drive em Apps Script','Drive Map on Apps Script')}</div><span class="op">→</span>
      <div class="box res"><span class="k">{t('nov/2026','Nov 2026')}</span>{t('App em Firebase, 32 testes das regras de acesso','App on Firebase, 32 access-rule tests')}</div>
    </div>
    <div class="nums">
      <div><b>25</b><small>{t('pessoas usam o app','people use the app')}</small></div>
      <div><b>32</b><small>{t('testes automáticos','automated tests')}</small></div>
      <div><b>124</b><small>{t('arquivos renomeados','files renamed')}</small></div>
      <div><b>33</b><small>{t('contas com acesso por papel','role-based accounts')}</small></div>
      <div><b>62</b><small>{t('pastas na nova estrutura','folders in the new structure')}</small></div>
    </div>
    <figure class="shot"><img src="assets/app-areia-viva-demo.jpg" width="700" height="525" loading="lazy" alt="{t('Tela do painel do app do Areia Viva, com horas e tarefas, no modo de demonstração','Screen of the Areia Viva app dashboard, with hours and tasks, in demo mode')}"><figcaption><b>{t('App do Areia Viva','Areia Viva app')}</b> · {t('tela no modo de demonstração, com dados fictícios','screen in demo mode, with fictitious data')}</figcaption></figure>
    <div class="chips"><span class="chip on">Claude Code</span><span class="chip on">Firebase</span><span class="chip">Google Apps Script</span><span class="chip">{t('API do Drive','Drive API')}</span><span class="chip">{t('4 prompts reutilizáveis','4 reusable prompts')}</span></div>
    <p class="how">{t('Como medi: as contagens saem dos registros dos scripts. A mudança no dia a dia ainda não tem número; o plano de medição está no repositório.','How I measured: the counts come from the scripts\' logs. The day-to-day change has no number yet; the measurement plan is in the repository.')}</p>
    <div class="link"><a href="{GH}/student-project-ops-ai">{t('repositório','repository')} · student-project-ops-ai</a></div>
  </div>
</article>

<article class="case" id="personal-os{sid}">
  <div class="meta"><b>Personal OS · 2026</b>{t('projeto pessoal','personal project')}<br>{t('desde set/2026','since Sep 2026')}<span class="tag">{t('agentes','agents')}</span></div>
  <div>
    <h3>{t('16 agentes de IA que organizam faculdade, extensão e busca de estágio','16 AI agents that run coursework, extension work and the internship search')}</h3>
    <div class="flow">
      <div class="box"><span class="k">{t('Problema','Problem')}</span>{t('Informação espalhada em vários sistemas. O gargalo era coordenar: o que vence primeiro e onde está cada arquivo.','Information spread across systems. The bottleneck was coordination: what is due first and where each file is.')}</div>
      <div class="box"><span class="k">{t('O que eu fiz','What I did')}</span>{t('Escrevi 16 skills do Claude que leem as fontes e propõem ações, mais um radar que dá nota de 0 a 100 a cada vaga.','I wrote 16 Claude skills that read the sources and propose actions, plus a radar that scores each opening from 0 to 100.')}</div>
      <div class="box res"><span class="k">{t('Resultado','Result')}</span>{t('273 e-mails arquivados e 163 arquivos renomeados na primeira rodada.','273 emails archived and 163 files renamed in the first run.')}</div>
    </div>
    <div class="eq">
      <div class="box"><span class="k">{t('Fontes','Sources')}</span>Gmail · {t('Agenda','Calendar')} · Drive · Moodle</div><span class="op">→</span>
      <div class="box"><span class="k">{t('Agentes','Agents')}</span>{t('16 skills propõem','16 skills propose')}</div><span class="op">→</span>
      <div class="box"><span class="k">{t('Eu','Me')}</span>{t('aprovo ou corrijo','approve or correct')}</div><span class="op">→</span>
      <div class="box res"><span class="k">{t('Ação','Action')}</span>{t('arquiva, renomeia, agenda','archives, renames, schedules')}</div>
    </div>
    <div class="nums">
      <div><b>273</b><small>{t('e-mails arquivados','emails archived')}</small></div>
      <div><b>163</b><small>{t('arquivos renomeados','files renamed')}</small></div>
      <div><b>~80 min</b><small>{t('por semana na coleta de aulas (estimativa)','a week on course materials (estimate)')}</small></div>
      <div><b>275</b><small>{t('peças no Mapa do Sistema','parts in the System Map')}</small></div>
    </div>
    <div class="chips"><span class="chip on">{t('Claude (skills, MCP, tarefas agendadas)','Claude (skills, MCP, scheduled tasks)')}</span><span class="chip">Google Apps Script</span><span class="chip">Python</span></div>
    <p class="how">{t('Como medi: contagem nos registros de execução (29/10/2026). O tempo poupado é estimativa minha, sem linha de base.','How I measured: counts from the run logs (29 Oct 2026). Time saved is my own estimate, with no baseline.')}</p>
    <div class="link"><a href="{GH}/personal-os-claude">{t('repositório','repository')} · personal-os-claude</a> · <a href="{GH}/personal-os-claude/tree/main/skills/radar-estagios">{t('radar de estágios','internship radar')}</a></div>
  </div>
</article>

<article class="case" id="campus{sid}">
  <div class="meta"><b>Campus de energia</b>{t('exercício pessoal','personal exercise')}<br>{t('nov/2026','Nov 2026')}<span class="tag">{t('dados fictícios','fictitious data')}</span></div>
  <div>
    <h3>{t('Qual cliente aproveita a energia que a rede não recebe','Which customer uses the energy the grid can\'t take')}</h3>
    <div class="flow">
      <div class="box"><span class="k">{t('Problema','Problem')}</span>{t('Um parque eólico e solar gera mais do que cabe na linha de conexão.','A wind and solar park produces more than its grid connection can carry.')}</div>
      <div class="box"><span class="k">{t('O que eu fiz','What I did')}</span>{t('Simulação hora a hora com programação linear, preço-sombra e matriz de decisão para 3 clientes. Problema e critérios meus; código com o Claude.','Hour-by-hour simulation with linear programming, shadow prices and a decision matrix for 3 customers. Problem and criteria mine; code with Claude.')}</div>
      <div class="box res"><span class="k">{t('Resultado','Result')}</span>{t('Com um data center ao lado, o parque aproveita toda a energia e a receita da semana sobe 96%.','With a data center next door, the park uses all its energy and weekly revenue rises 96%.')}</div>
    </div>
    <div class="bars">
      <div class="bar"><span>{t('Sem cliente ao lado','No customer next door')}</span><span class="trk"><span class="fill amb" style="width:64.1%"></span></span><span class="v">64,1%</span></div>
      <div class="bar"><span>{t('Com data center','With a data center')}</span><span class="trk"><span class="fill" style="width:100%"></span></span><span class="v">100%</span></div>
    </div>
    <div class="chips"><span class="chip on">{t('Claude (agente de código)','Claude (coding agent)')}</span><span class="chip">Python</span><span class="chip">SciPy</span><span class="chip">{t('programação linear','linear programming')}</span></div>
    <p class="how">{t('Como medi: 6 testes automáticos, entre eles a conta à mão contra o modelo e o preço-sombra com 1 MW a mais e a menos.','How I measured: 6 automated tests, including a hand calculation against the model and the shadow price at ±1 MW.')}</p>
    <div class="link"><a href="{GH}/campus-de-energia">{t('repositório','repository')} · campus-de-energia</a></div>
  </div>
</article>

<article class="case" id="rota{sid}">
  <div class="meta"><b>Rota do Excedente</b>{t('case de desafio de IA','AI challenge case')}<br>{t('out/2026','Oct 2026')}<span class="tag">{t('dados fictícios','fictitious data')}</span></div>
  <div>
    <h3>{t('Comida que sobra em restaurantes até cozinhas solidárias','Surplus restaurant food to community kitchens')}</h3>
    <div class="flow">
      <div class="box"><span class="k">{t('Problema','Problem')}</span>{t('Restaurantes têm comida sobrando e as cozinhas não têm como buscar. Hipótese: falta transporte.','Restaurants have surplus food and kitchens can\'t collect it. Hypothesis: transport is missing.')}</div>
      <div class="box"><span class="k">{t('O que eu fiz','What I did')}</span>{t('Algoritmo que agrupa restaurantes em rotas, calcula o custo por kg e descarta rota que não se paga. Página com premissas editáveis.','An algorithm that groups restaurants into routes, computes cost per kg and drops routes that don\'t pay off. A page with editable assumptions.')}</div>
      <div class="box res"><span class="k">{t('Resultado','Result')}</span>{t('No exemplo, 128 kg resgatados a R$ 1,64 por kg, contra R$ 12,00 para comprar.','In the example, 128 kg rescued at R$ 1.64 per kg, versus R$ 12.00 to buy.')}</div>
    </div>
    <div class="funnel">
      <div class="fun"><span>{t('Restaurantes','Restaurants')}</span><span class="seg" style="width:100%">16</span></div>
      <div class="fun"><span>{t('Rotas','Routes')}</span><span class="seg l2" style="width:37.5%">6</span></div>
      <div class="fun"><span>{t('Resgatados','Rescued')}</span><span class="seg l3" style="width:60%">128 kg</span></div>
    </div>
    <div class="bars">
      <div class="bar"><span>{t('Custo por kg, pela rota','Cost per kg, by route')}</span><span class="trk"><span class="fill" style="width:13.7%"></span></span><span class="v">R$ 1,64</span></div>
      <div class="bar"><span>{t('Custo por kg, comprando','Cost per kg, buying')}</span><span class="trk"><span class="fill amb" style="width:100%"></span></span><span class="v">R$ 12,00</span></div>
    </div>
    <div class="chips"><span class="chip on">{t('Claude (agente de código)','Claude (coding agent)')}</span><span class="chip">JavaScript</span><span class="chip">Leaflet · OpenStreetMap</span></div>
    <p class="how">{t('Como medi: o algoritmo descarta a rota quando o custo por kg passa do custo de comprar. Os valores em reais são hipóteses; proponho um piloto de 4 semanas para medir em campo.','How I measured: the algorithm drops a route when its cost per kg exceeds the cost of buying. The amounts are hypotheses; I propose a 4-week field pilot.')}</p>
    <div class="link"><a href="https://gabriela-doria.github.io/rota-do-excedente/">{t('demo ao vivo','live demo')}</a> · <a href="{GH}/rota-do-excedente">{t('repositório','repository')}</a></div>
  </div>
</article>

<article class="case" id="qgis{sid}">
  <div class="meta"><b>{t('Análise espacial','Spatial analysis')}</b>Geoprocessamento, Poli-USP<br>{t('1º sem/2026 · grupo de 3','1st sem 2026 · group of 3')}<span class="tag">{t('dados públicos','public data')}</span></div>
  <div>
    <h3>{t('Metrô, renda e área construída em São Paulo, no QGIS','Metro, income and built area in São Paulo, in QGIS')}</h3>
    <div class="flow">
      <div class="box"><span class="k">{t('Problema','Problem')}</span>{t('A renda dos distritos acompanha o acesso ao metrô? Onde a cidade mais cresceu de 2010 a 2022?','Does district income follow metro access? Where did the city grow most from 2010 to 2022?')}</div>
      <div class="box"><span class="k">{t('O que eu fiz','What I did')}</span>{t('Cruzei Censo 2022, Pesquisa OD 2023 e IPTU com raios de 800 m nas 94 estações. Claude como guia de método e código.','I combined the 2022 census, 2023 travel survey and property tax data with 800 m buffers around 94 stations. Claude as a method and code guide.')}</div>
      <div class="box res"><span class="k">{t('Resultado','Result')}</span>{t('Em 46 dos 96 distritos, nenhum morador está a até 800 m de uma estação.','In 46 of 96 districts, no resident lives within 800 m of a station.')}</div>
    </div>
    <div class="bars">
      <div class="bar"><span>{t('Distritos sem metrô a 800 m','Districts with no metro within 800 m')}</span><span class="trk"><span class="fill amb" style="width:47.9%"></span></span><span class="v">46 / 96</span></div>
      <div class="bar"><span>{t('Área construída, Lapa','Built area, Lapa')}</span><span class="trk"><span class="fill" style="width:100%"></span></span><span class="v">+25,5%</span></div>
      <div class="bar"><span>{t('Área construída, Capela do Socorro','Built area, Capela do Socorro')}</span><span class="trk"><span class="fill" style="width:66.7%"></span></span><span class="v">+17,0%</span></div>
    </div>
    <div class="chips"><span class="chip">QGIS</span><span class="chip">Python · geopandas</span><span class="chip">Google Earth Engine</span><span class="chip on">{t('Claude (guia de método)','Claude (method guide)')}</span></div>
    <p class="how">{t('Trabalho em grupo; os mapas citados são os que eu fiz. Limites escritos no repositório: população uniforme no setor e distância em linha reta.','Group work; the maps cited are the ones I made. Limits written in the repository: uniform population within each tract and straight-line distance.')}</p>
    <div class="link"><a href="{GH}/analise-espacial-qgis-sp">{t('repositório com os mapas','repository with the maps')}</a></div>
  </div>
</article>
</div>

<h2 id="gestao{sid}"><b>{t('Além da IA','Beyond AI')}</b> · {t('indicadores, inovação e pessoas na Poli Social, 2023 – 2025','metrics, innovation and people at Poli Social, 2023 – 2025')}</h2>
<div class="beyond">
  <div class="bars">
    <div class="bar"><span>{t('KPIs da área que dirigi, 2025','KPIs of the area I led, 2025')}</span><span class="trk"><span class="fill" style="width:94.9%"></span></span><span class="v">94,9%</span></div>
    <div class="bar"><span>{t('Meta de relacionamento com as ONGs','Relationship target with NGOs')}</span><span class="trk"><span class="fill" style="width:100%"></span><span class="goal" style="left:46.7%"></span></span><span class="v">214,3%</span></div>
    <div class="bar"><span>{t('Grupo de Inovação: modelo aprovado','Innovation Group: model approved')}</span><span class="trk"><span class="fill amb" style="width:84.2%"></span></span><span class="v">84,2%</span></div>
    <div class="bar"><span>{t('Grupo de Inovação: proposta final','Innovation Group: final proposal')}</span><span class="trk"><span class="fill amb" style="width:83.3%"></span></span><span class="v">83,3%</span></div>
    <div class="bar"><span>{t('NPS da ONG no projeto de 10 meses','NGO NPS on the 10-month project')}</span><span class="trk"><span class="fill" style="width:100%"></span></span><span class="v">100</span></div>
  </div>
  <div class="nums three">
    <div><b>12</b><small>{t('pessoas lideradas diretamente','people led directly')}</small></div>
    <div><b>3</b><small>{t('cargos: consultora, gerente, diretora','roles: consultant, manager, director')}</small></div>
    <div><b>40</b><small>{t('membros na assembleia que aprovou o Grupo de Inovação','members at the assembly that approved the Innovation Group')}</small></div>
  </div>
  <p class="how">{t('Fonte: relatório de atividades 2025 da Poli Social e pesquisas de satisfação dos projetos.','Source: Poli Social 2025 activity report and project satisfaction surveys.')}</p>
</div>

<h2 id="proximos{sid}">{t('Próximos projetos','Next projects')} · {t('planejados, ainda sem resultado','planned, no results yet')}</h2>
<div class="next">
  <div class="box dashed"><span class="k">Make + Gemini</span>{t('Ata de reunião vira lista de tarefas com responsável e prazo.','Meeting minutes become a task list with owners and deadlines.')}</div>
  <div class="box dashed"><span class="k">Claude + Gemini</span>{t('O Claude divide o trabalho e confere; o Gemini lê o PDF longo.','Claude splits the work and checks; Gemini reads the long PDF.')}</div>
  <div class="box dashed"><span class="k">Apps Script</span>{t('A planilha do Areia Viva serve dados ao app por um endpoint JSON.','The Areia Viva spreadsheet serves data to the app through a JSON endpoint.')}</div>
</div>

<footer class="foot">
  <a href="{LI}">LinkedIn</a> · <a href="{GH}">GitHub</a> · <a href="mailto:gabrielavsdoria@gmail.com">gabrielavsdoria@gmail.com</a><br>
  {t('Atualizado em','Updated on')} {ATUALIZADO[L]}. {t('Os números têm fonte nos repositórios; dado fictício e estimativa estão marcados como tais.','Numbers are sourced in the repositories; fictitious data and estimates are labeled as such.')}
</footer>
</section>
"""


CSS = """
:root{
  --paper:#F1F3EE; --surface:#FBFCFA; --surface-2:#E7EBE3;
  --ink:#141D1A; --ink-2:#3C4A45; --ink-3:#5E6D67;
  --rule:#C9D2C9; --rule-strong:#9FAEA6;
  --petrol:#0E5259; --petrol-soft:#D6E5E5;
  --amber:#9A5C0E; --amber-soft:#F0E2CB;
  --flag:#8A3324;
  --f-display:"Archivo","Helvetica Neue",Arial,sans-serif;
  --f-body:"Source Serif 4",Georgia,"Times New Roman",serif;
  --f-mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root{
    --paper:#0C1210; --surface:#131B18; --surface-2:#1B2521;
    --ink:#E7EEE9; --ink-2:#B4C2BB; --ink-3:#8FA198;
    --rule:#2B3733; --rule-strong:#44544E;
    --petrol:#61BFC2; --petrol-soft:#143135;
    --amber:#D9A050; --amber-soft:#332615;
    --flag:#E08975;
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--f-body);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:var(--petrol);text-underline-offset:3px;text-decoration-thickness:1px}
a:focus-visible{outline:2px solid var(--amber);outline-offset:3px;border-radius:2px}
.page{max-width:900px;margin:0 auto;padding:22px 22px 56px}
#en{border-top:2px dashed var(--rule-strong)}
.ruler{height:14px;background:repeating-linear-gradient(90deg,var(--rule-strong) 0 1px,transparent 1px 10px);border-bottom:1px solid var(--rule-strong);opacity:.65;margin-bottom:10px}
.lang{text-align:right;font-family:var(--f-mono);font-size:.72rem;margin-bottom:6px}
.mast{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px 32px;align-items:end;padding-bottom:18px;border-bottom:2px solid var(--ink)}
@media (max-width:680px){.mast{grid-template-columns:minmax(0,1fr)}}
.who{display:flex;gap:18px;align-items:center}
.who img{width:104px;height:104px;border-radius:50%;object-fit:cover;border:3px solid var(--surface);box-shadow:0 0 0 1.5px var(--petrol);flex:none}
@media (max-width:680px){.who img{width:76px;height:76px}}
.eyebrow{font-family:var(--f-mono);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin:0 0 10px}
.eyebrow b{color:var(--petrol);font-weight:600}
h1{font-family:var(--f-display);font-weight:800;font-size:clamp(2.1rem,6vw,3.2rem);line-height:.95;letter-spacing:-.02em;margin:0 0 10px}
h1 em{font-style:normal;color:var(--petrol)}
.lede{font-size:clamp(1.02rem,2.2vw,1.14rem);line-height:1.45;color:var(--ink-2);margin:0;max-width:56ch}
.lede b{color:var(--ink);font-weight:600}
.contact{font-family:var(--f-mono);font-size:.74rem;color:var(--ink-2);line-height:1.9;text-align:right;white-space:nowrap}
@media (max-width:680px){.contact{text-align:left;white-space:normal}}
.contact a{color:inherit;text-decoration:none}
.figures{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin:0 0 26px}
@media (max-width:680px){.figures{grid-template-columns:repeat(2,minmax(0,1fr))}}
.fig{padding:14px 14px 14px 0;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.fig:nth-child(4n){border-right:0}
@media (max-width:680px){.fig:nth-child(2n){border-right:0}}
.fig b{display:block;font-family:var(--f-display);font-weight:750;font-size:clamp(1.6rem,3.8vw,2.2rem);line-height:1;letter-spacing:-.02em;font-variant-numeric:tabular-nums;color:var(--petrol)}
.fig b span{font-size:.55em;color:var(--ink-3);font-weight:500}
.fig small{display:block;font-family:var(--f-mono);font-size:.66rem;line-height:1.4;color:var(--ink-3);margin-top:6px;text-transform:uppercase;letter-spacing:.04em}
h2{font-family:var(--f-mono);font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3);font-weight:500;margin:0 0 12px}
h2 b{color:var(--ink);font-weight:600}
.cycle{margin:0 0 26px}
.cycle svg,.tl svg{width:100%;height:auto;display:block}
.cycle .node{fill:var(--surface);stroke:var(--rule-strong);stroke-width:1.2}
.cycle .node.hi{fill:var(--petrol-soft);stroke:var(--petrol)}
.cycle .num{font-family:var(--f-display);font-weight:700;font-size:22px;fill:var(--petrol)}
.cycle .ttl{font-family:var(--f-display);font-weight:700;font-size:15px;fill:var(--ink)}
.cycle .sub{font-family:var(--f-mono);font-size:11px;fill:var(--ink-3)}
.cycle .arr{stroke:var(--amber);stroke-width:1.8;fill:none}
.cycle .arrh{fill:var(--amber)}
.cycle .loop{font-family:var(--f-mono);font-size:11px;fill:var(--amber)}
.cyclist,.tlist{display:none;list-style:none;margin:0;padding:0}
@media (max-width:680px){
  .cycle svg,.tl svg{display:none}
  .cyclist{display:grid;gap:8px}
  .cyclist li{background:var(--surface);border:1px solid var(--rule-strong);border-radius:4px;padding:8px 10px;font-family:var(--f-mono);font-size:.72rem;color:var(--ink-3)}
  .cyclist li b{display:block;font-family:var(--f-display);font-size:.98rem;color:var(--ink);margin-bottom:2px}
  .cyclist li.hi{background:var(--petrol-soft);border-color:var(--petrol)}
  .cyclist li.loop{background:none;border:0;color:var(--amber);padding:0 2px}
  .tlist{display:grid;gap:0;border-left:2px solid var(--rule-strong);margin-left:6px}
  .tlist li{position:relative;padding:4px 0 8px 16px;font-family:var(--f-mono);font-size:.72rem;color:var(--ink-3)}
  .tlist li::before{content:"";position:absolute;left:-7px;top:8px;width:10px;height:10px;border-radius:50%;background:var(--surface);border:1.5px solid var(--rule-strong)}
  .tlist li.hi::before{background:var(--petrol);border-color:var(--petrol)}
  .tlist li b{display:block;color:var(--ink)}
  .tlist li.hi{color:var(--petrol)}
}
.tl{margin:0 0 26px;border-bottom:1px solid var(--rule);padding-bottom:10px}
.tl svg{overflow:visible}
.tl text{font-family:var(--f-mono);font-size:10.5px;fill:var(--ink-3)}
.tl text.y{font-size:11px;fill:var(--ink);font-weight:600}
.tl text.hi{fill:var(--petrol);font-weight:600}
.tl line.axis{stroke:var(--rule-strong);stroke-width:1.5}
.tl circle{fill:var(--surface);stroke:var(--rule-strong);stroke-width:1.5}
.tl circle.hi{fill:var(--petrol);stroke:var(--petrol)}
table.mx{width:100%;border-collapse:collapse;margin:0 0 28px;font-size:.88rem}
table.mx th,table.mx td{padding:6px 8px;border-bottom:1px solid var(--rule);text-align:center}
table.mx th{font-family:var(--f-mono);font-size:.62rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);font-weight:500;vertical-align:bottom}
table.mx td:first-child,table.mx th:first-child{text-align:left}
table.mx td:first-child{color:var(--ink-2)}
table.mx tr.pl td{color:var(--ink-3)}
table.mx tr.pl td:last-child{text-align:left}
.d{display:inline-block;width:11px;height:11px;border-radius:50%;background:var(--petrol);vertical-align:middle}
.o{display:inline-block;width:11px;height:11px;border-radius:50%;border:1.5px solid var(--rule-strong);vertical-align:middle}
table.mx tfoot td{font-family:var(--f-mono);font-size:.64rem;color:var(--ink-3);border:0;padding-top:8px;text-align:left}
@media (max-width:680px){table.mx{font-size:.78rem}table.mx th{font-size:.54rem;letter-spacing:0}table.mx th,table.mx td{padding:5px 3px}}
.cases{display:grid;margin:0 0 26px}
.case{display:grid;grid-template-columns:150px minmax(0,1fr);gap:0 22px;padding:18px 0 20px;border-top:1px solid var(--rule)}
@media (max-width:680px){.case{grid-template-columns:minmax(0,1fr);gap:8px}}
.case .meta{font-family:var(--f-mono);font-size:.7rem;line-height:1.6;color:var(--ink-3)}
.case .meta b{display:block;color:var(--ink);font-weight:600;font-size:.76rem;margin-bottom:2px}
.case .meta .tag{display:inline-block;margin-top:8px;border:1px solid var(--amber);color:var(--amber);border-radius:999px;padding:1px 8px;font-size:.62rem;letter-spacing:.06em;text-transform:uppercase}
.case h3{font-family:var(--f-display);font-weight:700;font-size:1.1rem;line-height:1.25;letter-spacing:-.01em;margin:0 0 8px}
.flow{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:6px 0 12px}
@media (max-width:680px){.flow{grid-template-columns:1fr;gap:16px}}
.box{background:var(--surface);border:1px solid var(--rule);border-radius:4px;padding:8px 10px;font-size:.86rem;line-height:1.38;position:relative}
.box .k{font-family:var(--f-mono);font-size:.6rem;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:3px}
.box.res{border-color:var(--petrol);background:var(--petrol-soft)}
.box.res .k{color:var(--petrol)}
.flow .box:not(:last-child)::after{content:"→";position:absolute;right:-12px;top:50%;transform:translateY(-50%);color:var(--amber);font-weight:700;font-size:.9rem;z-index:1}
@media (max-width:680px){.flow .box:not(:last-child)::after{content:"↓";right:auto;left:50%;top:auto;bottom:-15px;transform:translateX(-50%)}}
.eq{display:flex;flex-wrap:wrap;align-items:stretch;gap:6px;margin:0 0 12px}
.eq .box{flex:1 1 120px;font-size:.82rem}
.eq .op{align-self:center;font-family:var(--f-display);font-weight:700;color:var(--amber);font-size:1.15rem}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:8px;margin:0 0 12px}
.nums div{border-left:3px solid var(--petrol);padding:2px 0 2px 9px}
.nums b{display:block;font-family:var(--f-display);font-weight:750;font-size:1.45rem;line-height:1.05;color:var(--petrol);font-variant-numeric:tabular-nums}
.nums small{display:block;font-family:var(--f-mono);font-size:.62rem;line-height:1.35;color:var(--ink-3);margin-top:3px}
.bars{display:grid;gap:6px;margin:4px 0 12px}
.bar{display:grid;grid-template-columns:210px 1fr 78px;gap:10px;align-items:center;font-family:var(--f-mono);font-size:.66rem;color:var(--ink-3)}
@media (max-width:680px){.bar{grid-template-columns:120px 1fr 64px}}
.bar .trk{display:block;height:10px;background:var(--surface-2);border-radius:2px;position:relative}
.bar .fill{display:block;height:100%;background:var(--petrol);border-radius:2px}
.bar .fill.amb{background:var(--amber)}
.bar .goal{position:absolute;top:-4px;width:2px;height:18px;background:var(--flag)}
.bar .goal::after{content:"meta";position:absolute;top:-12px;left:-10px;font-size:.56rem;color:var(--flag)}
#en .bar .goal::after{content:"target";left:-14px}
.bar .v{text-align:right;color:var(--ink);font-weight:600}
.funnel{display:grid;gap:4px;margin:4px 0 10px}
.fun{display:grid;grid-template-columns:210px 1fr;gap:10px;align-items:center;font-family:var(--f-mono);font-size:.66rem;color:var(--ink-3)}
@media (max-width:680px){.fun{grid-template-columns:120px 1fr}}
.fun .seg{height:20px;background:var(--petrol);border-radius:2px;color:#fff;font-weight:600;font-size:.7rem;display:flex;align-items:center;padding-left:8px;white-space:nowrap}
@media (prefers-color-scheme: dark){.fun .seg{color:#0C1210}}
.fun .seg.l2{opacity:.75}.fun .seg.l3{background:var(--amber)}
.chips{display:flex;flex-wrap:wrap;gap:5px;margin:6px 0 0}
.chip{font-family:var(--f-mono);font-size:.64rem;border:1px solid var(--rule-strong);border-radius:999px;padding:2px 8px;color:var(--ink-2);background:var(--surface)}
.chip.on{border-color:var(--petrol);color:var(--petrol)}
.chip.dash{border-style:dashed;color:var(--ink-3)}
.how{font-family:var(--f-mono);font-size:.64rem;line-height:1.5;color:var(--ink-3);margin:8px 0 0}
.link{font-family:var(--f-mono);font-size:.7rem;margin-top:8px}
.shot{margin:4px 0 10px;border:1px solid var(--rule);border-radius:4px;overflow:hidden;background:var(--surface);max-width:520px}
.shot img{display:block;width:100%;height:auto}
.shot figcaption{font-family:var(--f-mono);font-size:.64rem;line-height:1.45;color:var(--ink-3);padding:7px 9px}
.shot figcaption b{color:var(--ink);font-weight:600}
.beyond{margin:0 0 28px}
.nums.three{grid-template-columns:repeat(3,minmax(0,1fr))}
@media (max-width:680px){.nums.three{grid-template-columns:1fr}}
.next{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:0 0 26px}
@media (max-width:680px){.next{grid-template-columns:1fr}}
.box.dashed{border-style:dashed;background:transparent;color:var(--ink-2)}
.foot{padding-top:12px;border-top:2px solid var(--ink);font-family:var(--f-mono);font-size:.68rem;color:var(--ink-3);line-height:1.8}
@media print{
  body{background:#fff;color:#000;font-size:9.5pt}
  .page{max-width:none;padding:0}
  #en,.lang,.ruler,.shot{display:none}
  .case,table.mx,.cycle,.beyond{break-inside:avoid}
  h2{break-after:avoid}
  @page{size:A4;margin:12mm}
}
"""

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gabriela Dória · Portfólio de IA</title>
<meta name="description" content="Projetos de IA aplicada de Gabriela Dória, Engenharia Ambiental na Poli-USP: um app em uso por 25 pessoas, 16 agentes com Claude e demos feitas do zero, com problema, o que fiz e resultado.">
<meta name="author" content="Gabriela Dória">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:locale:alternate" content="en_US">
<meta property="og:title" content="Gabriela Dória · Portfólio de IA">
<meta property="og:description" content="Encontro o gargalo, construo a solução e meço se funcionou. Cinco casos com problema, o que eu fiz e resultado.">
<meta property="og:url" content="https://gabriela-doria.github.io/ai-portfolio/">
<meta property="og:image" content="https://gabriela-doria.github.io/ai-portfolio/assets/foto-gabriela.jpg">
<meta name="twitter:card" content="summary">
<meta name="color-scheme" content="light dark">
<link rel="canonical" href="https://gabriela-doria.github.io/ai-portfolio/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='4' fill='%230E5259'/%3E%3Ctext x='16' y='22' font-family='Arial' font-size='15' font-weight='700' fill='%23fff' text-anchor='middle'%3EGD%3C/text%3E%3C/svg%3E">
<style>"""

html = HEAD + CSS + "</style>\n</head>\n<body>\n<main>" + page("pt") + page("en") + "</main>\n</body>\n</html>\n"
pathlib.Path("index.html").write_text(html, encoding="utf-8")
print("index.html:", len(html), "bytes")
