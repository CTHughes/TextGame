from items import *

room_start = {
    "name": "dimly lit room",

    "description":
    """You are in the dank and dimly lit room where you
first awoke. The only light is cast from a daunting red
display on the wall. The room contains two doors along with a
table and the chair you slept on. One of the doors is
green and the other is gold. Entering back into this
room makes you shiver. You take another look at the display
with its red lights gleaming at you worsening the atmosphere.

You need to escape. Fast.""",

    "exits": {"table": "Table", "chair": "Chair", "clock" : "Clock", "greendoor": "Green Door"},

    "items": []
}

room_table = {
    "name": "the table",

    "description":
    """Out of place in the dimly lit room, the hardwood
table appears up-market and bespoke. On its surface
is a single sheet of paper.""",

    "exits": {"back": "Start"},

    "items": []
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
    """This tall towering door looms down on you with hopes of escape or truth. As you glance at
    it you cannot help but feel frustrated that it is not a fire exit, why can't you just leave
    already? 

    It seems it requires a username and password to escape.""",

    "exits": {"back": "Start"},

    "items": []
}

room_green_door = {
    "name": "the green door",

    "description":
    """The green door seems like it belongs in this dimly lit room, its wood seems aged, yet 
    you are well aware you wouldn't be able to break it down. Curiosity leaves you craving 
    to know what awaits you on the other side.

    It appears the only way through is to use a key.'""",

    "exits": {"back": "Start"},

    "items": []
}

room_clock = {
    "name": "the clock",

    "description":
    """The red display of this clock is very ominous. It's decreasing value seems to only
    mean impending doom.""",

    "exits": {"back": "Start"},

    "items": []
}

room_keypad = {
    "name": "the keypad",

    "description": "A display awaiting 4 characters input, and a flashing keyboard.",

    "exits": {"back": "Start"},

    "items": []
}
rooms = {
    "Start": room_start,
    "Table": room_table,
    "Chair": room_chair,
    "Gold Door": room_gold_door,
    "Green Door": room_green_door,
    "Clock": room_clock,
    "Keypad": room_keypad
}
