#!/usr/bin/python3

from map import rooms
from player import *
from items import *
from gameparser import *
import time

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

    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    #This function takes a dictionary of exits and a direction and
    #returns the name of the room into which this exit leads.

    return rooms[exits[direction]]["name"]

def is_valid_exit(exits, chosen_exit):
    #This function checks whether the player has chosen a valid exit.

    return chosen_exit in exits

def execute_go(direction):
    #This function, given the direction updates the current room
    #to reflect the movement of the player if the direction is a valid exit.

    global current_room

    if is_valid_exit(current_room["exits"], direction):
        current_room = rooms[current_room["exits"][direction]]
    else:
        print("You cannot go there.")

def execute_inspect(article, extension = ""):
    #This function allows a part of the environment to be examined
    
    global inventory
    global current_room

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
    
    if article_inspected == False:
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

def room_specific_command(command, article, extension = ""):
    #This function is for running the hard-coded room commands which produce a specific result
    global current_room

    if current_room == rooms["Chair"] and command == "pick" and article == "chair":
        print("When you pick up the chair a green key clatters to the floor.")
        current_room["items"].append(item_greenkey)
    elif current_room == rooms["Green Door"] and command == "use" and article + extension == "greenkey":
        inventory.remove(item_greenkey)
        print("As you unlock the green door with the green key, a keypad opens.")
        current_room = rooms["Keypad"]
        rooms["Start"]["exits"]["greendoor"] = "Keypad"
    elif current_room == rooms["Clock"] and command == "check" and article == "time":
        minutes = time.clock() / 60
        seconds = time.clock() % 60
        if 30 - minutes >= 0:
            print(str(int(30 - minutes)) + ":" + str(int(60 - seconds)) + " is what can be read on the clock.")
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
        if len(command) > 1:
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

    elif len(command) > 2:
        if room_specific_command(command[0], command[1], command[2]) == False:
            command_executed = False
    elif len(command) > 1:
        if room_specific_command(command[0], command[1]) == False:
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
    time.clock()

    print_slow("""As you groggily wake up and roll over, you find yourself groping
at empty air tumbling to the cold, hard floor. Looking up it is clear that you fell
from a chair, in a cold, dim, wet and seemingly unfamiliar room.

Why are you here?

Your memory is hazy. In fact, you cannot even recall your
own name. It appears you have some form of amnesia.

As you get to your feet, your attention is caught by the red glare of a digital
clock embedded into the wall. It reads 30:00.

29:59

It's counting down. You decide you don't want to be around when it
reaches zero. Perhaps the answers to your questions lie somewhere in the
room. It's time to take a look around.
""")
    time.sleep(1)

    # Main game loop

    #When 30 minutes has elapsed, the game ends
    while time.clock() < 108000:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Shows the menu
        command = user_input()

        # Execute the player's command
        execute_command(command)
    print("Game Over")
# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

