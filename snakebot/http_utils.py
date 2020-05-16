from json import JSONEncoder
from django.http import JsonResponse


class SnakeBotJsonEncoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


''' Utility class that handles the Plain old objects passed into it into a json format'''
class SnakeBotJsonResponse(JsonResponse):

    def __init__(self, data, encoder=SnakeBotJsonEncoder, safe=False, json_dumps_params=None, **kwargs):
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)
