from random import randrange


class Snake:

    def __init__(self):
        self.color = "#ff0000"
        self.headType = "bendr"  # TODO: Pick a cooler head type
        self.tailType = "pixel"


class MoveCommand:

    moves = ["right", "left", "up", "down"]

    def __init__(self):
        self.move = self.moves[randrange(4)]
        self.shout = f"I am moving {self.move}!"
