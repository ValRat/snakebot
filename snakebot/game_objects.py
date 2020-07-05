from random import randrange
from enum import Enum


class Direction(Enum):
    LEFT = "left",
    RIGHT = "right",
    UP = "up",
    DOWN = "down"


moves = [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]


class Snake:
    """
    id: unique id for snake in current game
    name: given name by author
    health: integer between 0 - 100 inclusive
    body: array of coords from head to tail
    head: head of the snake, equiv to body[0]
    length: length of the snake, equiv to body.length
    shout: reee
    """

    def __init__(self, color="#ff0000", head_type="bendr", tail_type="pixel"):
        self.color = color
        self.headType = head_type  # TODO: Pick a cooler head type
        self.tailType = tail_type

        # These are received from the game engine
        self.id = None
        self.name = None
        self.health = None
        self.body = None
        self.shout = None

    def Initialise(self, snake_id, name, health, body, shout):
        self.id = snake_id
        self.name = name
        self.health = health
        self.body = body
        self.shout = shout  # TODO: not sure if needed


# Note: These classes which are serialised _cannot_ contain any
#       "non-primitives", i.e. objects, dicts, enums
class MoveCommand:

    def __init__(self):
        self.move = moves[randrange(4)].name
        self.shout = f"I am moving {self.move}!"


class Game:

    def __init__(self, game_id):
        self.id = game_id
        self.board_states = []

    def tick(self, board_state):
        self.board_states.append(board_state)


class Board:
    """
    food: array of coords representing food locations on the game board
    snakes: array of Snakes
    """

    def __init__(self, height, width, food, snakes):
        self.height = height
        self.width = width
        self.food = food
        self.snakes = snakes


