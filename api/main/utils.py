from django.http import JsonResponse
import json
from .errors import Error , newError
def encode(data):
    return data

def send(data , status=200):
    return JsonResponse(data = encode(data) , safe=False, status=status)

def sendError(err:Error):
    return JsonResponse(data = err.responseData() , safe=False, status=err.responseStatus())



def parseBody(b):
    return json.loads(b)