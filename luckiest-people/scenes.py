import json

STYLE = (
    "Medium-skill MS Paint sketch: a crude hand-made doodle by someone with some drawing skill - amateur, funny, "
    "deliberately clumsy. Characters are simple cartoon stick-style people with round heads and simple bodies, eyes as "
    "plain dots or circles, and clear simple facial expressions. Thick uneven hand-drawn black outlines. Flat colour "
    "fills only (green, brown, grey, red, yellow, orange, blue). The whole frame is filled with NO empty white space: a "
    "simple flat-coloured background built from primitive shapes (sky, hills, forest, jungle, sea, rooms, streets) "
    "with a few simple background details, but no complex textures. Red arrows or red question marks for emphasis. "
    "NO shading, NO gradients, NO 3D, NO cinematic lighting. NOT a polished cartoon, NOT Disney or anime look, not "
    "vector art, not professional, no realistic people. Not gory, no blood, no wounds shown, no dead bodies. "
    "Uncluttered, subject centred with breathing room, nothing cropped. Wide horizontal 16:9 YouTube video still. Any "
    "text is short handwritten scrawl, correctly spelled and legible."
)

ANN = "Ann (a stick woman with curly brown hair and a pink dress)"
ROY = "Roy (a stick-man park ranger in a green uniform and a flat brown ranger hat)"
VIO = "Violet (a stick woman with dark hair in a bun, a white nurse cap and a blue dress)"
VES = "Vesna (a stick-woman flight attendant with short dark hair, a red uniform and a small red hat)"
JUL = "Juliane (a stick-figure teenage girl with a blonde ponytail and a yellow dress)"
TIT = "a big black and white ship with four yellow funnels"

