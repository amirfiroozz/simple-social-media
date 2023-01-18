from django.http import JsonResponse
import json

def encode(data):
    return data

def send(data , status):
    return JsonResponse(data = encode(data) , safe=False, status=status)


def parseBody(b):
    return json.loads(b)