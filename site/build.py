"""Build the channel website from each video's DESCRIPTION.md.

Run: python3 site/build.py  ->  writes site/index.html
"""
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "index.html"

CHANNEL = "Loulou"
TAGLINE = "Scary things caught on camera, and the strangest true stories in history."
BANNER = ("https://d2ol7oe51mr4n9.cloudfront.net/user_3JmeyhT6HR0AQ60Jl0BCMTgyyoT/"
          "2d0bd3d1-3a38-453a-b56b-93de751f00df.jpg")

# Folders whose videos are scary compilations; everything else is history.
SCARY = {"forest", "ring-doorbell", "scary-top10", "scary-top10-v2"}

URL = re.compile(r"https?://\S+")


def added_date(path):
    out = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%as", "--", str(path)],
        cwd=ROOT, capture_output=True, text=True).stdout.split()
    return out[-1] if out else ""


def parse(path):
    text = path.read_text()
    title = re.search(r"\*\*Title:\*\*\s*(.+)", text).group(1).strip()
    video = re.search(r"\*\*Video:\*\*\s*(\S+)", text)
    body = text.split("**Description:**", 1)[1]
    body = body.split("\n## ", 1)[0]  # drop thumbnail sections

    paras = [p.strip() for p in body.strip().split("\n\n")]
    intro = []
    for p in paras:
        if p.startswith(("⏱", "👉", "💬", "🎥", "#")):
            break
        intro.append(p)

    chapters = re.findall(r"^(\d+:\d\d)\s+(.+)$", body, re.M)
    credits = []
    if "🎥" in body:
        block = body.split("🎥", 1)[1].split("\n\n", 1)[0]
        for line in block.splitlines()[1:]:
            m = URL.search(line)
            if m:
                credits.append({"name": line[:m.start()].rstrip(" :,"),
                                "url": m.group(0)})
    question = re.search(r"💬\s*(.+)", body)
    tags = re.findall(r"#([A-Za-z]\w+)", body.split("💬")[-1])
    thumbs = re.findall(r"^\d+\.\s.*?(https://\S+\.jpg)", text, re.M)

    slug = path.parent.name
    return {
        "slug": slug,
        "kind": "scary" if slug in SCARY else "history",
        "date": added_date(path),
        "title": title,
        "intro": intro,
        "chapters": [{"t": t, "label": l} for t, l in chapters],
        "credits": credits,
        "question": question.group(1).strip() if question else "",
        "tags": tags[:8],
        "thumb": thumbs[0] if thumbs else "",
        "video": video.group(1) if video else "",
    }


def main():
    videos = [parse(p) for p in sorted(ROOT.glob("*/DESCRIPTION.md"))]
    videos.sort(key=lambda v: v["date"], reverse=True)
    data = json.dumps(videos, ensure_ascii=False).replace("</", "<\\/")
    page = (TEMPLATE
            .replace("{{CHANNEL}}", html.escape(CHANNEL))
            .replace("{{TAGLINE}}", html.escape(TAGLINE))
            .replace("{{BANNER}}", BANNER)
            .replace("{{DATA}}", data))
    OUT.write_text(page)
    print(f"wrote {OUT.relative_to(ROOT)} with {len(videos)} videos")


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{CHANNEL}}</title>
<meta name="description" content="{{TAGLINE}}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #0c0d10; --panel: #15171c; --panel-2: #1c1f26; --line: #2a2e38;
  --text: #ecebe6; --muted: #9a9ca5; --accent: #e5483b; --history: #d9a441;
  --radius: 12px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.6 Inter, system-ui, sans-serif; }
a { color: inherit; }
.wrap { max-width: 1180px; margin: 0 auto; padding: 0 16px; }

header.hero { position: relative; min-height: 440px; display: flex; align-items: flex-end; overflow: hidden; }
header.hero::before { content: ""; position: absolute; inset: -20px; z-index: -1;
  background: url("{{BANNER}}") center/cover no-repeat; filter: blur(14px) brightness(.5); }
header.hero::after { content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, rgba(12,13,16,.2) 0%, rgba(12,13,16,.6) 60%, var(--bg) 100%); }
header.hero { isolation: isolate; }
nav { position: absolute; top: 0; left: 0; right: 0; }
nav .wrap { display: flex; justify-content: space-between; align-items: center; padding-top: 18px; }
.logo { font: 700 22px Oswald, sans-serif; letter-spacing: .08em; text-transform: uppercase; }
.logo span { color: var(--accent); }
nav a.sub { background: var(--accent); color: #fff; text-decoration: none; font-weight: 600;
  padding: 8px 16px; border-radius: 999px; font-size: 14px; }
.hero h1 { font: 700 clamp(38px, 7vw, 76px)/1 Oswald, sans-serif; text-transform: uppercase;
  margin: 0 0 12px; letter-spacing: .02em; }