P1 = [
    f"{ANN} asleep on a sofa while a glowing rock crashes through the roof above her, red arrow.",
    f"{ROY} getting zapped by a yellow lightning bolt with his hair standing up, a tally sign \"7\".",
    f"{VIO} standing in front of three ships drawn in a row, each with a red X.",
    f"{VES} falling through blue sky past clouds with surprised circle eyes, no parachute, a sign \"10 KM\".",
    f"{JUL} walking out of a green jungle with a determined face, a broken plane wing far behind in the trees.",
    "Five small stick-figure portraits on a wall labelled \"UNLUCKY?\" on one side and \"LUCKY?\" on the other.",
    "A stick man shrugging between a black cloud and a four-leaf clover, handwritten \"BOTH\".",
    "A countdown board with numbers 5, 4, 3, 2, 1 and a sign \"SURVIVED\".",
    "A big number \"1\" next to a cinema screen, a stack of books and a TV, all showing a jungle, red question mark.",
    "A big red start button being pressed by a cartoon finger, a sign \"LET'S START\".",
    "A giant number \"5\" on a sign in front of a small American house at sunset.",
    "A grey space rock with a fiery tail heading towards a small house, a sign \"METEORITE\".",
    "A small town street with wooden houses and a sign \"SYLACAUGA 1954\", a calendar \"30 NOV\".",
    f"{ANN} lying on a sofa under a blanket in a cosy living room, a radio and a lamp, sleepy face.",
    "A big \"BANG\" burst in the living room ceiling, dust flying.",
    "A grapefruit-sized grey rock smashing through a roof, roof tiles flying, a sign \"4 KG\".",
    f"The rock bouncing off a big wooden radio and hitting {ANN} on the hip, red dotted arrow showing its path.",
    f"{ANN} sitting up in pain in a dusty room with a big purple bruise on her side, circle eyes.",
    "A dotted line from outer space with stars and planets down to the little house.",
    "The grey rock on a table with a magnifying glass over it and a sign \"METEORITE\".",
    "A globe with many little rocks landing in the sea, a desert and empty fields, red arrows.",
    f"{ANN} pointing at herself with a gold medal labelled \"FIRST\", a meteorite next to her.",
    "A stick man scratching his head with a dice and a big \"?\".",
    "A huge globe with a tiny red target circle on one small house, a red arrow pointing at it.",
    "A stick man leaning in with wide circle eyes and a speech bubble \"WEIRDER\".",
    f"{ANN} on a newspaper front page with the headline \"HIT BY SPACE ROCK\".",
    "A crowd of stick-man reporters with cameras and notepads outside the little house.",
    "Two officials in suits carrying the meteorite away in a box labelled \"STUDY\".",
    f"A stern stick-woman landlady with a hat pointing at the meteorite, speech bubble \"MINE!\", {ANN} frowning.",
    f"{ANN} and the landlady arguing at a table, a calendar showing \"1 YEAR\", red question marks.",
    "A stick-man farmer in overalls and a straw hat finding a grey rock in a field, a mule behind.",
    "The farmer standing next to a shiny new car and a small house, holding money, big grin.",
    f"Split scene: on the left {ANN} with a bruise and sad face, on the right the farmer with a car and money, smiling.",
    "A stick man shrugging with a speech bubble \"LUCK!\", a four-leaf clover.",
    "A giant number \"4\" on a sign in front of a stormy sky.",
    f"{ROY} with seven lightning bolts drawn around him, a sign \"7 TIMES\".",
    f"{ROY} standing in front of a sign \"SHENANDOAH NATIONAL PARK\", green mountains behind.",
    "Green mountains, pine forests and a tall wooden lookout tower under a blue sky.",
    "Dark grey storm clouds over the mountains with yellow lightning bolts.",
    "A giant dice and a sign \"1 IN 15,000\", a stick man looking nervous.",
    f"{ROY} holding up seven fingers with a tired face, seven lightning bolts above.",
    f"{ROY} inside a wooden lookout tower being hit by lightning, a sign \"1942\".",
    f"{ROY} hopping on one foot holding his other bare foot, a little toenail flying off, funny face.",
    f"{ROY} driving a green truck on a mountain road, a sign \"1969\", dark clouds above.",
    f"{ROY} in the truck with lightning hitting it, his eyebrows gone, dizzy stars over his head.",
    f"{ROY} in his garden with flowers, a lightning bolt hitting his shoulder, a sign \"3\".",
    f"{ROY} with his hair on fire as a small cartoon flame, a lightning bolt, a sign \"4\".",
    f"{ROY} walking carrying a can of water, nervously watching the sky.",
    f"{ROY} driving a truck fast away from a dark storm cloud, a sign \"5\".",
    "A dark storm cloud with an angry face chasing a little green truck down a road.",
    f"{ROY} stepping out of his truck and getting zapped, hair on fire again, pouring water on his head.",
    f"{ROY} fishing in a rowing boat on a lake with a lightning bolt hitting near him, a sign \"1977\".",
    f"{ROY} standing proudly with a thumbs up and seven tiny lightning stickers on his shirt.",
    f"{ROY} holding a certificate labelled \"WORLD RECORD\", a gold star.",
    "Two burnt ranger hats with holes on display in a glass case in a museum, a sign \"MUSEUM\".",
    f"Stick people running away from {ROY} under a cloudy sky, him looking sad and alone.",
    "A stick man laughing with a speech bubble \"CAN YOU BLAME THEM?\", a red number \"3\" on a sign behind.",
    f"{VIO} standing on the deck of a big ocean liner with a waving smile, a sign \"1900s\".",
    f"{VIO} with a big red question mark over her head, a ship in the background.",
    f"A giant new ocean liner with four yellow funnels and a sign \"OLYMPIC 1911\", {VIO} waving from the deck.",
    "A big ocean liner bumping into a grey warship at sea with a \"CRUNCH\", red arrows.",
    "The damaged ocean liner sailing slowly back into a harbour with a dent in its side.",
    "Stick-figure passengers on the dock all smiling and safe, a green tick.",
    f"{VIO} carrying a suitcase up the gangplank of a new giant ship, a sign \"NEW JOB\".",
    f"{TIT}, very big, with a sign \"UNSINKABLE\".",
    f"{TIT} with its name \"TITANIC\" painted on the side, a red arrow.",
    f"{TIT} at night next to an iceberg, tilting, a sign \"1912\".",
    f"{VIO} on the ship deck at night calming worried stick-figure passengers in coats.",
    f"{VIO} in a small lifeboat being lowered down the side of the ship, someone handing her a baby in a blanket.",
    f"{VIO} in a lifeboat on a dark freezing sea hugging the baby, a rescue ship's lights on the horizon at dawn.",
    "A dark night sea with a few empty lifeboats and a sad grey sky, a sign \"1,500\".",
    f"{VIO} on the rescue ship wrapped in a blanket with a small relieved smile, a green tick.",
]

