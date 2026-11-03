import json, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont

# Reference-style edit: VHS "PLAY" title card, narrated setup over a still,
# the clip played out in full with its own audio, then slowed/zoomed analysis.
W, H, FPS = 1920, 1080, 30
MONO = "/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf"
MONO_L = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
spec = json.load(open("spec.json"))
os.makedirs("out", exist_ok=True); os.makedirs("tmp", exist_ok=True)

def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

def run(a):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + a, check=True)

def fit(crop=None):
    f = ""
    if crop:
        x, y, w, h = crop
        f = f"crop=iw*{w}:ih*{h}:iw*{x}:ih*{y},"
    return f + f"scale={W}:{H}:force_original_aspect_ratio=decrease:flags=lanczos,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,setsar=1"

def overlay_png(name, credit=None, cap=None):
    # transparent layer with the credit (bottom right) and a caption box (bottom centre)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if credit:
        f = ImageFont.truetype(SANS, 30); b = d.textbbox((0, 0), credit, font=f)
        d.text((W - 40 - (b[2] - b[0]), H - 60), credit, font=f, fill=(255, 255, 255, 190))
    if cap:
        f = ImageFont.truetype(SANS, 40); b = d.textbbox((0, 0), cap, font=f)
        tw, th = b[2] - b[0], b[3] - b[1]; x = (W - tw) // 2; y = H - 190
        d.rectangle((x - 18, y - 12, x + tw + 18, y + th + 22), fill=(20, 20, 20, 200))
        d.text((x - b[0], y - b[1] + 4), cap, font=f, fill=(255, 255, 255, 255))
    p = f"tmp/{name}.png"; im.save(p); return p

def card(n, s):
    D = 3.5
    im = Image.new("RGB", (W, H), (0, 0, 0)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(MONO, 74); d.text((70, 50), "PLAY", font=f, fill=(235, 235, 235))
    tx = 70 + d.textlength("PLAY ", font=f); d.polygon([(tx, 66), (tx, 118), (tx + 44, 92)], fill=(235, 235, 235))
    f2 = ImageFont.truetype(MONO_L, 46); b = d.textbbox((0, 0), s["title"], font=f2)
    d.text(((W - (b[2] - b[0])) // 2, H // 2 - 40), s["title"], font=f2, fill=(220, 220, 220))
    im.save(f"tmp/card{n}.png")
    # VHS feel: grain everywhere, a rolling band of static along the bottom, tape hiss
    run(["-loop", "1", "-t", str(D), "-i", f"tmp/card{n}.png",
         "-f", "lavfi", "-t", str(D), "-i", "anoisesrc=color=pink:amplitude=0.08,lowpass=f=3500,highpass=f=200",
         "-filter_complex",
         f"[0:v]format=yuv420p,noise=alls=14:allf=t,drawbox=x=0:y=ih-70:w=iw:h=6:color=white@0.35:t=fill:enable='lt(mod(t,0.5),0.25)',"
         f"drawbox=x=0:y=ih-40:w=iw:h=3:color=white@0.25:t=fill,fade=in:st=0:d=0.25,fade=out:st={D-0.3}:d=0.3[v];"
         f"[1:a]afade=in:d=0.2,afade=out:st={D-0.4}:d=0.4,aformat=sample_rates=48000:channel_layouts=stereo[a]",
         "-map", "[v]", "-map", "[a]", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", f"out/s{n:03d}.mp4"])
    return D

def intro(n, s):
    vo = f"vo/{s['vo']}.wav"; D = dur(vo) + 1.2
    run(["-ss", str(s["t"]), "-i", f"raw/{s['src']}.mp4", "-frames:v", "1", "-vf", fit(s.get("crop")), f"tmp/still{n}.png"])
    ov = overlay_png(f"ov{n}", s.get("credit"))
    frames = int(D * FPS) + 2
    run(["-loop", "1", "-i", f"tmp/still{n}.png", "-i", ov, "-i", vo,
         "-filter_complex",
         f"[0:v]scale=3840:2160,zoompan=z='1+0.06*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
         f"eq=brightness=-0.06:saturation=0.8,format=yuv420p[b];[b][1:v]overlay[v0];[v0]fade=in:d=0.4[v];"
         f"[2:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=400|400,volume=1.6,apad[a]",
         "-map", "[v]", "-map", "[a]", "-t", str(D), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", f"out/s{n:03d}.mp4"])
    return D

def clips(n, s, parts, vol, D=None, vo=None, caps=()):
    # concat parts (src,t0,t1,speed,crop); loop the list if narration runs longer
    vlen = sum((p[2] - p[1]) / p[3] for p in parts)
    if D is None: D = vlen
    seq = list(parts)
    while sum((p[2] - p[1]) / p[3] for p in seq) < D: seq += parts
    args, fc, cat = [], [], ""
    for i, p in enumerate(seq):
        src, t0, t1, sp = p[:4]; crop = p[4] if len(p) > 4 else None
        args += ["-ss", str(t0), "-t", str(t1 - t0), "-i", f"raw/{src}.mp4"]
        tempo = []; r = sp
        while r < 0.5: tempo.append("atempo=0.5"); r /= 0.5
        tempo.append(f"atempo={r}")
        fc.append(f"[{i}:v]{fit(crop)},setpts=(PTS-STARTPTS)/{sp},fps={FPS},format=yuv420p[v{i}]")
        fc.append(f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,asetpts=PTS-STARTPTS,{','.join(tempo)},volume={vol}[a{i}]")
        cat += f"[v{i}][a{i}]"
    k = len(seq)
    fc.append(f"{cat}concat=n={k}:v=1:a=1[cv][ca]")
    ov = overlay_png(f"ov{n}", s.get("credit")); args += ["-i", ov]
    oi = k; vchain = f"[cv][{oi}:v]overlay[c0]"; last = "c0"
    for j, c in enumerate(caps):
        cp = overlay_png(f"cap{n}_{j}", None, c[0]); args += ["-i", cp]
        vchain += f";[{last}][{oi + 1 + j}:v]overlay=enable='between(t,{c[1]},{c[2]})'[c{j + 1}]"; last = f"c{j + 1}"
    fc.append(vchain)
    fc.append(f"[{last}]fade=in:d=0.2[v]")
    if vo:
        args += ["-i", vo]; vi = oi + 1 + len(caps)
        fc.append(f"[{vi}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay=500|500,volume=1.6,apad[vo];[ca][vo]amix=inputs=2:duration=first:normalize=0[a]")
    else:
        fc.append("[ca]anull[a]")
    run(args + ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-t", str(D), "-r", str(FPS),
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", f"out/s{n:03d}.mp4"])
    return D

def segment(n, s):
    t = s["type"]
    if t == "card": return card(n, s)
    if t == "intro": return intro(n, s)
    if t == "play": return clips(n, s, [[s["src"], a, b, 1, s.get("crop")] for a, b in s["parts"]], s.get("vol", 1.0), caps=s.get("caps", ()))
    if t == "analysis":
        vo = f"vo/{s['vo']}.wav"
        return clips(n, s, s["parts"], s.get("vol", 0.2), D=dur(vo) + 1.2, vo=vo, caps=s.get("caps", ()))

segs = spec["segments"]
only = [int(a) for a in sys.argv[1:]] or range(len(segs))
with open("out/list.txt", "w") as f:
    for i in range(len(segs)): f.write(f"file 's{i:03d}.mp4'\n")
for i in only:
    D = segment(i, segs[i]); print(i, segs[i]["type"], round(D, 2), flush=True)
