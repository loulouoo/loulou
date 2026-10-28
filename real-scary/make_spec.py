import json
# Same edit as the forest and abandoned videos: card, setup over a still, clip plays out, slowed/zoomed breakdown.
# Sources are the user's Reddit downloads; silent ones got a silent track, the fence clip was brightened.
CR = [0, 0.235, 1, 0.525]   # Ring clip: drop the black bars and the reposter's watermark
RA = [0, 0.205, 1, 0.58]    # ranch trail cam: drop the black bars, keep the date strip
stories = [
 dict(title="At The Window", src="leering", credit="r/blinkcameras", vo=10, still=4, play=[[0, 15.1]],
      ana=[[0, 15, 0.5], [3, 10, 0.5, [0.3, 0, 0.55, 0.75]]]),
 dict(title="Wandering", src="yard_stranger", credit="r/oddlyterrifying", vo=20, still=1, play=[[0, 12]],
      ana=[[0, 12, 0.5, [0.45, 0.1, 0.55, 0.65]], [0, 12, 0.7]]),
 dict(title="Behind The Fence", src="fence", credit="r/creepy", vo=30, still=10.5, play=[[0, 12.3]],
      ana=[[6, 12.3, 0.4], [0, 12.3, 0.7]], ana_vol=0.4),
 dict(title="Slithering", src="slither", credit="r/WTF", vo=40, still=10, play=[[0, 30]],
      ana=[[2, 26, 0.7, [0.07, 0.25, 0.45, 0.45]]]),
 dict(title="Private Land", src="ranch", credit="r/HighStrangeness", vo=50, still=5.5, crop=RA, play=[[0, 7.8]],
      ana=[[0, 7.8, 0.4, [0.5, 0.33, 0.5, 0.42]], [0, 7.8, 0.6, RA]]),
 dict(title="1:11 AM", src="knock1am", credit="r/Weird", vo=60, still=12, play=[[0, 38.5]],
      ana=[[0, 16, 0.6], [16, 38, 1, [0.2, 0.05, 0.6, 0.8]]]),
 dict(title="Check Your Camera", src="checkring", credit="via r/TerrifyingAsFuck", vo=70, still=13, crop=CR, play=[[3, 40]],
      ana=[[5, 18, 0.5, CR], [18, 28, 0.6, CR], [28, 36, 0.5, CR]], ana_vol=0.3),
]
S = []
for st in stories:
    c = "Video: " + st["credit"]; s = st["src"]
    S.append(dict(type="card", title=st["title"]))
    S.append(dict(type="intro", src=s, t=st["still"], vo=st["vo"], credit=c, crop=st.get("crop")))
    S.append(dict(type="play", src=s, parts=st["play"], credit=c, crop=st.get("crop")))
    S.append(dict(type="analysis", vo=st["vo"] + 1, credit=c, vol=st.get("ana_vol", 0.2),
                  parts=[[s] + p for p in st["ana"]]))
S.append(dict(type="analysis", vo=90, vol=0.1, parts=[["leering", 4, 9, 1], ["slither", 4, 14, 1],
                                                    ["checkring", 12, 20, 1, CR], ["ranch", 3, 7.8, 1, RA]]))
json.dump(dict(segments=S), open("spec.json", "w"), indent=1)
print(len(S))
