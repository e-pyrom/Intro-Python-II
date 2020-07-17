from room import Room
from player import Player
from item import Item, Weapon, Healing

# Declare all items

item = {
    'sword': Weapon("Sword", "Trusty sword for close range protection.", 2),
    'bow': Weapon("Bow and Arrow", "Classic bow and arrow used for long range hunting and a weapon.", 5),
    'healing1': Healing("First aid kit", "Sack filled with bandages, gauze, and ointments to treat wounds", 3),
    'healing2': Healing("Magic Mushrooms", "Natural remedy that is a magic cure all.", 5),
    'coins': Item("Pile of Gold", "Pile of gold use for currency to purchase items.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ['bow']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input('Please Enter your name: '), room['outside'], [item['bow'], item['coins']])
print('Hello, ', player.name)
print(player.current_room)

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

while 1:
    command = input(">").split(" ")
    if command == 'q':
        break
    elif command[0] in ('n', 's', 'e', 'w'):
        player.travel(command[0])
    elif command[0] == 'drop':
        if(len(command) > 0):
            if player.drop_item(command[1]):
                player.current_room.add_item(command[1])
        else:
            print("No item under that name.")
    elif command[0] in ('get', 'take'):
        if(len(command) > 1):
            if player.current_room.remove_item(command[1]):
                player.pickup_item(command[1])
        else:
            print("No item under that name.")
    elif command[0] == 'i':
        player.show_inventory()
    else:
        print("I can't do that", player.name)