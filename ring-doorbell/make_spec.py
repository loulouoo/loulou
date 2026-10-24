import json
NBC = [0.075, 0, 0.85, 0.85]  # drops NBC's lower-third banner
stories = [
 dict(title="The Window", src="2MqPJjTc1Bo", credit="Ring", vo=10, still=0.4, play=[[0, 14.7]],
      ana=[[0, 6, 0.5, [0.08, 0.4, 0.5, 0.5]], [6, 11.2, 0.5, [0.08, 0.4, 0.5, 0.5]], [11, 14.5, 0.4]]),
 dict(title="Cougar Country", src="aZjRfzSKCeU", credit="Ring", vo=20, still=0.5, play=[[0, 24]],
      ana=[[0, 6, 0.5, [0.45, 0, 0.5, 0.5]], [6, 15, 0.5], [15, 24, 0.5, [0.35, 0, 0.6, 0.6]]]),
 dict(title="Three Visitors", src="dXNmmCNK_fU", credit="Ring", vo=30, still=0.1, play=[[0, 24]],
      ana=[[0, 12, 0.5], [12, 24, 0.6, [0.4, 0.2, 0.6, 0.6]]]),
 dict(title="The Chicken Coop", src="H6_YpVBzqNw", credit="Ring", vo=40, still=0.5, play=[[0, 46.7]],
      ana=[[10, 22, 0.6], [25, 31, 0.4], [38, 46, 1]]),
 dict(title="Something in the Snow", src="VQaXxTrd88I", credit="Jensen Poore / TownLift", vo=50, still=0.5, play=[[0, 32.4]],
      ana=[[9, 20, 0.6, [0, 0.25, 0.6, 0.6]], [20, 27, 0.4], [27, 32, 0.6]]),
 dict(title="4:30 AM", src="xxdFMqHiGV4", credit="armando Jr", vo=60, still=0.3, play=[[0, 30]],
      ana=[[0, 5, 0.5, [0.1, 0.2, 0.6, 0.6]], [13, 18, 0.4, [0.1, 0.2, 0.6, 0.6]], [18, 30, 1]]),
 dict(title="They Have a Ring", src="Rl3I1rX5U6c", credit="Ring", vo=70, still=0.2, play=[[0, 16.4]],
      ana=[[0, 6, 0.5], [6, 12.5, 0.5], [12.5, 16.4, 0.4]]),
 dict(title="Somebody Help Me", src="ZgEa8I4hrL0", credit="Inside Edition", vo=80, still=1, play=[[0, 25.5], [48, 51.5], [55, 67.4]],
      ana=[[0, 10, 0.6], [10, 25, 0.6], [55, 64, 0.5]], ana_vol=0.12),
 dict(title="Open the Door", src="sYvEz8evrgU", credit="NBC News", vo=90, still=3, crop=NBC, play=[[0, 51.8], [59.5, 64.6], [74.8, 79]],
      ana=[[0, 14, 0.6, NBC], [28, 36, 0.5, NBC], [71, 74, 0.4, NBC], [59.5, 64.5, 0.6, NBC]], ana_vol=0.12),
]
S = []
for st in stories:
    c = "Video: " + st["credit"]; src = st["src"]
    S.append(dict(type="card", title=st["title"]))
    S.append(dict(type="intro", src=src, t=st["still"], vo=st["vo"], credit=c, crop=st.get("crop")))
    S.append(dict(type="play", src=src, parts=st["play"], credit=c, crop=st.get("crop")))
    S.append(dict(type="analysis", vo=st["vo"] + 1, credit=c, vol=st.get("ana_vol", 0.2),
                  parts=[[src] + p for p in st["ana"]]))
S.append(dict(type="analysis", vo=110, vol=0.1, parts=[["2MqPJjTc1Bo", 0, 8, 1], ["dXNmmCNK_fU", 2, 10, 1], ["sYvEz8evrgU", 70, 74, 1, NBC], ["H6_YpVBzqNw", 26, 31, 1]]))
json.dump(dict(segments=S), open("spec.json", "w"), indent=1)
print(len(S))
