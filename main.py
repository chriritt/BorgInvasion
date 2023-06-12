import sys, time
from locations import locations


class text_decoration:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    DARKCYAN = '\033[36m'
    BOLD = '\033[1m'
    ITALICS = '\x1B[3m'
    END = '\033[0m'

char_message =  "During a routine mission, the USS Enterprise-D unexpectedly encountered a formidable Borg cube. " \
                "Despite valiant efforts, the Borg overwhelmed the ship's defenses, leaving most of the crew " \
                "incapacitated. In the midst of the chaos, Worf fought courageously, engaging multiple Borg drones in " \
                "intense combat. However, he was eventually struck down and rendered unconscious by a powerful blast " \
                "from an assimilation tubule. Now, as Worf awakens on the bridge, he finds himself surrounded by the " \
                "aftermath of the Borg assault, his crewmates lying motionless. Determined to assess the situation " \
                "and protect the ship, Worf's warrior instincts kick in as he searches for any signs of the Borg " \
                "presence and a possible way to regain control of the USS Enterprise-D..."

def letter_printer(char_message):
    for char in char_message:
        print(text_decoration.ITALICS + text_decoration.YELLOW + char, end='' + text_decoration.END)
        sys.stdout.flush()
        time.sleep(0.015)

# welcome message
print(text_decoration.BOLD + text_decoration.GREEN + 'Welcome to BORG INVASION: A Star Trek Text Adventure' + text_decoration.END)
print('\033[0m' + 'Developed by Chris Ritter.\n')
play_game = int(input('1. Play Game   2. Exit: '))

# player selection starts game
if play_game == 1:
    game_instructions = "Reach Engineering to win the game. \nTo move, type a direction: ex. 'North' Type 'exit' to quit."
    move_directions = ['north', 'north east', 'east', 'south east', 'south', 'south west', 'west', 'north west']

    print()
    print(game_instructions)
    print('Move directions: north, north east, east, south east, south, south west, west, north west\n\n')
    
    # prints opening story
    letter_printer(char_message)
    print()
    print()
    
    current_room = locations['bridge']
    inventory = []
else:
    exit()

# gameplay loop
while True:
    # display player current location and items
    print(text_decoration.BOLD + 'You are {}.'.format(current_room['name']).upper() + text_decoration.END)
    # show items in room
    if current_room['equipment']:
      print(text_decoration.BOLD + 'Helpful items: {}'.format(', '.join(current_room['equipment'])) + text_decoration.END)

    command = input('\nWhat are your orders? ')
    print()

    # player movement
    if command in move_directions:
        if command in current_room:
            current_room = locations[current_room[command]]
            if current_room == locations['engineering']:
                print()
                print('You have made it to Engineering and defeated the Borg!')
                print()
                print('Thank you for playing!')
                print()
                exit()
        # invalid movement
        else:
            print()
            print("You can't go that way.")

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
            print(text_decoration.BOLD + text_decoration.PURPLE + 'Inventory: {}'.format(', '.join(inventory).capitalize()) + text_decoration.END)
            print()
        else:
            print('There is no {} here.'.format(item))

    # invalid command
    else:
        print()
        print('I do not understand that command. Please try again.')

# player selection kills program
else:
    exit()
