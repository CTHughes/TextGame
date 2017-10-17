from items import *

room_start = {
    "name": "dimly lit room",

    "description":
    """You are in the dank and dimly lit room where you
first awoke. The room contains two doors along with a
table and the chair you slept on. One of the doors is
green and the other is gold. Entering back into this
room makes you shiver, the atmosphere not helped by the
digital clock with a red display ominously ticking down
on the wall. You need to escape. And fast.""",

    "exits": {"table": "Table", "chair": "Chair"},

    "items": []
}

room_table = {
    "name": "the table",

    "description":
    """Out of place in the dimly lit room, the hardwood
table appeared high end and bespoke. On its surface
were 4 coloured sheets of paper with writing on them.
One was blue, one red, one yellow and one green.""",

    "exits": {"back": "Start"},

    "items": []
}

room_chair = {
    "name": "the chair",

    "description":
    """The chair that you were seated on when you were awoke is a plastic folding
chair. It looks so unbelievably uncomfortable that you find it hard to
imagine you managed to sleep on it without having first been drugged. It
looks light enough that it could easily be picked up if you should need to."""
},

    "exits": {"back": "Start"},

    "items": []

rooms = {
    "Start": room_start,
    "Table": room_table
    "Chair": room_chair
}
