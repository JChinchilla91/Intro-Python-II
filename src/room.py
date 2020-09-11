# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, room_items = []):
        self.name = name
        self.description = description
        self.room_items = room_items
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def location_move(self, direction):
        if direction == 'N':
            return self.n_to
        elif direction == 'E':
            return self.e_to
        elif direction == 'W':
            return self.w_to
        elif direction == 'S':
            return self.s_to

    def __str__(self):
        return f'{self.name} -- {self.description} -- contains {self.room_items}'
