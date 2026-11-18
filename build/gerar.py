# Gera o index.html do portfólio (PT e EN) a partir do conteúdo em build/conteudo.py.
# Uso: python3 build/gerar.py  (na raiz do repositório)
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from conteudo import page

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
.eq{display:flex;flex-wrap:nowrap;align-items:stretch;gap:6px;margin:0 0 12px}
.eq .box{flex:1 1 0;min-width:0;font-size:.82rem}
@media (max-width:680px){.eq{flex-wrap:wrap}.eq .box{flex:1 1 120px}}
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

.toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 26px}
.toc a{font-family:var(--f-mono);font-size:.72rem;text-decoration:none;color:var(--ink-2);border:1px solid var(--rule-strong);border-radius:999px;padding:4px 12px;background:var(--surface)}
.toc a b{color:var(--petrol);margin-right:4px}
.toc a:hover{border-color:var(--petrol);color:var(--petrol)}
.part{display:flex;gap:16px;align-items:flex-start;margin:34px 0 6px;padding-top:16px;border-top:2px solid var(--ink)}
.part>span{font-family:var(--f-display);font-weight:800;font-size:2.6rem;line-height:.9;color:var(--petrol)}
.part h2.ph{font-family:var(--f-display);font-size:1.45rem;letter-spacing:-.01em;text-transform:none;color:var(--ink);font-weight:800;margin:0 0 4px}
.part p{margin:0;color:var(--ink-2);font-size:.95rem;max-width:62ch}
.okr{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:0 0 10px}
@media (max-width:680px){.okr{grid-template-columns:1fr}}
.okr .o1{border:1px solid var(--rule);border-top:3px solid var(--petrol);border-radius:4px;background:var(--surface);padding:7px 10px;font-size:.84rem;line-height:1.35}
.okr .o1 .k{display:block;font-family:var(--f-mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--petrol);margin-bottom:2px}
.okr .o1.hi{background:var(--petrol-soft)}
.shot.wide{max-width:none}
.mxwrap{overflow-x:auto;margin:0 0 28px}
.mxwrap table.mx{margin:0;min-width:640px}
table.mx th span{display:inline-block;max-width:70px;line-height:1.2}
.gallery{display:grid;grid-template-columns:1fr 1fr 190px;grid-template-areas:"a a d" "b c d";gap:10px;margin:2px 0 6px;align-items:start}
.gallery .g1{grid-area:a}.gallery .g2{grid-area:b}.gallery .g3{grid-area:c}.gallery .g4{grid-area:d}
@media (max-width:680px){.gallery{grid-template-columns:1fr;grid-template-areas:"a" "d" "b" "c"}.gallery .g4{max-width:240px}}
.shot a{display:block}
.gallery .shot{margin:0;max-width:none}
.flow.two{grid-template-columns:1fr 1fr}
@media (max-width:680px){.flow.two{grid-template-columns:1fr}}
.nums.two{grid-template-columns:repeat(2,minmax(0,200px))}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:22px 32px;margin:10px 0 28px}
@media (max-width:680px){.cols{grid-template-columns:minmax(0,1fr)}}
.cols .t{font-family:var(--f-mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);display:block;margin-bottom:2px}
.cols .t.sp{margin-top:14px}
.edu{display:grid;grid-template-columns:62px 1fr;gap:5px 10px;font-size:.9rem;line-height:1.4;margin-top:6px}
.edu .yy{font-family:var(--f-mono);font-size:.68rem;color:var(--petrol);font-weight:600;padding-top:3px}
.langs{font-family:var(--f-mono);font-size:.7rem;color:var(--ink-2);margin:12px 0 0}
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
<title>Gabriela Dória · Portfólio: gestão por indicadores, dados e IA</title>
<meta name="description" content="Portfólio de Gabriela Dória, Engenharia Ambiental na Poli-USP: gestão por indicadores na Poli Social (94,9% dos KPIs), um app em uso por 25 pessoas, 16 agentes de IA e demos com dados, com problema, o que fiz e resultado.">
<meta name="author" content="Gabriela Dória">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:locale:alternate" content="en_US">
<meta property="og:title" content="Gabriela Dória · Portfólio">
<meta property="og:description" content="Encontro o gargalo, construo a solução e meço se funcionou. Casos de gestão por indicadores e de IA, com problema, o que eu fiz e resultado.">
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
