#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
import time

glasses_taken = False

def list_of_items(items):
    #This function takes a list of items (see items.py for the definition) and
    #returns a comma-separated list of item names (as a string).

    names = [li["name"] for li in items]
    return ", ".join(names)

def print_room_items(room):
    #This function takes a room as an input and nicely displays a list of items
    #found in this room.
    
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print()

def print_inventory_items(items):
    #This function takes a list of inventory items and displays it nicely, in a
    #manner similar to print_room_items().

    if items:
        print("You have " + list_of_items(items) + ".")
        print()

def print_room(room):
    #This function takes a room as an input and nicely displays its name
    #and description.
    import textwrap

    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    dedented_text = textwrap.dedent(room["description"]).strip()
    print(textwrap.fill(dedented_text, 70))
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    #This function takes a dictionary of exits and a direction and
    #returns the name of the room into which this exit leads.

    return rooms[exits[direction]]["name"]

def is_valid_exit(exits, chosen_exit):
    #This function checks whether the player has chosen a valid exit.

    return chosen_exit in exits

def execute_go(direction, extension = ""):
    #This function, given the direction updates the current room
    #to reflect the movement of the player if the direction is a valid exit.

    global current_room

    if is_valid_exit(current_room["exits"], direction + extension):
        current_room = rooms[current_room["exits"][direction + extension]]
    else:
        print("You cannot go there.")

def execute_inspect(article, extension = ""):
    #This function allows a part of the environment to be examined
    
    global inventory
    global current_room
    global glasses_taken

    article_inspected = False
    if is_valid_exit(current_room["exits"], article + extension):
        current_room = rooms[current_room["exits"][article + extension]]
        article_inspected = True
    else:
        for item in current_room["items"]:
            if item["id"] == article:
                print(item["description"])
                article_inspected = True
        for item in inventory:
            if item["id"] == article:
                print(item["description"])
                article_inspected = True

    if glasses_taken == True and article == "pocket":
        print("Your pockets are empty.")
        article_inspected = True

    if glasses_taken == False and article == "pocket":
        print("You find a pair of glasses in your pocket.")
        inventory.append(item_glasses)
        article_inspected = True
        glasses_taken = True


    elif article_inspected == False:
        print("You cannot inspect that.")
        
def execute_take(item_id):
    #This function takes an item_id as an argument and moves this item from the
    #list of items in the current room to the player's inventory. 

    global inventory
    global current_room

    item_taken = False
    for item in current_room["items"]:
        if item["id"] == item_id:
                inventory.append(item)
                current_room["items"].remove(item)
                item_taken = True

    if item_id == "painting" and current_room == rooms["Second Room"]:
        rooms["Second Room"]["description"] = """You are in a dark vast room, the high ceiling towers at a staggering height above you. Through the dingey light you
can make out and piano in the corner, a safe revealed by taking down the painting and a new door across from you - it's
gleaming red crimson clearly capturing your attention. Whoever owns this place really has a thing for coloured doors.Yet, in the middle of the room you
observe a dark metal box, completely void of colour, but filled with a sense of mystery."""
        rooms["Second Room"]["exits"].update({"safe" : "Safe"})
    if item_taken == False:
        print("You cannot take that.")
    

def execute_drop(item_id):
    #This function takes an item_id as an argument and moves this item from the
    #player's inventory to list of items in the current room.
    
    global inventory
    global current_room

    item_dropped = False
    for item in inventory:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
            item_dropped = True

    if item_dropped == False:
        print("You cannot drop that.")

def execute_help():
    print('Possible actions:')
    print('-----------------------------------------')
    print('INSPECT or EXAMINE to examine an object')
    print('MOVE or PUSH to move certain objects')
    print('TAKE to pick up an item')
    print('DROP to drop an item')
    print('GO to move.')
    print('If you are inspecting an object, type \'GO back\' to go back to the main room.')
    print('CHECK TIME to check time.')
    print('USE to use certain items')
    print('WEAR to wear certain items')
    print('PLAY to play a series of notes on the piano')
    print('EMPTY or POUR certain items')
    print('PICK to check under certain objects')

