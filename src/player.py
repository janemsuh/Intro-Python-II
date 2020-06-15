# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def player_inventory(self):
        if len(self.inventory) == 0:
            print(f'\n{self.name} has no items.')
        else:
            print(f'\n{self.name} has the following item(s):')
            for item in self.inventory:
                print(item.name)

    def addItem(self, action):
        for item in self.current_room.items:
            if item.name == action:
                print(f'\nPicked up {item.name}!')
                self.inventory.append(item)
                self.current_room.removeItem(item)
            else:
                print(f'\nCannot pick up {item.name}.')
    
    def dropItem(self, action):
        for item in self.inventory:
            if item.name == action:
                print(f'\nDropped {item.name}.')
                self.inventory.remove(item)
                self.current_room.addItem(item)
            else:
                print(f'\nCannot drop {item.name}.')