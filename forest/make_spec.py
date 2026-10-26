import json
# Same edit as the Ring video: card, setup over a still, clip plays out, slowed/zoomed breakdown.
stories = [
 dict(title="Walking Backwards", src="8d5vENjxCyg", credit="Jeffrey Glassner / Inside Edition", vo=10, still=2, play=[[0, 97]],
      ana=[[0, 12, 0.6], [50, 58, 0.5], [88, 97, 0.6]]),
 dict(title="Time To Go", src="GdHLtbo80dk", credit="Tomorrowsgarden", vo=20, still=1, play=[[0, 74.2]],
      ana=[[52, 74, 0.6], [56, 68, 1]], ana_vol=0.5),
 dict(title="Consolation Lakes", src="K8Qf4QcYy48", credit="CBC News / Phoebe Nicholson", vo=30, still=41.9, play=[[0, 82]],
      ana=[[40, 47, 0.5], [55, 63, 0.5], [30, 34, 0.6]]),
 dict(title="Vermilion River", src="GY73ffSq4uU", credit="APTN News", vo=40, still=5, play=[[0, 45.3]],
      ana=[[0, 45, 1]], ana_vol=0.4),
 dict(title="Get Off The Trail", src="7g9aEaESfL0", credit="Dulé Krivdich / KRTV News", vo=50, still=6, play=[[0, 45.7]],
      ana=[[0, 15, 0.6, [0.2, 0.2, 0.6, 0.6]], [20, 32, 0.6]], ana_vol=0.35),
 dict(title="A Strange Noise", src="stISzPngwh4", credit="Stargell Blackstar", vo=60, still=10, play=[[0, 70]],
      ana=[[30, 66, 1]], ana_vol=0.4),
 dict(title="Nowhere To Go", src="ICVpIUeD6gY", credit="@laurago1d via Storyful / FOX 11", vo=70, still=2, play=[[0, 99]],
      ana=[[0, 6, 0.5, [0.3, 0.05, 0.4, 0.6]], [26, 40, 0.6], [70, 80, 0.6]]),
 dict(title="Seven Calls", src="vjsuy8TsgjE", credit="The Facts By Howtohunt.com", vo=80, still=12, play=[[7, 62]],
      ana=[[8, 62, 0.6]], ana_vol=0.45),
 dict(title="Stalked", src="d4FbHzeCJjM", credit="Chris / Sophia Zhang", vo=90, still=30, play=[[18, 45], [125, 292]],
      ana=[[205, 225, 0.5], [240, 262, 0.6], [128, 140, 0.6, [0.2, 0.1, 0.6, 0.6]]]),
 dict(title="Six Minutes", src="9Pg2c", credit="Kyle Burgess (@kunkyle)", vo=100, still=20, play=[[0, 160], [322, 360]],
      ana=[[45, 60, 0.5], [95, 110, 0.6], [330, 350, 0.6]], ana_vol=0.15),
]
S = []
for st in stories:
    c = "Video: " + st["credit"]; src = st["src"]
    S.append(dict(type="card", title=st["title"]))
    S.append(dict(type="intro", src=src, t=st["still"], vo=st["vo"], credit=c, crop=st.get("crop")))
    S.append(dict(type="play", src=src, parts=st["play"], credit=c, crop=st.get("crop")))
    S.append(dict(type="analysis", vo=st["vo"] + 1, credit=c, vol=st.get("ana_vol", 0.2),
                  parts=[[src] + p for p in st["ana"]]))
S.append(dict(type="analysis", vo=110, vol=0.1, parts=[["K8Qf4QcYy48", 40, 47, 1], ["8d5vENjxCyg", 10, 18, 1], ["d4FbHzeCJjM", 240, 250, 1], ["9Pg2c", 48, 58, 1]]))
json.dump(dict(segments=S), open("spec.json", "w"), indent=1)
print(len(S))
