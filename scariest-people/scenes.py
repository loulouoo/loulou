import json

STYLE = (
    "Medium-skill MS Paint sketch: a crude hand-made doodle by someone with some drawing skill - amateur, funny, "
    "deliberately clumsy. Characters are simple cartoon stick-style people with round heads and simple bodies, eyes as "
    "plain dots or circles, and clear simple facial expressions. Thick uneven hand-drawn black outlines. Flat colour "
    "fills only (green, brown, grey, red, yellow, orange, blue). The whole frame is filled with NO empty white space: a "
    "simple flat-coloured background built from primitive shapes (sky, hills, castles, palaces, rooms, streets, snow, steppe) "
    "with a few simple background details, but no complex textures. Red arrows or red question marks for emphasis. "
    "NO shading, NO gradients, NO 3D, NO cinematic lighting. NOT a polished cartoon, NOT Disney or anime look, not "
    "vector art, not professional, no realistic people. Not gory, NO blood, NO weapons or guns, NO dead bodies, NO violence shown, no flags or "
    "symbols of any regime. Uncluttered, subject centred with breathing room, nothing cropped. Wide horizontal 16:9 "
    "YouTube video still. Any text is short handwritten scrawl, correctly spelled and legible."
)

RAS = "Rasputin (a stick man with long black greasy hair, a big wild black beard, big staring circle eyes and a long black robe)"
TSAR = "Tsar Nicholas (a stick man with a neat brown beard, a red-and-white uniform and a small gold crown)"
TSARINA = "Tsarina Alexandra (a stick woman with brown hair in a bun, a long white dress and a small tiara)"
ALEX = "Alexei (a small stick boy in a white sailor suit)"
YUS = "Prince Yusupov (a thin stick man with slicked dark hair and a smart black suit)"
ELIZ = "Countess Elizabeth (a stick woman with a pale face, dark hair, a tall white ruff collar and a long dark red dress)"
IVAN = "Ivan (a stick man with a long pointed dark beard, a gold fur-trimmed crown and a long red robe, holding a tall wooden staff)"
OPR = "Oprichniki riders (stick men dressed all in black riding black horses)"
VLAD = "Vlad (a stick man with a long black moustache, long dark curly hair, a red hat with a gold brooch and a red cloak)"
SULTAN = "the sultan (a stick man with a big white turban, a short black beard and a green robe)"
GENG = "Genghis Khan (a stick man with a thin moustache, a small beard, a fur-trimmed pointed hat and a blue robe)"
TEM = "young Temujin (a small stick boy in a brown fur hat and brown tunic)"
MONG = "Mongol riders (stick men in fur hats riding small brown horses)"
PRES = "a stick-man presenter in a blue shirt"

