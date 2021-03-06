from items import *

room_start = {
    "name": "dimly lit room",

    "description":
    """You are in a dank and dimly lit room where you can still make out a
patch of drool on a chair from when you were sleeping. The only light
is cast from a daunting red display on the wall. The room contains two doors 
along  with a table and the chair you slept on. One of the doors is green 
and the other is gold.  You take another look at the display with its red
lights gleaming at you worsening the atmosphere.

You need to escape. Fast.""",

    "exits": {"table": "Table", "chair": "Chair", "clock" : "Clock", "greendoor": "Green Door", "golddoor": "Gold Door"},

    "items": []
}

room_table = {
    "name": "the table",

    "description":
    """Out of place in the dimly lit room, the hardwood table appears up-market and 
bespoke. There is some sort of white smudge against the brown surface of the table. Maybe if you could see better you would know what it was.""",

    "exits": {"back": "Start"},

    "items": [item_paper]
}

room_chair = {
    "name": "the chair",

    "description":
    """The chair that you were seated on when you were awoke is a plastic folding
chair. It looks so unbelievably uncomfortable that you find it hard to
imagine you managed to sleep on it without having first been drugged. It
looks light enough that it could easily be picked up if you should need to.""",
    
    "exits": {"back": "Start"},

    "items": []
}

room_gold_door = {
    "name": "the gold door",

    "description":
    """This tall towering door looms down on you with hopes of escape or truth.
As you glance at it you cannot help but feel frustrated that it is not a fire 
exit, why can't you just leave already? 

It seems it requires a key and a password to escape.""",

    "exits": {"back": "Start"},

    "items": []
}

room_green_door = {
    "name": "the green door",

    "description":
    """The green door seems like it belongs in this dimly lit room, its wood seems 
aged, yet you are well aware you wouldn't be able to break it down. Curiosity 
leaves you craving to know what awaits you on the other side.

It appears the only way through is to use a key.""",

    "exits": {"back": "Start"},

    "items": []
}

room_clock = {
    "name": "the clock",

    "description":
    """The red display of this clock is very ominous. It's decreasing value seems to
only mean impending doom.""",

    "exits": {"back": "Start"},

    "items": []
}

room_keypad = {
    "name": "the keypad",

    "description": "A display awaiting a 4 digit input, and a flashing keyboard.",

    "exits": {"back": "Start"},

    "items": []
}
room_second_keypad = {
    "name": "the keypad",

    "description": "A display awaiting a 4 digit input, and a flashing keyboard.",

    "exits": {"back": "Second Room"},

    "items": []
}
room_third_keypad = {
    "name": "the keypad",

    "description": "A display with a full keyboard. It appears to be waiting for a password.",

    "exits": {"back": "Start"},

    "items": []
}
room_red_door = {
    "name": "the red door",

    "description": """This door seems different to the rest you have encountered. It has a red colour and is smaller in all proportions,
if you were taller, you would probably have to duck. There is a slot for a key.""",

    "exits": {"back": "Second Room"},

    "items": []
}
room_piano = {
    "name": "the piano",

    "description": """A grand Piano is awkwardly pressed against the wall. It doesn't seem to fit with the dark 
room - how would anyone read sheet music in that light? Maybe you could move it into the light and play something.""",

    "exits": {"back": "Second Room"},

    "items": []
}
room_metal_box = {
    "name": "a metal box",

    "description": """The cold, hard metal seems to solidify your helpless situation - how can you escape? 
You focus your attention solely on the box observering a grate covering it from your hands, and inside there seems to be a key attached to a floatation device. 
Is there a way to retrieve the key?""",

    "exits": {"back": "Second Room"},

    "items": []
}
room_second = {
    "name": "the second room",

    "description": """You are in a dark vast room, the high ceiling towers at a
staggering height above you. There is a piano, a painting on the wall and a red door across from you - it's
gleaming red crimson clearly capturing your attention. Whoever owns this
place really has a thing for coloured doors. Yet, in the centre of the room you
observe a dark metal box, completely void of colour, but filled with a sense
of mystery.""",

    "exits": {"back": "Start", "greendoor": "Start", "reddoor": "Red Door", "piano": "Piano", "box": "Metal Box"},

    "items": [item_bottle, item_painting]
}
room_safe = {
    "name": "the safe",

    "description": "The safe is closed and has a keypad with the numbers one to nine.",

    "exits": {"back": "Second Room"},

    "items": []
}
room_mirrors = {
    "name": "the mirror room",

    "description": """You are in a blindingly bright room, or at least that is how it
feels after the previous two dark prisons. Your eyes take a few minutes to adjust
but when they do; you see a large mirror hung on the back wall. You remember the clock back in 
the first room - there can't be that much time left to escape. Perhaps you should reflect on how?""",

    "exits": {"back": "Second Room", "reddoor": "Second Room", "mirror": "Mirror"},

    "items": [item_goldkey]
}
room_mirror = {
    "name": "the mirror",

    "description": """You look into the mirror, your brown eyes gaze back to you and 
realisation dawns over you. You are Kirill Sidorov.""",

    "exits": {"back": "Mirror Room"},

    "items": []
}
rooms = {
    "Start": room_start,
    "Table": room_table,
    "Chair": room_chair,
    "Gold Door": room_gold_door,
    "Green Door": room_green_door,
    "Clock": room_clock,
    "Keypad": room_keypad,
    "Second Keypad": room_second_keypad,
    "Third Keypad": room_third_keypad,
    "Piano": room_piano,
    "Metal Box": room_metal_box,
    "Second Room": room_second,
    "Red Door": room_red_door,
    "Safe": room_safe,
    "Mirror Room": room_mirrors,
    "Mirror": room_mirror
}