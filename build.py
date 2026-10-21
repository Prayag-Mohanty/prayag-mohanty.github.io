"""Generates the static pages. Run: python3 build.py"""
import html, re
NAV=[("index.html","About"),("blog.html","Blog"),("research.html","Research"),("projects.html","Projects"),("experience.html","Experience"),("academics.html","Academics"),("cv.pdf","CV")]
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Lora:wght@500;600&amp;display=swap" rel="stylesheet">'
CSS=open("style.css").read()
JS=open("script.js").read()
DL=' download="Prayag_Mohanty_CV.pdf"'
def page(fn,title,body):
    body=re.sub(r"@@(\w+)@@",lambda m:LOGO[m.group(1)],body)
    nav="".join(f'<a href="{h}"{" class=on" if h==fn else ""}{DL if h=="cv.pdf" else ""}>{t}</a>' for h,t in NAV)
    open(fn,"w").write(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Prayag Mohanty: M.Tech researcher in computer architecture and VLSI at IIT Bombay.">
{FONTS}
<style>{CSS}</style>
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body>
<header class="nav"><div class="wrap"><a class="brand" href="index.html">Prayag Mohanty</a><div class="actions"><nav id="menu">{nav}</nav><button id="theme" aria-label="Toggle theme" title="Toggle theme">☀</button><button id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu">☰</button></div></div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">© <span id="year"></span> Prayag Mohanty.</div></footer>
<script>{JS}</script>
</body>
</html>
''')
I=lambda p:f'<span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg></span>'
CHIP=I('<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>')
LAYERS=I('<path d="M12 2 2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>')
SHIELD=I('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>')
GH="https://github.com/Prayag-Mohanty"
LI="https://www.linkedin.com/in/prayag-mohanty"
MAIL="mailto:24m1177@iitb.ac.in"
# Brand logo paths from Simple Icons (CC0); mail and globe are outline icons.
LOGO={
 "github":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>',
 "linkedin":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
 "medium":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.21 0A4.201 4.201 0 0 0 0 4.21v15.58A4.201 4.201 0 0 0 4.21 24h15.58A4.201 4.201 0 0 0 24 19.79v-1.093c-.137.013-.278.02-.422.02-2.577 0-4.027-2.146-4.09-4.832a7.592 7.592 0 0 1 .022-.708c.093-1.186.475-2.241 1.105-3.022a3.885 3.885 0 0 1 1.395-1.1c.468-.237 1.127-.367 1.664-.367h.023c.101 0 .202.004.303.01V4.211A4.201 4.201 0 0 0 19.79 0Zm.198 5.583h4.165l3.588 8.435 3.59-8.435h3.864v.146l-.019.004c-.705.16-1.063.397-1.063 1.254h-.003l.003 10.274c.06.676.424.885 1.063 1.03l.02.004v.145h-4.923v-.145l.019-.005c.639-.144.994-.353 1.054-1.03V7.267l-4.745 11.15h-.261L6.15 7.569v9.445c0 .857.358 1.094 1.063 1.253l.02.004v.147H4.405v-.147l.019-.004c.705-.16 1.065-.397 1.065-1.253V6.987c0-.857-.358-1.094-1.064-1.254l-.018-.004zm19.25 3.668c-1.086.023-1.733 1.323-1.813 3.124H24V9.298a1.378 1.378 0 0 0-.342-.047Zm-1.862 3.632c-.1 1.756.86 3.239 2.204 3.634v-3.634z"/></svg>',
 "youtube":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>',
 "behance":'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.969 16.927a2.561 2.561 0 0 0 1.901.677 2.501 2.501 0 0 0 1.531-.475c.362-.235.636-.584.779-.99h2.585a5.091 5.091 0 0 1-1.9 2.896 5.292 5.292 0 0 1-3.091.88 5.839 5.839 0 0 1-2.284-.433 4.871 4.871 0 0 1-1.723-1.211 5.657 5.657 0 0 1-1.08-1.874 7.057 7.057 0 0 1-.383-2.393c-.005-.8.129-1.595.396-2.349a5.313 5.313 0 0 1 5.088-3.604 4.87 4.87 0 0 1 2.376.563c.661.362 1.231.87 1.668 1.485a6.2 6.2 0 0 1 .943 2.133c.194.821.263 1.666.205 2.508h-7.699c-.063.79.184 1.574.688 2.187ZM6.947 4.084a8.065 8.065 0 0 1 1.928.198 4.29 4.29 0 0 1 1.49.638c.418.303.748.711.958 1.182.241.579.357 1.203.341 1.83a3.506 3.506 0 0 1-.506 1.961 3.726 3.726 0 0 1-1.503 1.287 3.588 3.588 0 0 1 2.027 1.437c.464.747.697 1.615.67 2.494a4.593 4.593 0 0 1-.423 2.032 3.945 3.945 0 0 1-1.163 1.413 5.114 5.114 0 0 1-1.683.807 7.135 7.135 0 0 1-1.928.259H0V4.084h6.947Zm-.235 12.9c.308.004.616-.029.916-.099a2.18 2.18 0 0 0 .766-.332c.228-.158.411-.371.534-.619.142-.317.208-.663.191-1.009a2.08 2.08 0 0 0-.642-1.715 2.618 2.618 0 0 0-1.696-.505h-3.54v4.279h3.471Zm13.635-5.967a2.13 2.13 0 0 0-1.654-.619 2.336 2.336 0 0 0-1.163.259 2.474 2.474 0 0 0-.738.62 2.359 2.359 0 0 0-.396.792c-.074.239-.12.485-.137.734h4.769a3.239 3.239 0 0 0-.679-1.785l-.002-.001Zm-13.813-.648a2.254 2.254 0 0 0 1.423-.433c.399-.355.607-.88.56-1.413a1.916 1.916 0 0 0-.178-.891 1.298 1.298 0 0 0-.495-.533 1.851 1.851 0 0 0-.711-.274 3.966 3.966 0 0 0-.835-.073H3.241v3.631h3.293v-.014ZM21.62 5.122h-5.976v1.527h5.976V5.122Z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
 "cv":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M12 18v-6M9 15l3 3 3-3"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>',
}
def ico(href,name,label,cls="ico",extra=""): return f'<a class="{cls}" href="{href}" aria-label="{label}" title="{label}"{extra}>{LOGO[name]}</a>'
def pills(): return ico("cv.pdf","cv","Download CV (PDF)",extra=DL)+ico(MAIL,"mail","Email")+ico(GH,"github","GitHub")+ico(LI,"linkedin","LinkedIn")

# ---------- About ----------
page("index.html","Prayag Mohanty",f'''
<div class="about"><div>
<h1>Prayag Mohanty</h1>
<p class="sub">M.Tech student, EE (Integrated Circuits &amp; Systems), IIT Bombay</p>
<p>Hey! I'm Prayag, an M.Tech student at IIT Bombay, advised by <strong>Prof. Virendra Singh</strong> at the Computer Architecture and Dependable Systems Lab (CADSL). I did my B.E. (Hons.) in Electrical &amp; Electronics Engineering at BITS Pilani, Goa campus.</p>
<p>I'm interested in computer architecture, especially where GPUs waste on-chip resources. I'm currently working on address translation for multi-chip-module GPUs, and I previously designed a locality-aware victim cache for GPU L1 data caches. I also enjoy taking designs all the way from RTL to GDSII.</p>
<p>Outside academics, I play badminton, take part in quizzes, and write.</p>
</div>
<div class="side"><img class="photo" src="photo.jpg" alt="Prayag Mohanty" width="280" height="280">Mumbai, India<div class="pills">{pills()}</div></div></div>

<h2>Research Interests</h2>
<div class="cards">
<div class="card">{CHIP}<h3>Computer Architecture</h3></div>
<div class="card">{LAYERS}<h3>GPU Memory Systems</h3></div>
<div class="card">{SHIELD}<h3>Dependable Systems &amp; VLSI</h3></div>
</div>
<p style="margin-top:28px">I am a part of the following groups:</p>
<ul class="list">
<li><a href="research.html"><strong>CADSL</strong></a> — Computer Architecture &amp; Dependable Systems Lab<small>Prof. Virendra Singh · IIT Bombay</small></li>
<li><strong>WEL</strong> — Wadhwani Electronics Laboratory<small>Research Assistant · IIT Bombay</small></li>
</ul>

<h2>News</h2>
<ul class="news">
<li><span class="date">2026</span><span>Submitted our paper on locality-aware victim caching for GPUs to ICCD 2026.</span></li>
<li><span class="date">2026</span><span>Presented a poster on the victim cache at the Indo-Japanese Workshop on Trustable Cyber-Physical Cognitive Systems, IIT Bombay.</span></li>
<li><span class="date">2026</span><span>Won the IIT Bombay PG General Championship in badminton (men's).</span></li>
<li><span class="date">2025</span><span>Won the Institute Badminton League and the NTPC Electron Quiz Western Regionals.</span></li>
<li><span class="date">2024</span><span>Started my M.Tech at IIT Bombay.</span></li>
</ul>
<div class="social">{pills()}{ico("https://medium.com/@topper1728","medium","Medium")}{ico("https://www.youtube.com/@prayag_mohanty","youtube","YouTube")}{ico("https://www.behance.net/prayagmohanty","behance","Behance")}</div>
<p class="lead" style="text-align:center;font-size:14px">Feel free to reach out to me. I would love to have a chat!</p>
''')

# ---------- Research ----------
def tl(year,title,body): return f'<div class="card tl"><span class="year">{year}</span><h3>{title}</h3><p>{body}</p></div>'
page("research.html","Research · Prayag Mohanty",f'''
<h1>Research</h1><p class="sub">GPU architecture and memory systems</p>
<div class="cards" style="grid-template-columns:1fr">
{tl("Jul 2025 – Present","Address Translation for Multi-Chip-Module GPUs","M.Tech thesis, advised by Prof. Virendra Singh. Investigating virtual-memory translation as a bottleneck when the TLB and page-walk hierarchy is split across dies. Proposes coupling TLB and cache replacement through dead-page prediction at the L1 TLB, prototyped on the MGvm MCM-GPU simulator. Targeting a conference submission by mid-2027.")}
{tl("Jan – May 2026","Locality-Aware Victim Cache for GPGPU L1 Data Caches","Co-designed a victim cache held in underused register-file capacity, with a warp scheduler that favours warps whose working set is still resident, so retained L1D lines are re-referenced before eviction. Implemented end to end in GPGPU-Sim on an NVIDIA Volta GV100 configuration for a 1.042× IPC gain over baseline. Presented as a poster at the Indo-Japanese Workshop on Trustable Cyber-Physical Cognitive Systems, IIT Bombay (2026).")}
{tl("Jul – Dec 2025","Out-of-Order Scheduling for GPUs","M.Tech seminar. Surveyed seven out-of-order GPU proposals from ISCA, HPCA, TPDS and TACO (2016–2024), tabulating performance, power and area trade-offs: 6.9–38% speedup for 0.007–13% power and 0.05–2.4% area. Showed that PTX-level simulation overstates available ILP, so SASS-level evaluation is the right baseline.")}
</div>
<h2>Publications</h2>
<ul class="list"><li><strong>Locality-Aware Victim Caching with Locality-Aware Warp Scheduling for GPUs</strong><small>P. Mohanty and V. Singh · IEEE International Conference on Computer Design (ICCD) 2026 · under review</small></li></ul>
''')

# ---------- Projects ----------
hw=[("2026","SS16: 16-bit superscalar processor","In-order superscalar core in SystemVerilog with a two-pass assembler, a golden instruction-set simulator and an automated co-simulation regression. Out-of-order extension (rename, ROB, issue queue) in progress.",["SystemVerilog"]),
("2026","6-stage pipelined RISC processor and SAT-based ATPG","Full datapath with forwarding and interlocks in VHDL, plus SAT-based ATPG for the 74181 ALU that cut ATPG effort 3.67×.",["VHDL","ATPG"]),
("2026","FHSS secure transmission with a hardware LWE engine","Learning-With-Errors encryption core on a PYNQ-Z2, interfaced over AXI-Lite and AXI-DMA for a 12.87× speedup over software, with frequency hopping through a custom GNU Radio module on a USRP.",["Verilog","FPGA"]),
("2026","Microarchitectural side-channels on RISC-V out-of-order cores","Reproduced Spectre-class cache and prefetcher side-channel primitives on a RISC-V out-of-order core, with the toolchain and full-system gem5 + Chipyard flow built end to end.",["gem5","Chipyard"]),
("2025","ML-driven LLC partitioning for CPU-GPU SoCs","Hardware perceptron that predicts per-core cache sensitivity to set LLC way-masks every 1M cycles, gaining 8.36% on CPU at a 7.5% GPU cost over a static split. Instrumented gem5 for the motivating results.",["gem5"]),
("2025","Spiking neural networks and compute-in-memory","Compared supervised deep SNNs with unsupervised STDP on MNIST (93.8% for the supervised model) and evaluated compute-in-memory inference in SpikeSim on a 64×64 crossbar at 65 nm.",["Python","SNN"]),
("2024","RTL-to-GDSII sequential MAC","16×16 shift-and-add multiplier taken through the full OpenLane flow on SkyWater sky130, closing at 5.53 ns setup with zero DRC violations and clean LVS. 6× smaller and 19× lower power than a parallel FIR.",["OpenLane","sky130"]),
("2023","CNN inference accelerator on FPGA","B.E. thesis. AlexNet accelerator on a Zedboard (Zynq-7020) with Vivado HLS: 0.74 GFLOPS at about 0.9 W, with roughly 10× lower power than comparable published designs.",["Vivado HLS","FPGA"])]
repos=[("MGVm-GPU","Go","Multi-chip-module GPU simulator work behind my address-translation research."),
("gpgpu-lwdsp","C","GPGPU-Sim experiments for locality-aware victim caching in L1D."),
("lwsdp","C","Locality-aware L1D cache extension, companion to the GPGPU-Sim work."),
("GPU-SoC","","CPU-GPU SoC shared last-level cache partitioning experiments."),
("RISC-V-Spectre","","Spectre-class side-channel experiments on RISC-V out-of-order cores."),
("Neuromorphic-Computing","Jupyter","Spiking neural network experiments from the neuromorphic engineering course."),
("badminton-scoreboard","JavaScript","Upload a match recording and get a scoreboard tracking the players' points through the match."),
("buzz-n-pounce","JavaScript","Free online quiz buzzer with a pounce round."),
("x-quiz-site","TypeScript","A quiz website built in TypeScript."),
("QM","JavaScript","A JavaScript side project."),
("Family-Tree","JavaScript","Interactive family tree, deployed on Vercel."),
("Sharada-script-practice-tool","HTML","A tool for practising the Sharada script."),
("wel-website","HTML","Website for the Wadhwani Electronics Laboratory, IIT Bombay.")]
SITES={"wel-website":"https://www.ee.iitb.ac.in/~wel_iitb","Family-Tree":"https://family-tree-praymo.vercel.app","QM":"https://prayag-mohanty.github.io/QM/","badminton-scoreboard":"https://prayag-mohanty.github.io/badminton-scoreboard/"}
HWREPO={"Microarchitectural side-channels on RISC-V out-of-order cores":"RISC-V-Spectre","ML-driven LLC partitioning for CPU-GPU SoCs":"GPU-SoC","Spiking neural networks and compute-in-memory":"Neuromorphic-Computing"}
def links(repo,site=None):
    out=[]
    if repo: out.append(ico(f"{GH}/{repo}","github","GitHub repository","ico sm"))
    if site: out.append(ico(site,"globe","Live site","ico sm"))
    return f'<div class="plinks">{"".join(out)}</div>' if out else ''
hwh="".join(f'<div class="card tl"><span class="year">{y}</span><h3>{t}</h3><p>{d}</p><div class="tags">{"".join(f"<span>{x}</span>" for x in g)}</div>{links(HWREPO.get(t))}</div>' for y,t,d,g in hw)
rh="".join(f'<div class="card"><h3>{n}</h3><p>{d}</p>'+(f'<div class="tags"><span>{l}</span></div>' if l else '')+links(n,SITES.get(n))+'</div>' for n,l,d in repos)
page("projects.html","Projects · Prayag Mohanty",f'''
<h1>Projects</h1><p class="sub">Hardware, architecture and side projects</p>
<h2 style="margin-top:0">Hardware &amp; Architecture</h2>
<div class="cards" style="grid-template-columns:1fr">{hwh}</div>
<h2>Side Projects</h2>
<p class="lead">Public repositories from <a href="{GH}">github.com/Prayag-Mohanty</a>.</p>
<div class="cards">{rh}</div>
''')

# ---------- Blog ----------
page("blog.html","Blog · Prayag Mohanty",'''
<h1>Blog</h1><p class="sub">Writing, videos and design</p>
<h2 style="margin-top:0">Latest from Medium</h2>
<div id="posts" class="cards"><p class="lead">Loading posts…</p></div>
<p class="lead" style="margin-top:18px"><a href="https://medium.com/@topper1728">Read everything on Medium →</a></p>
<h2>Elsewhere</h2>
<div class="cards">
<a class="card" href="https://www.youtube.com/@prayag_mohanty/featured"><span class="icon">@@youtube@@</span><h3>YouTube</h3><p>Videos on my channel, @prayag_mohanty.</p></a>
<a class="card" href="https://www.behance.net/prayagmohanty"><span class="icon">@@behance@@</span><h3>Behance</h3><p>Design work and creative projects.</p></a>
</div>
<script>
(function(){
  var box=document.getElementById('posts');
  var fail=function(){box.innerHTML='<p class="lead">Could not load posts right now. <a href="https://medium.com/@topper1728">Read them on Medium →</a></p>'};
  var esc=function(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML};
  var card=function(p){
    var img=p.thumbnail?'<img class="thumb" src="'+esc(p.thumbnail)+'" alt="" loading="lazy">':'';
    return '<a class="card post" href="'+esc(p.link)+'">'+img+'<span class="year">'+esc(p.date)+'</span><h3>'+esc(p.title)+'</h3><p>'+esc(p.excerpt)+'…</p></a>';
  };
  var show=function(ps){if(!ps||!ps.length)throw 0;box.innerHTML=ps.map(card).join('')};
  var strip=function(h){return h.replace(/<[^>]+>/g,' ').replace(/\\s+/g,' ').trim().slice(0,160)};
  fetch('posts.json',{cache:'no-cache'}).then(function(r){return r.json()}).then(show)
    .catch(function(){
      return fetch('https://api.rss2json.com/v1/api.json?rss_url='+encodeURIComponent('https://medium.com/feed/@topper1728'))
        .then(function(r){return r.json()})
        .then(function(d){show((d.items||[]).map(function(p){return {title:p.title,link:p.link,thumbnail:p.thumbnail,excerpt:strip(p.description),
          date:new Date(p.pubDate.replace(' ','T')+'Z').toLocaleDateString('en-US',{year:'numeric',month:'short',day:'numeric'})}}))});
    }).catch(fail);
})();
</script>
''')

# ---------- Experience ----------
page("experience.html","Experience · Prayag Mohanty",f'''
<h1>Experience</h1><p class="sub">Work, teaching and beyond</p>
<div class="cards" style="grid-template-columns:1fr">
{tl("Jul 2024 – Present","Research Assistant · Wadhwani Electronics Laboratory, IIT Bombay","Support the Communication Lab and Electronic Design Lab, train incoming TAs on the experiments, and maintain the lab website, social media and external workshops.")}
{tl("Jul 2025 – Present","Graduate Researcher · CADSL, IIT Bombay","Computer Architecture and Dependable Systems Lab, advised by Prof. Virendra Singh.")}
{tl("Jul – Aug 2022","Summer Intern · 313 Army Workshop, Pithoragarh","Applied supervised learning to detect drones in night-vision footage for an anti-drone defence system, under the BITS PS-1 programme.")}
</div>
<h2>Beyond the lab</h2>
<div class="cards" style="grid-template-columns:1fr">
<div class="card"><h3>Badminton</h3><p>Winner, IIT Bombay PG General Championship (2026) and Institute Badminton League (2025). Represented IIT Bombay at Inter-IIT 2025 and BITS Goa at Inter-BITS (winners, 2024).</p></div>
<div class="card"><h3>Quizzing</h3><p>Winner of the NTPC Electron Quiz Western Regionals (2025), Zerodha Varsity Quiz Mumbai (2024, 2026) and Tata Crucible Goa (2021). Finalist at Nihilanth 2026, the Inter IIT-IIM quizzing festival.</p></div>
<div class="card"><h3>Hosting</h3><p>Hosted the intra-campus quiz “Lord of the Rings” (2026) and anchored the PG Night of PG Cultural Phase 1 at IIT Bombay (2024).</p></div>
</div>
''')

# ---------- Academics ----------
co=[("IIT Bombay (M.Tech)",[("EE797","M.Tech Project"),("EE739","Processor Design"),("EE748","Advanced Topics in Computer Architecture"),("EE746","Neuromorphic Engineering"),("EE712","Embedded Systems Design"),("EE691","Research and Development Project"),("EE694","M.Tech Seminar"),("EE671","VLSI Design")])]
skills=[("Languages","SystemVerilog, Verilog, VHDL, C++, C, Python, CUDA"),("Architecture &amp; simulation","gem5, GPGPU-Sim, AccelSim, MGvm, Chipyard/BOOM, SpikeSim"),("EDA &amp; flow","OpenLane, Yosys, OpenSTA, Magic, KLayout, sky130, Xilinx Vivado &amp; HLS, Quartus Prime"),("Platforms &amp; ML","PYNQ / Zynq-7020, AXI, PCB design, GNU Radio, PyTorch, scikit-learn")]
page("academics.html","Academics · Prayag Mohanty",f'''
<h1>Academics</h1><p class="sub">Education, courses and skills</p>
<div class="cards" style="grid-template-columns:1fr">
{tl("2024 – 2027 (expected)","Indian Institute of Technology Bombay","M.Tech, Electrical Engineering (Integrated Circuits &amp; Systems)")}
{tl("2020 – 2024","BITS Pilani, K. K. Birla Goa Campus","B.E. (Hons.), Electrical &amp; Electronics Engineering")}
</div>
<h2>Courses</h2>
<div class="cols">{"".join(f'<div class="card"><span class="code">{c}</span> - {n}</div>' for c,n in co[0][1])}</div>
<p class="lead" style="margin-top:14px">Also: VLSI Testing &amp; Verification, Machine Learning.</p>
<h2>Technical Skills</h2>
<div class="cards" style="grid-template-columns:1fr">{"".join(f'<div class="card"><span class="code">{k}</span>: {v}</div>' for k,v in skills)}</div>
''')
