"""Generates the static pages. Run: python3 build.py"""
import html
NAV=[("index.html","About"),("blog.html","Blog"),("research.html","Research"),("projects.html","Projects"),("experience.html","Experience"),("academics.html","Academics")]
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Lora:wght@500;600&amp;display=swap" rel="stylesheet">'
CSS=open("style.css").read()
JS=open("script.js").read()
def page(fn,title,body):
    nav="".join(f'<a href="{h}"{" class=on" if h==fn else ""}>{t}</a>' for h,t in NAV)
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
<header class="nav"><div class="wrap"><a class="brand" href="index.html">Prayag Mohanty</a><nav>{nav}<button id="theme" aria-label="Toggle theme" title="Toggle theme">☀</button></nav></div></header>
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
def pills(): return f'<a class="pill" href="{MAIL}">Email</a><a class="pill" href="{GH}">GitHub</a><a class="pill" href="{LI}">LinkedIn</a>'

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
<div class="social">{pills()}<a class="pill" href="https://medium.com/@topper1728">Medium</a><a class="pill" href="https://www.youtube.com/@prayag_mohanty">YouTube</a><a class="pill" href="https://www.behance.net/prayagmohanty">Behance</a></div>
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
    if repo: out.append(f'<a href="{GH}/{repo}">GitHub ↗</a>')
    if site: out.append(f'<a href="{site}">Live site ↗</a>')
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
<a class="card" href="https://www.youtube.com/@prayag_mohanty/featured"><h3>YouTube</h3><p>Videos on my channel, @prayag_mohanty.</p></a>
<a class="card" href="https://www.behance.net/prayagmohanty"><h3>Behance</h3><p>Design work and creative projects.</p></a>
</div>
<script>
(function(){
  var box=document.getElementById('posts');
  var fail=function(){box.innerHTML='<p class="lead">Could not load posts right now. <a href="https://medium.com/@topper1728">Read them on Medium →</a></p>'};
  var esc=function(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML};
  fetch('https://api.rss2json.com/v1/api.json?rss_url='+encodeURIComponent('https://medium.com/feed/@topper1728'))
    .then(function(r){return r.json()})
    .then(function(d){
      if(!d.items||!d.items.length){fail();return}
      box.innerHTML=d.items.map(function(p){
        var text=esc(p.description.replace(/<[^>]+>/g,' ').replace(/\\s+/g,' ').trim().slice(0,160));
        var img=p.thumbnail?'<img class="thumb" src="'+esc(p.thumbnail)+'" alt="" loading="lazy">':'';
        var date=new Date(p.pubDate.replace(' ','T')+'Z').toLocaleDateString('en-US',{year:'numeric',month:'short',day:'numeric'});
        return '<a class="card post" href="'+esc(p.link)+'">'+img+'<span class="year">'+date+'</span><h3>'+esc(p.title)+'</h3><p>'+text+'…</p></a>';
      }).join('');
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