.hero p { color: #cfcfd4; font-size: clamp(16px, 2.2vw, 20px); max-width: 620px; margin: 0 0 22px; }
.stats { display: flex; gap: 28px; flex-wrap: wrap; padding-bottom: 36px; }
.stats b { display: block; font: 700 28px Oswald, sans-serif; }
.stats small { color: var(--muted); text-transform: uppercase; letter-spacing: .1em; font-size: 12px; }

.controls { position: sticky; top: 0; z-index: 5; background: rgba(12,13,16,.92);
  backdrop-filter: blur(8px); border-bottom: 1px solid var(--line); }
.controls .wrap { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; padding: 12px 16px; }
.tab { background: var(--panel); border: 1px solid var(--line); color: var(--text);
  padding: 8px 16px; border-radius: 999px; cursor: pointer; font: 500 14px Inter, sans-serif; }
.tab[aria-pressed="true"] { background: var(--text); color: var(--bg); border-color: var(--text); }
input[type=search] { margin-left: auto; flex: 1 1 200px; max-width: 320px; background: var(--panel);
  border: 1px solid var(--line); color: var(--text); padding: 9px 14px; border-radius: 999px;
  font: 14px Inter, sans-serif; }

main { padding: 32px 0 64px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 22px; }
.card { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius);
  overflow: hidden; cursor: pointer; display: flex; flex-direction: column; text-align: left;
  color: inherit; font: inherit; padding: 0; transition: transform .15s, border-color .15s; }