def specific_command(command, article, extension = ""):
    #This function is for running the hard-coded room commands which produce a specific result
    global current_room
        
    if item_glasses in inventory and command == "wear" and article == "glasses":
        print("You put on your glasses, everything becomes much clearer now.")
        inventory.remove(item_glasses)
        rooms["Table"]["description"] = """Out of place in the dimly lit room, the hardwood table appears up-market and 
bespoke. On its surface is a single sheet of paper. There is also a post-it note with the numbers 3748."""
    elif current_room == rooms["Chair"] and command == "pick" and article == "chair":
        if current_room["description"] != "The chair lies on the floor where you left it.":
            print("When you pick up the chair a green key clatters to the floor.")
            current_room["items"].append(item_greenkey)
            current_room["description"] = "The chair lies on the floor where you left it."
    elif current_room == rooms["Green Door"] and command == "use" and article + extension == "greenkey":
        inventory.remove(item_greenkey)
        print("As you unlock the green door with the green key, a keypad opens.")
        current_room = rooms["Keypad"]
        rooms["Start"]["exits"]["greendoor"] = "Keypad"
    elif current_room == rooms["Keypad"] and (command == "enter" or command == "type") and article == "3748":
        print("As you enter the code into the keypad, the door opens and step into another room.")
        current_room = rooms["Second Room"]
        rooms["Start"]["exits"]["greendoor"] = "Second Room"
    elif current_room == rooms["Clock"] and command == "check" and article == "time":

        minutes = time.clock() / 60
        seconds = time.clock() % 60
        if 30 - minutes >= 0:
            minutes = int(30 - minutes)
            seconds = int(60 - seconds)
            print(("%02d" % (minutes,)) + ":" + ("%02d" % (seconds,)) + " is what can be read on the clock.")
    
    elif current_room == rooms["Piano"] and (command == "push" or command == "move") and article == "piano":
        if current_room["description"] == """A grand Piano is awkwardly pressed against the wall. It doesn't seem to fit with the dark 
room - how would anyone read sheet music in that light? Yet, it seems to draw you in.""" or current_room["description"] == """The grand Piano has the top open, who would have known it was set up to open
after a certain input.""":
            print("The piano is pushed to one side and behind it you find a water bottle.")
            current_room["items"].append(item_bottle)
            current_room["description"] = """A grand Piano off to one side where you pushed it. It doesn't seem to fit with the dark 
room - how would anyone read sheet music in that light? Yet, it seems to draw you in."""
    elif current_room == rooms["Piano"] and command == "play" and article == "cab":
        if current_room["description"] == """A grand Piano is awkwardly pressed against the wall. It doesn't seem to fit with the dark 
room - how would anyone read sheet music in that light? Yet, it seems to draw you in.""" or current_room["description"] == """A grand Piano off to one side where you pushed it. It doesn't seem to fit with the dark 
room - how would anyone read sheet music in that light? Yet, it seems to draw you in.""":
            print("The top of the piano mechanically opens to reveal a red note.")
            current_room["items"].append(item_note)
            current_room["description"] = """The grand Piano has the top open, who would have known it was set up to open
after a certain input."""
    elif current_room == rooms["Metal Box"] and (command == "empty" or command == "pour") and (article == "bottle" or article == "waterbottle" or article == "water") and extension == "box":
        for item in inventory:
            if item["id"] == "bottle":
                if current_room["description"]=="""The cold, hard metal seems to solidify your helpless situation - how can you escape? 
You focus your attention solely on the box observering a grate covering it from your hands, and inside there seems to be a key attached to an arm band. 
Is there a way to retrieve the key?""":
                    print("You empty a bottle into the grate, it looks to be about a third full.")
                    current_room["description"] = "The box looks to be about 1/3 full of water. Perhaps you could fill it the whole way with more water."
                    inventory.remove(item)
                elif current_room["description"]=="The box looks to be about 1/3 full of water. Perhaps you could fill it the whole way with more water.":
                    print("You empty a bottle into the grate, it looks to be about two thirds full.")
                    current_room["description"] = "The box looks to be about 2/3 full of water. Perhaps you could fill it the whole way with more water."
                    inventory.remove(item)
                elif current_room["description"]=="The box looks to be about 2/3 full of water. Perhaps you could fill it the whole way with more water.":
                    print("You empty a bottle into the grate, it looks to be full, there is a key sticking out of the grate.")
                    current_room["description"] = "The box is full of water."
                    inventory.remove(item)
                    current_room["items"].append(item_redkey)
                break
        print("You have nothing to poor")
    elif current_room == rooms["Metal Box"] and (command == "push" or command == "lift") and article == "box":
        print("The box is too heavy to lift.")
    elif current_room == rooms["Red Door"] and command == "use" and article + extension == "redkey":
        inventory.remove(item_redkey)
        print("As you unlock the red door with the red key, a keypad opens.")
        current_room = rooms["Second Keypad"]
        rooms["Second Room"]["exits"]["reddoor"] = "Second Keypad"
    elif current_room == rooms["Safe"] and (command == "enter" or command == "type") and article == "816":
        if current_room["description"] != "The safe lies ajar and you can see inside.":
            print("The safe unlocks when you enter in the correct combination.")
            current_room["items"].append(item_bottle)
            current_room["items"].append(item_picture)
            current_room["description"] = "The safe lies ajar and you can see inside."
    elif current_room == rooms["Second Keypad"] and (command == "enter" or command == "type") and article == "2187":
        print("As you enter the code into the keypad, the door opens and step into another room.")
        current_room = rooms["Mirror Room"]
        rooms["Second Room"]["exits"]["reddoor"] = "Mirror Room"
    elif current_room == rooms["Mirror"] and (command == "breathe") and article == "mirror":
        print("Your breath reveals something written on the mirror, it seems to be a password. It says: IAMGOD")
    elif current_room == rooms["Mirror"] and (command == "look") and article == "mirror":
        print("""@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+@@
@@      ++++##++++++######+'+####'+;''+##++++++';:::;;;;;;;';'.    +@@
@@     ++#+##++##+######+++++#####+++''++#++'+++;';;::;';;;;;:;:   +@@
@@   .#+############+'';::++#'++;'#+;:::;+########+#+'''::,,;''+'  +@@
@@   '+##########+';:::,::;;:'::''::,:::;#+######++++::,,.`.,+#### +@@
@@   +##########++';:::::::::;::;:::,:::;++#####+''+',,...`..'#### +@@
@@   ##########++';::::::::::::::,,,,,::::;;;;;;::,,,.....``.;+### +@@
@@  ;##########+';::::,::::::::::::::::::::::,,,,,,....`````.,;### +@@
@@  ;##########';::::::::,,,:::::::::::::::::,::,,,,,...````.,'+## +@@
@@  +#####+++++':::::::::::::::::::::;;;;;::::;:::,....`````.,###' +@@
@@  +##+##++++''+;;::::::;;;;;;;';;;;;;;;;::;;;;::,........`.,###` +@@
@@  +#+'+##+'''+'''';::;''''''+++++++'';;;;:;';;;;;::,,....`..###  +@@
@@  ++++#####++''++''++#######++++++++''';;;;'''++'''';::,....+#+  +@@
@@  #+'+####+';;'+''++##;;;;;;;;''''+#+';;;;'+++++++''';:,,...;'.  +@@
@@  #'+#####+';::;;''##+;;''+####++''';;'#+''++####+##++';,..;;    +@@
@@  +'''##++';::::::;'#;;'++++##++++'';;;######+++++##++;::,'++;   +@@
@@  +;+;;+++';:::::::;+;;';;;;;;;''';;;;'#:,:'''+'+###+++;,,+++#   +@@
@@  ,;::;'+';;:::::::::::::::;;;;;;;::++#:,,:;+;;'';;;;,.,;;,,#+   +@@
@@   +::''+;:;:::::::::,,::::::::::::::;:,,.`,;,::::,....,,..:,    +@@
@@   ;+:::;;::::::::::,::::::::::::::::::,,.``.,`...,,.,,.```.'`   +@@
@@   `##::,::::::::::::::::::::::;;;::;;:::::,..::::::,,....:      +@@
@@   `###:::::::::::::::::::::::;;;;;'+#+;;;;:;:;;::::,,...,:      +@@
@@   `###+;;:::::::::::::::::::;;:::::;;;''';;,,:;;:::,,,.,,,      +@@
@@    `##+:::::::::::::::::::;;:::::;;;;;';;:,..,,;;;:,,,,:,       +@@
@@    :###;::::::::::::::::;;;:::::;:;:;;;;;:,....,;;:,,,,:        +@@
@@        ;:::::::::::::::::::::;::::::;:,.,..,,,,.,:;:,,:.        +@@
@@        ,;::::::::::::::::::;;;;;;''''';;'';,:::,.;;:,,:         +@@
@@          ;;;;;;;:::;;;;:::;;;:::;;;;;;;:::;''''':::,,:          +@@
@@           ;;;;;;;;;;;;;;;;;:::::;;;'''''';::,:;;;:,:`           +@@
@@            ';;;;'';;;;;;;:::::::::;;''';;::,,,::::;             +@@
@@            ;;;;;;''';;;;;::::::::::;;;;:,.,.,,,:;;              +@@
@@            ,';;;;;'''';;;;:::::::::::;:,,.....,:;               +@@
@@             +;;;;;'''''';;;::::::::::;::,,...,:;                +@@
@@             `';;;';''''''';;:;;;;;;;;;;::,,,,:'                 +@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")

    elif current_room == rooms["Gold Door"] and command == "use" and article+extension == "goldkey":
         inventory.remove(item_goldkey)
         print("As you unlock the gold door with the gold key, a keypad opens.")
         current_room = rooms["Third Keypad"]
         rooms["Second Room"]["exits"]["golddoor"] = "Third Keypad"
    elif current_room == rooms["Third Keypad"] and (command == "enter" or command == "type") and article == "iamgod":
        print("As you enter the code into the keypad, the door opens... You can smell the fresh air, you step through the door and... and...")
        print("Game over?")
        input()
        exit()
    else:   
        return False
    return True

def execute_command(command):
    #This function takes a command (a list of words as returned by
    #normalise_input) and, depending on the type of action performs it.

    command_executed = True
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 2:
            execute_go(command[1], command[2])
        elif len(command) > 1:
        	execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "inspect" or command[0] == "examine":
        if len(command) > 2:
            execute_inspect(command[1], command[2])
        elif len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")

    elif command[0] == "help":
        execute_help()

    elif len(command) > 2:
        if specific_command(command[0], command[1], command[2]) == False:
            command_executed = False
    elif len(command) > 1:
        if specific_command(command[0], command[1]) == False:
            command_executed = False

    if command_executed == False:
        print("This makes no sense.")


def user_input():
    #This function normalises and returns the user input.

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def print_slow(string):
    #Slow printing for introduction
    import sys, random
    from msvcrt import kbhit

    typing_speed = 40
    for letter in string:
        sys.stdout.write(letter)
        #Flush writes everything out in buffer into the terminal
        sys.stdout.flush()

        #Returns true if a keypress is waiting to be read
        key = kbhit()
        if key == False:
            #Produces a random number between 0.0 and 1.0 and
            #divided it by typing speed, using random intervals for realism
            time.sleep(random.random()/typing_speed)
            #Added to prevent typing being too jittery
            time.sleep(0.01)

# This is the entry point of our program

def main():
    #Starts the clock
    print("""___  ___________  ________________   __
|  \/  |  ___|  \/  |  _  | ___ \ \ / /
| .  . | |__ | .  . | | | | |_/ /\ V / 
| |\/| |  __|| |\/| | | | |    /  \ /  
| |  | | |___| |  | \ \_/ | |\ \  | |  
\_|  ________\_|____/\________\_| \_/  
     |  _  | | | |  \/  | ___ \        
     | | | | | | | .  . | |_/ /        
     | | | | | | | |\/| |  __/         
     | |/ /| |_| | |  | | |            
     |___/  \___/\_|  |_\_|            
                                       
                                       """)

    time.clock()

    print_slow("""As you groggily wake up and roll over, you find yourself groping
at empty air tumbling to the cold, hard floor. Looking up it is clear that you
fell from a chair, in a cold, dim, wet and seemingly unfamiliar room.

Why are you here?

Your memory is hazy. In fact, you cannot even recall your
own name. It appears you have some form of amnesia.

As you get to your feet, your attention is caught by the red glare of a digital
clock embedded into the wall. It reads 30:00

29:59

It's counting down. You decide you don't want to be around when it
reaches zero. Perhaps the answers to your questions lie somewhere in the
room. It's time to take a look around.
""")

    time.sleep(1)

    # Main game loop

    #When 30 minutes has elapsed, the game ends
    while time.clock() < 1800:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Shows the menu
        command = user_input()

        # Execute the player's command
        execute_command(command)
    print("You ran out of time!")   
    print("Game Over")
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

