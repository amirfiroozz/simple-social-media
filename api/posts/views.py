from rest_framework.decorators import api_view
from .helpers import *

@api_view(["GET"])
def postCommentsListView(request , postId):
    return showPostComments(postId)

@api_view(["GET"])
def postLikesListView(request , postId):
    return showPostLikes(postId)