.card:hover, .card:focus-visible { transform: translateY(-3px); border-color: #444a58; outline: none; }
.thumb { aspect-ratio: 16/9; background: var(--panel-2); position: relative; overflow: hidden; }
.thumb img { width: 100%; height: 100%; object-fit: cover; display: block; }
.thumb .ph { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
  padding: 20px; text-align: center; font: 700 22px/1.15 Oswald, sans-serif; text-transform: uppercase;
  background: radial-gradient(circle at 30% 20%, #3a2f1c, #16130d 70%); color: #f1dfb6; }
.badge { position: absolute; top: 10px; left: 10px; font: 600 11px Inter, sans-serif;
  text-transform: uppercase; letter-spacing: .08em; padding: 4px 8px; border-radius: 6px;
  background: var(--accent); color: #fff; }
.badge.history { background: var(--history); color: #1a1408; }
.dur { position: absolute; bottom: 8px; right: 8px; background: rgba(0,0,0,.8);
  font-size: 12px; padding: 2px 6px; border-radius: 4px; }
.card .body { padding: 14px 16px 18px; }
.card h3 { margin: 0 0 6px; font-size: 17px; line-height: 1.35; }
.card p { margin: 0; color: var(--muted); font-size: 14px;
  display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.empty { color: var(--muted); text-align: center; padding: 48px 0; }

dialog { width: min(860px, calc(100% - 24px)); max-height: calc(100% - 24px); padding: 0;
  background: var(--panel); color: var(--text); border: 1px solid var(--line); border-radius: var(--radius); }
dialog::backdrop { background: rgba(0,0,0,.75); }
.d-media img, .d-media video { width: 100%; display: block; aspect-ratio: 16/9; object-fit: cover; background: #000; }
.d-body { padding: 20px 24px 28px; }
.d-body h2 { font: 700 28px/1.15 Oswald, sans-serif; margin: 0 0 14px; }
.d-body h4 { margin: 24px 0 8px; font-size: 13px; text-transform: uppercase; letter-spacing: .1em; color: var(--muted); }
.d-body p { margin: 0 0 12px; color: #d4d4d9; }
.chapters { list-style: none; margin: 0; padding: 0; display: grid; gap: 2px; }
.chapters li { display: flex; gap: 14px; padding: 6px 10px; border-radius: 6px; }
.chapters li:nth-child(odd) { background: var(--panel-2); }
.chapters time { font-variant-numeric: tabular-nums; color: var(--accent); min-width: 44px; font-weight: 600; }
.credits { margin: 0; padding-left: 18px; color: var(--muted); font-size: 14px; }
.credits a { color: var(--muted); }
.tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 20px; }
.tags span { font-size: 12px; color: var(--muted); background: var(--panel-2); padding: 3px 9px; border-radius: 999px; }
.question { margin-top: 20px; padding: 14px 16px; border-left: 3px solid var(--accent); background: var(--panel-2); border-radius: 0 8px 8px 0; }
.close { position: absolute; top: 10px; right: 10px; width: 38px; height: 38px; border-radius: 50%;
  border: 0; background: rgba(0,0,0,.65); color: #fff; font-size: 22px; cursor: pointer; z-index: 2; }

footer { border-top: 1px solid var(--line); color: var(--muted); font-size: 14px; padding: 28px 0 40px; }
footer .wrap { display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; }
@media (max-width: 560px) { header.hero { min-height: 380px; padding-top: 80px; } .stats { gap: 18px; } .stats b { font-size: 22px; } .stats small { font-size: 10px; } input[type=search] { max-width: none; margin-left: 0; } }
</style>
</head>
<body>
<header class="hero">
  <nav><div class="wrap">
    <div class="logo">{{CHANNEL}}<span>.</span></div>
    <a class="sub" href="#videos">Watch the videos</a>
  </div></nav>
  <div class="wrap">
    <h1>{{CHANNEL}}</h1>
    <p>{{TAGLINE}}</p>
    <div class="stats" id="stats"></div>
  </div>
</header>

<div class="controls" id="videos"><div class="wrap">
  <button class="tab" data-f="all" aria-pressed="true">All</button>
  <button class="tab" data-f="scary" aria-pressed="false">Scary videos</button>
  <button class="tab" data-f="history" aria-pressed="false">History stories</button>
  <input type="search" id="q" placeholder="Search videos, people, places…" aria-label="Search videos">
</div></div>

<main><div class="wrap">
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" hidden>No videos match that search.</div>
</div></main>

<dialog id="dlg"><button class="close" aria-label="Close">×</button><div id="dbody"></div></dialog>

<footer><div class="wrap">
  <span>© {{CHANNEL}}. Clips in scary compilations belong to their credited owners.</span>
  <a href="#">Back to top ↑</a>
</div></footer>

<script>
const VIDEOS = {{DATA}};
const esc = s => String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const length = v => v.chapters.length ? v.chapters[v.chapters.length - 1].t : "";
const label = k => k === "scary" ? "Scary" : "History";

const scary = VIDEOS.filter(v => v.kind === "scary").length;
document.getElementById("stats").innerHTML =
  `<div><b>${VIDEOS.length}</b><small>Videos</small></div>` +
  `<div><b>${scary}</b><small>Scary compilations</small></div>` +
  `<div><b>${VIDEOS.length - scary}</b><small>History stories</small></div>`;

let filter = "all";
const grid = document.getElementById("grid"), q = document.getElementById("q");

function render() {
  const term = q.value.trim().toLowerCase();
  const list = VIDEOS.filter(v => (filter === "all" || v.kind === filter) &&
    (!term || [v.title, ...v.intro, ...v.chapters.map(c => c.label), ...v.tags].join(" ").toLowerCase().includes(term)));
  grid.innerHTML = list.map(v => `
    <button class="card" data-slug="${v.slug}">
      <div class="thumb">
        ${v.thumb ? `<img src="${esc(v.thumb)}" alt="" loading="lazy">` : `<div class="ph">${esc(v.title)}</div>`}
        <span class="badge ${v.kind}">${label(v.kind)}</span>
        ${length(v) ? `<span class="dur">${length(v)}</span>` : ""}
      </div>
      <div class="body"><h3>${esc(v.title)}</h3><p>${esc(v.intro[0] || "")}</p></div>
    </button>`).join("");
  document.getElementById("empty").hidden = list.length > 0;
}

document.querySelectorAll(".tab").forEach(b => b.onclick = () => {
  filter = b.dataset.f;
  document.querySelectorAll(".tab").forEach(t => t.setAttribute("aria-pressed", t === b));
  render();
});
q.oninput = render;

const dlg = document.getElementById("dlg");
grid.onclick = e => {
  const card = e.target.closest(".card");
  if (!card) return;
  const v = VIDEOS.find(x => x.slug === card.dataset.slug);
  const media = v.video
    ? `<video controls preload="none" poster="${esc(v.thumb)}" src="${esc(v.video)}"></video>`
    : v.thumb ? `<img src="${esc(v.thumb)}" alt="">` : "";
  document.getElementById("dbody").innerHTML = `
    ${media ? `<div class="d-media">${media}</div>` : ""}
    <div class="d-body">
      <h2>${esc(v.title)}</h2>
      ${v.intro.map(p => `<p>${esc(p)}</p>`).join("")}
      ${v.chapters.length ? `<h4>Chapters</h4><ol class="chapters">${v.chapters.map(c =>
        `<li><time>${c.t}</time><span>${esc(c.label)}</span></li>`).join("")}</ol>` : ""}
      ${v.credits.length ? `<h4>Video credits</h4><ul class="credits">${v.credits.map(c =>
        `<li><a href="${esc(c.url)}" target="_blank" rel="noopener">${esc(c.name)}</a></li>`).join("")}</ul>` : ""}
      ${v.question ? `<div class="question">💬 ${esc(v.question)}</div>` : ""}
      <div class="tags">${v.tags.map(t => `<span>#${esc(t)}</span>`).join("")}</div>
    </div>`;
  dlg.showModal();
};
dlg.addEventListener("close", () => { const vid = dlg.querySelector("video"); if (vid) vid.pause(); });
dlg.querySelector(".close").onclick = () => dlg.close();
dlg.onclick = e => { if (e.target === dlg) dlg.close(); };

render();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
