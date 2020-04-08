# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    def move_player(self, direction):
        next_room = getattr(self.current_room, direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print('There is nothing in that direction')
