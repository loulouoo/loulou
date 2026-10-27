import json, os
# Same edit as the forest and Ring videos: card, setup over a still, clip plays out, slowed/zoomed breakdown.
# Sources ending in _b are copies with swearing bleeped (see bleeps.json); fall back to the raw file otherwise.
def src(v):
    return v + "_b" if os.path.exists(f"raw/{v}_b.mp4") else v

stories = [
 dict(title="Fire Alarm", src="FbIZg6lRTpg", credit="Uncharted Expeditions", vo=10, still=90,
      play=[[18, 40], [160, 178], [792, 878]], ana=[[20, 36, 0.6], [805, 822, 0.6]], ana_vol=0.3),
 dict(title="Fast Footsteps", src="fLlkvDMBuqA", credit="weelass20", vo=20, still=51, play=[[0, 38]],
      ana=[[7, 14, 0.5], [21, 36, 0.7]], ana_vol=0.5),
 dict(title="Someone's Coming", src="_ugp0WUo4uw", credit="The Besties", vo=30, still=280,
      play=[[226, 250], [480, 505], [815, 878]], ana=[[480, 500, 0.6], [818, 842, 0.6]]),
 dict(title="It Was A Trap", src="D5tUHdUgAcI", credit="The Proper People", vo=40, still=50,
      play=[[118, 160], [355, 445], [478, 500]], ana=[[140, 158, 0.6], [366, 385, 0.6], [480, 492, 0.7]], ana_vol=0.3),
 dict(title="He Saw Me", src="o0TspPPzXf4", credit="Sam and Colby", vo=50, still=525,
      play=[[484, 556], [632, 722]], ana=[[486, 500, 0.6], [545, 556, 0.6], [636, 650, 0.6]]),
 dict(title="One Footstep", src="FKv5RXUPLhM", credit="Joe Weller", vo=60, still=520,
      play=[[134, 160], [538, 612], [668, 735]], ana=[[540, 560, 0.6], [668, 690, 0.6]], ana_vol=0.3),
 dict(title="Security", src="8JvlRtdsexE", credit="URBEX HILL", vo=70, still=280,
      play=[[528, 548], [668, 680], [740, 836]], ana=[[528, 548, 0.6], [756, 764, 0.5], [818, 831, 1]], ana_vol=0.35),
 dict(title="Bloody Murder", src="-pUPZVgmKCg", credit="Sam and Colby / Island Boys Productions", vo=80, still=450,
      play=[[662, 695], [820, 860], [876, 975]], ana=[[822, 840, 0.6], [878, 900, 1]], ana_vol=0.3),
]
S = []
for st in stories:
    c = "Video: " + st["credit"]; s = src(st["src"])
    S.append(dict(type="card", title=st["title"]))
    S.append(dict(type="intro", src=s, t=st["still"], vo=st["vo"], credit=c))
    S.append(dict(type="play", src=s, parts=st["play"], credit=c))
    S.append(dict(type="analysis", vo=st["vo"] + 1, credit=c, vol=st.get("ana_vol", 0.2),
                  parts=[[s] + p for p in st["ana"]]))
S.append(dict(type="analysis", vo=90, vol=0.1, parts=[[src("fLlkvDMBuqA"), 7, 14, 1], [src("D5tUHdUgAcI"), 370, 378, 1],
                                                    [src("-pUPZVgmKCg"), 880, 890, 1], [src("FKv5RXUPLhM"), 540, 548, 1]]))
json.dump(dict(segments=S), open("spec.json", "w"), indent=1)
print(len(S))