P2 = [
    f"A hospital ship with red crosses on its white side, a sign \"BRITANNIC\", {VIO} in a nurse cap on deck.",
    "The hospital ship hitting a sea mine with a big \"BOOM\" splash, a sign \"1916\".",
    f"{VIO} in a lifeboat being pulled towards huge spinning ship propellers, red arrows, scared face.",
    f"{VIO} underwater with bubbles, being pulled down near the bottom of a big ship, a red arrow pointing down.",
    f"{VIO} with a small bump and dizzy stars on her head giving a thumbs up, a sign \"FUNNY PART\".",
    f"{VIO} running back into a ship cabin while water rises, with a big red question mark.",
    f"{VIO} holding up a toothbrush triumphantly with a big grin, a speech bubble \"MY TOOTHBRUSH!\".",
    f"An old {VIO} with grey hair smiling next to a birthday cake \"83\", three small ships with red Xs behind her.",
    "A small passenger jet plane flying high above white clouds, a sign \"1972\", a giant number \"2\" in the corner.",
    f"A simple map with a dotted plane route from \"COPENHAGEN\" over \"CZECHOSLOVAKIA\", {VES} waving from a plane window, a sign \"AGE 22\".",
    f"{VES} looking at a flight list with a big red question mark, a speech bubble \"ME?\".",
    "Two flight attendants both with name tags reading \"VESNA\", a red arrow and a question mark between them.",
    "A plane high above a tall mountain labelled \"EVEREST\" breaking apart into pieces with a cartoon \"BOOM\" cloud, no people visible.",
    f"A tube-shaped piece of the plane drifting in the sky, {VES} inside it with wide circle eyes, a red arrow \"VESNA\".",
    f"The tube-shaped plane piece falling through clouds, {VES} held in place by a metal food trolley, red arrow down.",
    "The piece of plane landing on a snowy mountainside with pine trees, snow puffs flying, red arrows showing trees slowing it.",
    f"A stick man in a winter hat finding {VES} in the snowy wreck and waving for help.",
    f"{VES} in a hospital bed with bandages and a cast on her leg, a heart monitor with a beeping line, a sign \"COMA\".",
    f"{VES} with crutches taking her first steps in a hospital corridor, a nurse clapping.",
    f"{VES} holding a certificate labelled \"WORLD RECORD\", a measuring tape showing \"10,000 M\".",
    "Two stick-man investigators looking at a chart, one pointing at a lower height with a red question mark.",
    f"A tall measuring line from sky to ground with {VES} standing at the bottom, a big red \"WOW\", a reporter with a notepad.",
    f"{VES} looking sadly out of a window at the sky, a small grey cloud, handwritten \"NOT LUCKY\".",
    f"{VES} holding a candle with a calm sad face, a few stars in the sky.",
    "A giant number \"1\" on a sign in front of a dense green jungle.",
    f"{JUL} sitting in an airport waiting room with a small Christmas tree, a sign \"PERU 1971\".",
    f"{JUL} and her mother (a stick woman with a hat) sitting side by side in plane seats, a thought bubble of a man with glasses.",
    "A stick-man scientist with glasses at a wooden research hut in the jungle, a sign \"RESEARCH STATION\", a clock \"30 MIN\".",
    "A small plane flying into a huge dark thunderstorm, a lightning bolt hitting it, \"CRACK\".",
    f"{JUL} still strapped into a row of three plane seats, spinning in the open sky with wide circle eyes.",
    "A row of three blue airplane seats drifting down through a blue sky like a leaf, high above a green jungle with a winding river far below, a dotted red arrow pointing down and a sign \"3 KM\".",
    "View from above: round green treetops that look like broccoli heads, with a red arrow and handwritten \"BROCCOLI\".",
    f"{JUL} lying on the jungle floor, still in her seat row, waking up with dizzy stars, morning sun through the trees.",
    f"{JUL} with a sling on one arm and one eye swollen shut, without glasses, one bare foot, tiny and alone among giant jungle trees, a red question mark.",
    f"{JUL} with a sign \"ONLY SURVIVOR\" and a small candle, jungle behind.",
    f"{JUL} next to a sign \"1 OF 92\", thinking of the wooden research hut in a thought bubble.",
    f"{JUL} thinking with a light bulb over her head, a thought bubble of her dad in glasses pointing.",
    "A thought bubble showing the dad saying \"FIND WATER\", a stream in the jungle.",
    f"A simple map: a small stream joining a bigger river, then a little village with huts, red arrows, {JUL} pointing at a stream.",
    f"{JUL} wading knee-deep down a jungle stream, then floating, red arrows showing the direction, a calendar \"DAY 3\".",
    f"{JUL} walking in the stream looking hungry and tired, a snake on a branch and a flat stingray in the water.",
    f"{JUL} eating from a small bag of sweets, then finding a little boat and a wooden hut on a riverbank, a sign \"DAY 10\".",
    "Stick-man forest workers in hats arriving at the hut by boat, surprised to see the girl.",
    f"The workers stepping back with big circle eyes, a thought bubble of a ghost, {JUL} waving.",
    f"The workers giving {JUL} food and water and taking her away in a boat, a big calendar \"11 DAYS\".",
    f"{JUL} grown up, walking happily back into the green jungle with a backpack, a red arrow.",
    f"A grown-up {JUL} with glasses and a notebook in the jungle studying a butterfly, a sign \"BIOLOGIST\".",
    f"A grown-up {JUL} standing proudly in front of the wooden research hut, holding a small plant, a sign \"PROTECT\".",
    "A wall with three small pictures in a row: a meteorite hitting a house, a man hit by lightning, a ship, a stick man pointing.",
    "A wall with more pictures: a ship, a falling plane piece, a girl in a jungle, a stick man pointing.",
    "A stick man shrugging with a black rain cloud above him, a sign \"UNLUCKY?\".",
    "The same stick man smiling with a four-leaf clover and a rainbow, a sign \"LUCKY?\".",
    "A stick man standing behind a shield labelled \"SURVIVED\" as a storm rages around, a sign \"NOT ONLY LUCK\".",
    f"{VIO} in a lifeboat calmly holding a baby, a small red heart.",
]

P3 = [
    f"{JUL} with a light bulb above her head and a thought bubble of her dad, a stream behind her.",
    "A lightning bolt striking far away while a calm stick man holds an open book labelled \"KNOW\".",
    "A big red question mark between a four-leaf clover and a black cloud, a stick man thinking.",
    "A stick man presenter pointing at the viewer with a speech bubble \"COMMENTS?\".",
    "A stick man presenter next to a big crude red rounded button with white handwritten text \"SUBSCRIBE\".",
]

segs = json.load(open("segments.json"))
SCENES = [(p, ts, txt, s) for (p, ts, txt), s in zip(segs, P1 + P2 + P3)]
assert (len(P1), len(P2), len(P3)) == tuple(sum(1 for s in segs if s[0] == k) for k in (1, 2, 3)), (len(P1), len(P2), len(P3))
