# Chris Ritter IT-140

import sys, time
from dictionaries import locations
from story import *

# Classes and Functions -----------------------------

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

def letter_printer(message):
    for char in message:
        print(text_decoration.ITALICS + text_decoration.BOLD + text_decoration.YELLOW + char, end='' + text_decoration.END)
        sys.stdout.flush()
        time.sleep(0.015)

def main_menu():
    print(text_decoration.BOLD + text_decoration.GREEN + 'Welcome to BORG INVASION: A Star Trek Text Adventure' + text_decoration.END)
    print(text_decoration.ITALICS + 'Developed by Chris Ritter.\n' + text_decoration.END)
    play_game = int(input(text_decoration.BOLD + '1. Play Game   2. Exit: ' + text_decoration.END))

    # player selection starts game
    if play_game == 1:
        print()     
        print('Instructions:\nNavigate through the Enterprise to get to Engineering. Collect important items along the way. Once in Engineering, defeat the Borg Drones to win the game.\nFailing to collect all of the items will result in defeat!')
        print()
        print("Navigation:\nTo navigate through the ship, type a direction: ex." + text_decoration.BOLD + text_decoration.GREEN + "'north'" + text_decoration.END + "." + "\n\nGathering Items:\nObtain items by typing the word" + text_decoration.BOLD + text_decoration.GREEN + " 'take' " + text_decoration.END + "the item name: ex. 'take tricorder'.\n\nType" + text_decoration.BOLD + text_decoration.GREEN + " 'exit' " + text_decoration.END + "to quit.")
        print()
        print(text_decoration.DARKCYAN + text_decoration.BOLD + 'Movement directions: north, south, east, west\n\n' + text_decoration.END)
        
        # prints opening story
        message = backstory
        letter_printer(message)
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
        print(text_decoration.BOLD + 'Useful Items in this area: {}'.format(', '.join(current_room['equipment']).capitalize()) + text_decoration.END)
    else:
        print('There are no useful items in this area.')

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
            if current_room == locations['engineering']:
                if len(inventory) == 6:
                    message = ending
                    letter_printer(message)
                    print()
                    print()
                    print(text_decoration.GREEN + text_decoration.BOLD + 'You have made it to Engineering and defeated the Borg!'+ text_decoration.END)
                    print()
                    print('Thank you for playing Borg Invasion!')
                    print()
                    exit()
                if len(inventory) != 6:
                    message = defeat
                    letter_printer(message)
                    print()
                    print()
                    print(text_decoration.RED + text_decoration.BOLD + "You have made it to Engineering, but were assimilated by the Borg. You will never see the hallowed halls of Sto'Vo'Kor"+ text_decoration.END)
                    print()
                    print('You did not collect the necessary items to complete your mission.')
                    print()
                    print('Thank you for playing Borg Invasion!')
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
            current_room['equipment'].remove(item)
            inventory.append(item)
            print(text_decoration.DARKCYAN + text_decoration.BOLD + 'You have obtained {}.'.format(item) + text_decoration.END)
            print(text_decoration.BOLD + text_decoration.PURPLE + 'Inventory: {}'.format(', '.join(inventory).upper()) + text_decoration.END)
            print()
        else:
            print(text_decoration.RED + text_decoration.BOLD + 'There is no {} here.'.format(item).upper() + text_decoration.END)
            print()

    # invalid command
    else:
        print(text_decoration.RED + text_decoration.BOLD + 'COMMAND NOT UNDERSTOOD! PLEASE RESTATE COMMAND.' + text_decoration.END)
        print()