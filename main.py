# Chris Ritter IT-140

import sys, time
from dictionaries import locations
from story import *

# class that handles text decoration
class text_decoration:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    DARKCYAN = '\033[36m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ITALICS = '\x1B[3m'
    END = '\033[0m'
# game instructions function
def game_instructions():
        print()     
        print('Instructions:\nYour mission is to navigate through the USS Enterprise-D and reach Engineering while collecting important items along the way. Defeat the Borg Drones in Engineering to win the game.\nBe warned, failing to collect all of the items will result in defeat!!')
        print()
        print("Navigation:\nTo move around the ship, type the direction you want to go. For example, if you want to go north, simply type " + text_decoration.BOLD + text_decoration.GREEN + "'north'" + text_decoration.END + ".")
        print()
        print('You can move in four primary directions: ' + text_decoration.GREEN + text_decoration.BOLD + 'north, south, east, west' + text_decoration.END)
        print()
        print("Gathering Items:\nCollect valuable items by using the" + text_decoration.GREEN + text_decoration.BOLD + " 'take'" + text_decoration.END + " command followed by the item name. For example, if you want to take a tricorder, type 'take tricorder'. Make sure to gather all the essential items to aid you in your mission.")
        print()
        print("Inventory Limit:\nYour inventory has a maximum capacity of 6 items. If you attempt to pick up an additional item when your inventory is already full, you must first drop an item before you can pick up a new one.\nTo drop an item, use the " + text_decoration.GREEN + text_decoration.BOLD+ "'drop'" + text_decoration.END + " command followed by the item name. For example, to drop a phaser, type 'drop phaser'.")
        print()
        print("Exiting the Game:\nIf you want to exit the game at any time, simply type " + text_decoration.GREEN + text_decoration.BOLD + "'exit'." + text_decoration.END)
        print()
        print(text_decoration.BOLD + text_decoration.GREEN + "Good luck on your mission to defeat the Borg and protect the USS Enterprise!" + text_decoration.END)
        print()
# function that prints story elements a character at a time
def char_printer(message):
    for char in message:
        print(text_decoration.ITALICS + text_decoration.BOLD + text_decoration.YELLOW + char, end='' + text_decoration.END)
        sys.stdout.flush()
        time.sleep(0.010)

def main_menu():
    print(text_decoration.BOLD + text_decoration.GREEN + 'Welcome to BORG INVASION: A Star Trek Text Adventure' + text_decoration.END)
    print(text_decoration.ITALICS + 'Developed by Chris Ritter.\n' + text_decoration.END)
    play_game = int(input(text_decoration.BOLD + '1. Play Game   2. Exit: ' + text_decoration.END))

    # player selection starts game
    if play_game == 1:
        game_instructions()
        
        # prints opening story
        message = backstory
        char_printer(message)
        print()
        print('---------------------------------------------')
        print()

    else:
        exit()
        
# -----------------------------------------------------

# starting var values
move_directions = ['north', 'east', 'south', 'west']               
current_room = locations['bridge']
inventory = []

main_menu()

# gameplay loop
while True:
    # display player current location
    print(text_decoration.BOLD + 'You are {}.'.format(current_room['name']).upper() + text_decoration.END)
    
    # show items in room
    if current_room['equipment']:
        print(text_decoration.BOLD + text_decoration.DARKCYAN + 'Available Items: {}'.format(', '.join(current_room['equipment']).capitalize()) + text_decoration.END)
    # show current inventory
    print(text_decoration.BOLD + text_decoration.PURPLE + 'Inventory: {}'.format(', '.join(inventory).upper()) + text_decoration.END)

    command = input(text_decoration.YELLOW + '\nWhat are your orders? ' + text_decoration.END).lower()
    print()
    print('---------------------------------------------')
    print()

    # player movement
    if command in move_directions:
        if command in current_room:
            current_room = locations[current_room[command]]
            if current_room == locations['turbo lift 2']: # warns player when they're about to enter engineering
                print(text_decoration.RED + text_decoration.BOLD +'This Turbo Lift only goes to Engineering, once there you will not be able to return.\nMake sure you have all of the necessary equipment.' + text_decoration.END)
                print()
            #conditional for entering engineering
            if current_room == locations['engineering']:
                # all items added to inventory
                if len(inventory) == 6:
                    message = ending
                    char_printer(message)
                    print()
                    print()
                    print(text_decoration.GREEN + text_decoration.BOLD + 'You have made it to Engineering and defeated the Borg!'+ text_decoration.END)
                    print()
                    print(text_decoration.BOLD + text_decoration.GREEN + 'Thank you for playing Borg Invasion!' + text_decoration.END)
                    print()
                    exit()
                # less than 6 items added to inventory 
                if len(inventory) != 6:
                    message = defeat
                    char_printer(message)
                    print()
                    print()
                    print(text_decoration.RED + text_decoration.BOLD + "You have made it to Engineering, but were assimilated by the Borg. You will never see the hallowed halls of Sto'Vo'Kor."+ text_decoration.END)
                    print()
                    print(text_decoration.RED + text_decoration.BOLD + 'You did not collect the necessary items to complete your mission.' + text_decoration.END)
                    print()
                    print(text_decoration.BOLD + text_decoration.GREEN + 'Thank you for playing Borg Invasion!' + text_decoration.END)
                    print()
                    exit()
                    break                
        # invalid movement
        else:
            print(text_decoration.RED + text_decoration.BOLD + "YOU CANNOT GO THAT WAY!" + text_decoration.END)
            print()

    # exit game
    elif command in ('exit'):
        print()
        print('Thank you for playing Borg Invasion!')
        break

    # gathering items
    elif command.lower().split()[0] == 'take':
        item = command.lower().split()[1]
        if item in current_room['equipment']:
            if len(inventory) == 6:
                print(text_decoration.RED + text_decoration.BOLD + 'You have already gathered the maximum number of items. You must drop an item to pick up another.' + text_decoration.END)
                print()
            else:
                current_room['equipment'].remove(item)
                inventory.append(item)
                print(text_decoration.DARKCYAN + text_decoration.BOLD + 'Obtained {}.'.format(item) + text_decoration.END)
                print()
        else:
            print(text_decoration.RED + text_decoration.BOLD + 'There is no {} here.'.format(item).upper() + text_decoration.END)
            print()

    # dropping items
    elif command.lower().split()[0] == 'drop':
        item = command.lower().split()[1]
        if item in inventory:
            current_room['equipment'].append(item)
            inventory.remove(item)
            print(text_decoration.DARKCYAN + text_decoration.BOLD + 'Dropped {}.'.format(item) + text_decoration.END)
            print()
        else:
            print('You have not collected that item.')


    # invalid command
    else:
        print(text_decoration.RED + text_decoration.BOLD + 'COMMAND NOT UNDERSTOOD! PLEASE RESTATE COMMAND.' + text_decoration.END)
        print()