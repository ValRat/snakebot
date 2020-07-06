from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from snakebot.http_utils import SnakeBotJsonResponse
from snakebot.game_objects import Game, Snake, MoveCommand, GameObjectFactory

import json


def ping(request):
    return HttpResponse("Ping boys")


def start(request):

    try:

        if request.method != "POST":
            return HttpResponseBadRequest("This endpoint only accepts POST request")

        print("Initializing a game")

        start_dict = json.loads(request.body)

        # Initialize a game here
        new_game_id = start_dict["game"]["id"]

        game = Game(new_game_id)
        print(f"Initializing game with ID: {new_game_id}")

        my_snake = Snake()
        return SnakeBotJsonResponse(my_snake)

    # TODO: Make exception catching more specific
    except Exception as e:
        print(f"An exception occurred starting the game: {e}")
        return HttpResponseServerError(str(e))


def move(request):
    try:
        if request.method != "POST":
            return HttpResponseBadRequest("This endpoint only accepts POST request")

        print("Got move request")

        request_dictionary = json.loads(request.body)



        # Parse into Board
        # - parse board dimensions
        # - parse food
        # - Parse snakes (includes me)
        # - parse, me
        board = GameObjectFactory.parse_board(request_dictionary["board"])
        my_snake = GameObjectFactory.parse_snake(request_dictionary["you"])

        # Pass board into A*
        # - given board, and snake identity, returns best movement

        # A*.move() # TODO: Later

        # Return result as http response

        my_command = MoveCommand()
        return SnakeBotJsonResponse(my_command)
    except Exception as e:
        print(f"An exception occured querying for a move: {e}")
        return HttpResponseServerError(str(e))


def end(request):
    print(f"GAME OVER, RESULTS:")
    print(f"{request.body}")
    return HttpResponse("End boys")