P1 = [
    f"{RAS} standing next to a cake, a splash of icy river water and a big red question mark, with a sign \"WON'T DIE?\".",
    f"{ELIZ} peering sadly out of a tiny gap in a bricked-up castle window.",
    f"{IVAN} glaring, while small stick-man people hide behind a wall with scared faces and a sign \"WARNING!\".",
    f"{VLAD} standing calmly on a hill with arms folded while a huge crowd of tiny stick-man soldiers runs away in the distance.",
    f"{GENG} on a horse in front of a big map of Asia and Europe, behind him an empty town with no people and a red arrow.",
    f"{PRES} holding a sign \"REAL PEOPLE\" with a serious face.",
    "Two signs side by side: a green tick labelled \"TRUE\" and a cloud labelled \"LEGEND\", a stick man scratching his head between them.",
    "A countdown board with big numbers 5, 4, 3, 2, 1 and a sign \"SCARIEST PEOPLE\", a candle and a cobweb in the corner.",
    "A big red start button being pressed by a cartoon finger, a sign \"LET'S START\".",
    "A giant number \"5\" painted on a wooden sign in the snow.",
    f"{RAS} standing in the snow with a smug face and a sign \"THE MAN WHO WOULDN'T DIE\".",
    "A snowy Russian city with onion-domed churches, horse carriages and a sign \"RUSSIA 1900s\".",
    f"{TSAR} and {TSARINA} sitting on two gold thrones in a palace hall.",
    f"{TSAR} and {TSARINA} proudly holding hands with {ALEX}, a sign \"HEIR\" with a red arrow pointing at the boy.",
    f"{ALEX} with a worried face and a big padlock labelled \"SECRET\" floating above him.",
    f"A stick-man doctor holding a chart with a drawing of a drop and a sign \"HAEMOPHILIA\", {ALEX} sitting on a bed.",
    f"{ALEX} tripping over a toy, a worried {TSARINA} rushing towards him with her hands up.",
    f"A tall stranger in a long black robe walking through big palace gates in the snow, a red question mark.",
    f"{RAS} with a big name sign \"RASPUTIN\".",
    f"Close up of {RAS} with huge staring spiral eyes, little stick people backing away nervously.",
    f"{RAS} holding up his hands with a little gold halo drawn above his head and a sign \"HOLY MAN?\".",
    f"{RAS} sitting beside {ALEX} in bed, the boy smiling and feeling better, little hearts in the air.",
    f"{TSAR} and a stick-man doctor shrugging with big red question marks.",
    f"{RAS} gently patting the head of {ALEX}, who is calm and sleepy, a speech bubble \"SHHH\".",
    "A four-leaf clover and a dice rolling, a sign \"LUCK?\".",
    f"{TSARINA} kneeling and gazing up at {RAS}, who holds puppet strings attached to small crowns, palace room.",
    f"A group of grumpy stick-man nobles in fancy coats and top hats scowling and pointing at {RAS}.",
    f"{RAS} as a giant holding a tiny map of Russia, grumpy nobles shaking their fists below.",
    f"{YUS} and four stick-man nobles whispering around a table with a candle, a calendar page \"DEC 1916\".",
    f"{YUS} holding an open book labelled \"MY STORY\", a speech bubble with a cloud.",
    f"{RAS} sitting at a fancy table with pink cakes and a glass of red wine, a small green bottle labelled \"POISON\" next to them.",
    f"{RAS} munching a cake happily with crumbs in his beard, nobles behind him watching with shocked faces.",
    f"{YUS} jumping back in shock with a big \"BANG!\" scribble and smoke cloud, {RAS} falling over.",
    f"{RAS} sprawled on a red carpet with dizzy spiral eyes and little stars around his head, a candle on the table.",
    f"{RAS} suddenly sitting up with huge open eyes and grabbing the sleeve of {YUS}, who screams in fright.",
    "A rolled-up rug being tipped off a bridge into a frozen river with a hole in the ice, at night.",
    f"{PRES} with a twisty curly red arrow and a sign \"THE TWIST\".",
    f"{YUS} as an old man telling a story by a fireplace, a big speech bubble with a ghost drawn in it.",
    "A stick-man doctor in a white coat reading a clipboard labelled \"REPORT\", a crossed-out poison bottle, a red question mark.",
    f"A stick man holding a sign \"UNKILLABLE?\" with the word partly crossed out.",
    f"{RAS} as a spooky shadow behind a group of scared stick-man children by a campfire, a sign \"LEGEND\".",
    f"A giant number \"4\" on a sign next to {ELIZ}, a dark castle behind.",
    "A map with a crude shape labelled \"HUNGARY\" and a castle, a sign \"1500s\".",
    f"{ELIZ} sitting on a big chair surrounded by piles of gold coins and jewels.",
    f"{ELIZ} standing in front of a big map dotted with many small castles.",
    "A grey stone castle on top of a steep hill above a small village, a sign \"CACHTICE CASTLE\".",
    "Village stick people whispering to each other with speech bubbles full of red question marks.",
    f"A row of servant girl stick figures in aprons walking towards a dark castle gate, one empty spot in the line with a red question mark.",
    "Poor village stick people in patched clothes, a rich noble in a carriage driving past ignoring them.",
    "A stick-man noble father and mother in fancy clothes looking worried at an empty chair, a red question mark.",
    "A stick-man king with a crown pointing, sending two stick-man messengers on horses towards a castle, a sign \"1610\".",
    "A row of nervous stick-man witnesses standing in a court room, one pointing towards a castle drawn on a wall.",
    "A stick-man witness holding up a sign \"650?\" next to a closed old book with a lock.",
    "An empty open box with cobwebs and a red question mark, a sign \"DIARY?\".",
    "Two stick-man servants standing in front of a stern judge in a big wig, a wooden gavel on the desk.",
    f"{ELIZ} in her castle with her nose in the air, a sign \"NO TRIAL\".",
    f"Stick-man builders stacking bricks into a castle doorway while {ELIZ} watches from inside with a shocked face.",
    "A castle tower with all its windows bricked up except one tiny gap, a small tray of bread being passed through.",
    "A gravestone on a hill with the date \"1614\", a grey cloudy sky.",
    "An old book with a little stick figure drawn on it and a balloon labelled \"LEGEND\" growing bigger and bigger.",
    "A calendar with many pages flying away and a sign \"100 YEARS LATER\".",
    "A stick-man writer at a desk with a feather quill writing a book labelled \"STORIES\", a big red question mark.",
    f"A spooky book cover with {ELIZ} on it and the title \"BLOOD COUNTESS\".",
    "A stick-man judge holding a magnifying glass over an empty table with a sign \"NO EVIDENCE\".",
    f"A stick-man historian in glasses pointing at a board with a picture of {ELIZ} and a sign \"SET UP?\".",
    "A stick-man king with a crown holding an empty purse and an IOU note, next to a big pile of gold coins, a red arrow.",
    "A stick-man historian holding a big thick stack of papers labelled \"EVIDENCE\".",
    f"{ELIZ} at the top of a crude chart labelled \"MOST FEARED\", village people looking up nervously.",
    f"A giant number \"3\" on a sign next to {IVAN}.",
    "A teenage stick boy with a dark fringe being crowned with a big gold fur-trimmed crown, a sign \"1547\".",
    f"{IVAN} smiling on his throne with a green tick sign \"GOING WELL\".",
    f"{IVAN} holding a big book labelled \"LAWS\", rows of stick-man soldiers marching behind him.",
    "St Basil's Cathedral in Moscow drawn crudely with colourful onion domes in red, green, yellow and blue, little stick people admiring it.",
    "A small sad stick boy with a fringe sitting alone in a big empty palace hall.",
    "Two stick-man nobles in fur hats pulling at a gold throne in a tug of war while a small stick boy watches, scared.",
    "A teenage stick boy peeking suspiciously around a corner with narrow eyes, a red question mark.",
    f"{IVAN} crying beside a gravestone with a heart on it and the name \"ANASTASIA\", a sign \"1560\".",
    f"{IVAN} pointing angrily at a group of nervous stick-man nobles, a small green bottle labelled \"POISON\" with a red question mark.",
    f"{IVAN} with a cracked heart drawn above his head and wild angry eyes.",
    f"{OPR} lined up in a row, a sign \"OPRICHNIKI\".",
    f"{OPR} riding through the snow with a funny carved wooden dog-face badge and a broom tied to each saddle.",
    "A cartoon stick dog sniffing the ground with its nose next to a door, a sign \"TRAITORS?\".",
    "A big broom sweeping tiny stick-man nobles off a palace floor.",
    f"{OPR} carrying away bags of gold from a house while stick people peek out scared from windows.",
]

