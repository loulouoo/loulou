import json
# Same edit as the earlier videos: card, setup over a still, clip plays out, slowed/zoomed breakdown.
# raw/deck_boost is the deck clip with its faint background voice turned up.
# raw/bear and raw/hospital have swearing bleeped; raw/fig23 is brightened; silent clips got a silent track.
FIG = [0.3, 0.42, 0.26, 0.26]   # where the pale figure stands in the Ring clip
stories = [
 dict(title="4:30 AM", src="kc430", credit="r/kansascity", vo=10, still=7, play=[[0, 15.3]],
      ana=[[4, 10.5, 0.5], [5.5, 9.5, 0.5, [0.15, 0.05, 0.65, 0.8]]]),
 dict(title="Along The Fence", src="fence_run", credit="r/Ghosts", vo=20, still=3.6, play=[[0, 5.1]],
      ana=[[2.5, 5, 0.25], [3, 4.6, 0.2, [0.25, 0.45, 0.6, 0.45]]], ana_vol=0),
 dict(title="No Shoes", src="oldman", credit="Bridie Steinfort", vo=30, still=14, play=[[0, 45.7]],
      ana=[[12, 26, 0.6], [16, 24, 0.6, [0, 0.25, 1, 0.5]]]),
 dict(title="Between 2 And 3 AM", src="fig23", credit="r/Unexplained", vo=40, still=40, play=[[24, 62.5]],
      ana=[[28, 44, 0.6, FIG], [44, 62, 1, FIG]], ana_vol=0),
 dict(title="On The Deck", src="bear", credit="TikTok", vo=50, still=4, play=[[0, 30]],
      ana=[[0, 13, 0.8], [0, 13, 0.8, [0.35, 0.1, 0.5, 0.7]]], ana_vol=0.15,
      listen=dict(src="deck_boost", parts=[[0, 13.5]], caps=[["TURN YOUR VOLUME UP", 0, 13.5]])),
 dict(title="The Doorway", src="ghostface", credit="Sandboxen", vo=60, still=4, play=[[0, 102.5]],
      ana=[[50, 62, 0.6], [76, 92, 0.7]], ana_vol=0.15),
 dict(title="Shadow People", src="hospital", credit="amylouuuu20", vo=70, still=4, play=[[0, 57.3]],
      ana=[[2, 12, 0.6], [30, 46, 0.6], [30, 46, 0.6, [0.1, 0.2, 0.8, 0.5]]], ana_vol=0.25),
]
S = []
for st in stories:
    c = "Video: " + st["credit"]; s = st["src"]
    S.append(dict(type="card", title=st["title"]))
    S.append(dict(type="intro", src=s, t=st["still"], vo=st["vo"], credit=c, crop=st.get("crop")))
    S.append(dict(type="play", src=s, parts=st["play"], credit=c, crop=st.get("crop")))
    S.append(dict(type="analysis", vo=st["vo"] + 1, credit=c, vol=st.get("ana_vol", 0.2),
                  parts=[[s] + p for p in st["ana"]]))
    if "listen" in st:   # extra replay with the faint background voice boosted
        L = st["listen"]
        S.append(dict(type="play", src=L["src"], parts=L["parts"], credit=c, caps=L["caps"]))
S.append(dict(type="analysis", vo=90, vol=0.1, parts=[["kc430", 6, 9.5, 1], ["bear", 12, 18, 1], ["hospital", 32, 40, 1]]))
json.dump(dict(segments=S), open("spec.json", "w"), indent=1)
print(len(S))
