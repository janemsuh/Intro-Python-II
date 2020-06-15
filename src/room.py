# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def room_items(self):
        if len(self.items) == 0:
            print(f'{self.name} is empty.')
        else:
            print(f'{self.name} has the following item(s):')
            for item in self.items:
                print(item.name)

    def addItem(self, *newItems):
        for item in newItems:
            self.items.append(item)

    def removeItem(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'Cannot drop {item.name}.')