P2 = [
    f"{IVAN} pointing suspiciously at a crude walled city with onion domes and a sign \"NOVGOROD 1570\", a red question mark.",
    f"{OPR} riding towards a walled city in the snow with smoke rising, small stick people running away, a sign \"NOVGOROD\".",
    f"{IVAN} shouting at a younger stick man with a short beard in a palace room, both with furious faces and zig-zag anger lines, a sign \"1581\".",
    f"{IVAN} kneeling on the floor with his hands on his head in horror, his staff dropped on the floor beside him.",
    f"{IVAN} sitting alone and sad on his throne in a dark room, a grey rain cloud above his head.",
    "A painting in a gold frame on a museum wall showing a horrified bearded tsar hugging his son, stick-man visitors staring with wide eyes.",
    "A sign with \"GROZNY\" and an arrow pointing to two signs \"FEARSOME\" and \"FORMIDABLE\", a light bulb.",
    f"{IVAN} standing tall with a big sign above him \"IVAN THE TERRIBLE\".",
    "A giant number \"2\" on a sign, a bat flying past, green hills and a small castle behind, a sign \"WALLACHIA\".",
    f"{VLAD} standing proudly with a sign \"VLAD III\", and an older stick man with a crown next to him holding a little dragon badge.",
    "A big cartoon green dragon next to a sign \"DRACULA = SON OF THE DRAGON\".",
    f"A little stick boy version of {VLAD} sitting on a cart being taken towards a palace with domes, a sad face and a sign \"HOSTAGE\".",
    f"{VLAD} sitting on a throne with a very stern face and his arms folded, a sign \"PRINCE\".",
    f"{VLAD} pointing at a long list of rules nailed to a wall, scared stick-man townspeople backing away.",
    f"{VLAD} standing in front of a row of tall sharpened wooden poles stuck in the ground, a dark sky, a sign \"VLAD THE IMPALER\".",
    "A golden cup sitting on a stone fountain in a town square, a red arrow, townspeople walking past.",
    "A sneaky stick-man thief reaching towards the golden cup then running away scared, a red question mark.",
    f"{SULTAN} on a horse with a sign \"MEHMED II\" and a sign \"1462\".",
    f"A huge army of tiny stick-man soldiers in turbans marching over the hills, while {VLAD} and a much smaller group watch from a hilltop.",
    f"{VLAD} and a few stick-man soldiers sneaking towards a camp of tents at night under a big yellow moon.",
    f"{SULTAN} on a horse looking shocked at a hillside covered in hundreds of tall wooden poles, a dark sky.",
    "A huge field of tall wooden poles stretching to the horizon, crows flying, a sign \"20,000?\".",
    f"{SULTAN} turning his horse around with a horrified face, his army marching back the way they came.",
    "A stick-man writer with glasses and a quill writing a book labelled \"DRACULA 1897\".",
    f"A cartoon vampire with a cape and fangs crossed out with a red X, next to {VLAD} with a sign \"NOT A VAMPIRE\".",
    "A giant number \"1\" on a sign on a windswept green grassland with round white tents, a sign \"MONGOLIA\".",
    "A round white felt tent on a huge green grassland, a baby in a wooden cradle, a sign \"TEMUJIN\".",
    f"{TEM}, his mother and siblings standing alone on the grass while the rest of the tribe rides away.",
    f"{TEM} digging up roots and holding a small rabbit on a cold windy grassland, a determined face.",
    f"{GENG} shaking hands with other stick-man chiefs in fur hats, many little tents joining into one big camp.",
    f"{GENG} being lifted on a white felt blanket by cheering stick men, a sign \"1206\".",
    f"{GENG} on a horse pointing at a big crude world map, a red arrow sweeping across it.",
    "One Mongol stick-man rider in a fur hat with a line of five spare horses following behind, a sign \"FAST!\".",
    f"{MONG} galloping away while looking back over their shoulders with cheeky faces, surprised stick-man soldiers chasing them.",
    f"{MONG} suddenly turning their horses around towards surprised stick-man soldiers, a red curved arrow.",
    f"{GENG} holding up two signs: a white flag labelled \"SURRENDER\" with a green tick and a broken wall labelled \"FIGHT\" with a red X.",
    f"{GENG} pointing angrily at a stick-man ruler in a gold turban, two empty horses with no riders, a sign \"KHWARAZMIAN EMPIRE\".",
    "An empty city with blue domes and no people, broken walls, a sign \"SAMARKAND\".",
    "A big crude map with a huge blue area stretching from \"CHINA\" to \"EUROPE\", a red arrow.",
    "A stick-man historian standing next to a huge pile of question marks, a sign \"MILLIONS?\".",
    f"{GENG} with a thoughtful face between two signs \"DESTROYER\" and \"BUILDER\".",
    f"{GENG} holding a scroll with little drawings of different temples, a rider galloping with a letter, camels carrying goods on a road labelled \"SILK ROAD\".",
    "Rolling green hills with no marks, a big red question mark over one hill and a sign \"1227 WHERE?\".",
    "A line of Mongol stick-men riders walking slowly with heads bowed through empty hills at dusk, a sign \"SECRET\".",
    f"{PRES} standing next to two small framed pictures: {RAS} and {ELIZ}.",
    f"Three small framed pictures in a row: {IVAN}, {VLAD} and {GENG}.",
    f"{PRES} holding a sign \"THEY WERE REAL\" with a serious face.",
    "A huge balloon labelled \"LEGEND\" floating above a tiny box labelled \"TRUTH\", a stick man scratching his head.",
    f"{PRES} pointing at the viewer with a speech bubble \"SCARIEST?\".",
    f"{PRES} next to a big crude red rounded button with white handwritten text \"SUBSCRIBE\", a cinema poster \"HORROR FILM\" behind.",
]

segs = json.load(open("segments.json"))
SCENES = [(p, ts, txt, s) for (p, ts, txt), s in zip(segs, P1 + P2)]
assert (len(P1), len(P2)) == tuple(sum(1 for s in segs if s[0] == k) for k in (1, 2)), (len(P1), len(P2))
