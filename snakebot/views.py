from django.http import HttpResponse, JsonResponse
from snakebot.http_utils import SnakeBotJsonResponse
from snakebot.game_objects import *


def ping(request):
    return HttpResponse("Ping boys")


def start(request):
    my_snake = Snake()
    return SnakeBotJsonResponse(my_snake)


def move(request):
    return SnakeBotJsonResponse(MoveCommand())


def end(request):
    print(f"GAME OVER, RESULTS:")
    print(f"{request.body}")
    return HttpResponse("End boys")
