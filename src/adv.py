import textwrap

from room import Room
from player import Player
from item import Item

# Declare all the items

ring = Item('ring', 'family heirloom')
hat = Item('hat', 'former property of Indiana Jones')
rope = Item('rope', 'useful for climbing')
journal = Item('journal', 'blank or written in invisible ink?')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['outside'].items.append(hat)
room['foyer'].items.append(rope)
room['narrow'].items.extend([ring, journal])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def layout():
    print(f'{textwrap.shorten(player.current_room.description, 200)}')

play = True
new_player = input("Enter player's name: ")
player = Player(new_player, room['outside'])
print(f'\n{player.name} is ready to move...')
print(f'Starting Location: {player.current_room.name}')
layout()


while play == True:
    # ask for user input
    move = input(f"\nWhat is {player.name}'s next move? (n, s, e, w, i, take, drop): ")
    moves = move.split()

    # parse move
    if (move == 'n') & (player.current_room.n_to != None):
        player.current_room = player.current_room.n_to
        print(f'\nMoved NORTH to the {player.current_room.name}')
    elif (move == 's') & (player.current_room.s_to != None):
        player.current_room = player.current_room.s_to
        print(f'\nMoved SOUTH to the {player.current_room.name}')
    elif (move == 'e') & (player.current_room.e_to != None):
        player.current_room = player.current_room.e_to
        print(f'\nMoved EAST to the {player.current_room.name}')
    elif (move == 'w') & (player.current_room.w_to != None):
        player.current_room = player.current_room.w_to
        print(f'\nMoved WEST to the {player.current_room.name}')
    elif (move not in ['n', 's', 'e', 'w']):
        print('\n****** NOT A VALID MOVE ******')
    else:
        print(f'\nStill in the {player.current_room.name}.')
    player.current_room.room_items()
    layout()
