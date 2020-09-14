# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"Name: {self.name}\tLocation: {self.room}"

    def move_to(self, direction):
        move_room = getattr(self.room, f"{direction}_to")
        if (move_room != ""):
            self.room = move_room
        else:
            print("\nYou may not go in this direction!\n")


    def check_inventory(self):
        if len(self.inventory) > 0:
            print(f"\nYour inventory currently contains:")
            for i in self.inventory:
                print(f"\n{i.name}: {i.description}")
        else :
            print(f"\nYour inventory is currently empty")        