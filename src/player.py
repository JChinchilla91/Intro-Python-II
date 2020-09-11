# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, location, items = []):
        self.name = name
        self.location = location
        self.items = items

    def move(self, direction):
        new_location = self.location.location_move(direction)
        
        if new_location is not None and len(new_location.room_items) == 0:
            self.location = new_location
            print(f'\n{self.name}: You are now in the {new_location.name}.. {self.location}')
        elif new_location is not None:
            self.location = new_location
            print(f'\n{self.name}: You are now in {new_location.name}. \nIn this room you see... {new_location.items}')
        else:
            if direction == 'N':
                direction = 'North'
            if direction == 'E':
                direction = 'East'
            if direction == 'S':
                direction = 'South'
            if direction == 'W':
                direction = 'West'
            print(f'Nothing to the {direction}! Please choose another direction!')

    def __str__(self):
        return f'{self.name}'