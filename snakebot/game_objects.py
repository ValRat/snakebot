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
        self.head = None
        self.length = None
        self.shout = None

    def Initialise(self, snake_id, name, health, body, head, length, shout):
        self.id = snake_id
        self.name = name
        self.health = health
        self.body = body
        self.head = head
        self.length = length
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


class GameObjectFactory:
    """
    Creates game objects based on a dictionary of its values
    """

    @staticmethod
    def parse_board(values_dict):
        height = values_dict["height"]
        width = values_dict["width"]
        food = GameObjectFactory.parse_food(values_dict["food"])
        snakes = GameObjectFactory.parse_snakes(values_dict["snakes"])
        return Board(height, width, food, snakes)

    @staticmethod
    def parse_snake(snake):
        snake_id = snake["id"]
        name = snake["name"]
        health = snake["health"]
        body = GameObjectFactory.parse_coordinates(snake["body"])
        head = GameObjectFactory.parse_coordinate(snake["head"])
        length = snake["length"]
        shout = snake["shout"]
        # The color, head_type, tail_type are only sent once to the server.
        # they are not returned again.
        # TODO: We therefore have no representation on how the enemy looks like?
        snake_obj = Snake()
        snake_obj.Initialise(snake_id, name, health, body, head, length, shout)
        return snake_obj

    @staticmethod
    def parse_snakes(snakes):
        return list(map(lambda snake: GameObjectFactory.parse_snake(snake), snakes))

    @staticmethod
    def parse_coordinate(coord):
        return coord["x"], coord["y"]

    @staticmethod
    def parse_coordinates(coords):
        return list(map(lambda coord: GameObjectFactory.parse_coordinate(coord), coords))

    @staticmethod
    def parse_food(values_dict):
        return GameObjectFactory.parse_coordinates(values_dict)





