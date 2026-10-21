import json
TC,KN,FY,YI,OL,QL,AZ,JR,SU,RB="Eqh1yhsPYrc","Z-uGHXkdXH0","7QDVgByGi5Y","MmLAgUyW2us","i93_pLRydJo","aMr-ZjRtV-A","l-FSJ-4LPI4","0_85snQmX28","j_o2oAjCCOw","ClPZINVp0y8"
KNE={"eq":"eq=brightness=0.18:contrast=1.5:gamma=2"}
QLE={"eq":"eq=brightness=0.1:contrast=1.4:gamma=1.5"}
FYC={"crop":[0,0.02,0.8,0.76]}
RED="0xE01414"
c=lambda n:"Video: "+n
S=[
 dict(vo=10,num=10,title="THE THING IN THE FERNS",vol=0.1,credit=c("TrailCamsNorthwest"),parts=[[TC,4,16,1]]),
 dict(vo=11,vol=0.1,credit=c("TrailCamsNorthwest"),parts=[[TC,4,16,0.6,{"crop":[0.1,0.2,0.6,0.6]}]],circle=[0.45,0.52,0.17,0.3,1,19]),
 dict(vo=12,vol=0.1,credit=c("TrailCamsNorthwest"),parts=[[TC,40,58,1]]),
 dict(vo=20,num=9,title="3 AM KNOCKING",vol=0,credit=c("Someone keeps knocking at my door."),parts=[[KN,5,13,1,KNE]]),
 dict(vol=1.3,credit=c("Someone keeps knocking at my door."),parts=[[KN,0,41.7,1,KNE]],caps=[["LISTEN...",0.3,5,100,RED,880]]),
 dict(vo=22,vol=0.25,credit=c("Someone keeps knocking at my door."),parts=[[KN,9,34,1,KNE]]),
 dict(vo=30,num=8,title="THE FAIRY",vol=0,credit=c("CTV News / Steve McBeth"),parts=[[FY,58.6,63.5,0.4,FYC]]),
 dict(vo=31,vol=0,credit=c("CTV News / Steve McBeth"),parts=[[FY,62.5,70,0.5,FYC]],circle=[0.62,0.42,0.2,0.32,1,15]),
 dict(vo=32,vol=0,credit=c("CTV News / Steve McBeth"),parts=[[FY,58.6,70,1,FYC],[FY,62.5,70,0.4,FYC]]),
 dict(vo=40,num=7,title="THE ORB",vol=0.1,credit=c("LifeHackster"),parts=[[YI,43,55,1]]),
 dict(vo=41,vol=0.1,credit=c("LifeHackster"),parts=[[YI,54,58.5,0.5]]),
 dict(vo=42,vol=0.1,credit=c("LifeHackster"),parts=[[YI,54,58.5,1],[YI,64,96,1]],circle=[0.11,0.4,0.09,0.17,9,24]),
 dict(vo=50,num=6,title="THE WOMAN IN THE FOG",vol=0.1,credit=c("Fynsk Dashcam"),parts=[[OL,0,13,1]]),
 dict(vo=51,vol=0.1,credit=c("Fynsk Dashcam"),parts=[[OL,12,17,0.5,{"crop":[0.25,0.25,0.5,0.5]}]],circle=[0.56,0.62,0.08,0.18,1,10]),
 dict(vo=52,vol=0.1,credit=c("Fynsk Dashcam"),parts=[[OL,13,34,1]]),
 dict(vo=60,num=5,title="THE MAN IN THE LANE",vol=0.1,credit=c("Quarter Life Crisis"),parts=[[QL,4,18,1,QLE]]),
 dict(vo=61,vol=0.1,credit=c("Quarter Life Crisis"),parts=[[QL,24,38,1,QLE]],circle=[0.91,0.78,0.08,0.17,7,13]),
 dict(vo=62,vol=0.1,credit=c("Quarter Life Crisis"),parts=[[QL,29,38,0.5,{"crop":[0.45,0.35,0.55,0.55],**QLE}]],circle=[0.84,0.76,0.13,0.22,4,16]),
 dict(vo=70,num=4,title="GHOST OR GLARE?",vol=0,credit=c("FOX 10 Phoenix / Will Church & Erika Lake"),parts=[[AZ,0,12,1]]),
 dict(vo=71,vol=0,credit=c("FOX 10 Phoenix / Will Church & Erika Lake"),parts=[[AZ,1,5,0.4,{"crop":[0.4,0.3,0.45,0.45]}]],circle=[0.51,0.5,0.09,0.2,1,10]),
 dict(vo=72,vol=0,credit=c("FOX 10 Phoenix / Will Church & Erika Lake"),parts=[[AZ,5,34.5,1]],caps=[["GHOST OR GLARE?",24,32,90,RED,880]]),
 dict(vo=80,num=3,title="THE MASK",vol=0.15,credit=c("JoeRobTV"),parts=[[JR,0,30,1]]),
 dict(vo=81,vol=0.15,credit=c("JoeRobTV"),parts=[[JR,55,72,1]]),
 dict(vo=82,vol=0.15,credit=c("JoeRobTV"),parts=[[JR,66,90.4,1]]),
 dict(vo=90,num=2,title="THE MEN IN SUITS",vol=0.15,credit=c("Billy Boy"),parts=[[SU,0,8,1]]),
 dict(vo=91,vol=0.15,credit=c("Billy Boy"),parts=[[SU,8,14,0.5]]),
 dict(vo=92,vol=0.15,credit=c("Billy Boy"),parts=[[SU,13,25,1],[SU,8,25,0.6]],caps=[["WHO WERE THEY?",30,40,90,RED,880]]),
 dict(vo=100,num=1,title="THE ROADBLOCK",vol=0.08,credit=c("Ivan Tukhtin"),parts=[[RB,5,20,1]]),
 dict(vo=101,vol=0,credit=c("Ivan Tukhtin"),parts=[[RB,18,30,0.5]]),
 dict(vo=102,vol=0.45,credit=c("Ivan Tukhtin"),parts=[[RB,26,45,1],[RB,28,34,0.4]],circle=[0.87,0.6,0.07,0.17,2.5,8]),
 dict(vo=110,vol=0.1,parts=[[SU,13,20,1],[JR,74,80,1],[RB,28,34,1],[AZ,1,6,1]],caps=[["SUBSCRIBE",14,40,120,RED,880]]),
]
json.dump(S,open("spec.json","w"))
print(len(S))
