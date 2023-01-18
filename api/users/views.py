from rest_framework.decorators import api_view
from main.utils import send , sendError, parseBody
from .helpers import *


@api_view(["GET","POST"])
def userCreateListView(request):
    if request.method=="GET":
        return showAllusers()
    else:
        userData = parseBody(request.body)
        return newUser(userData['username'])
        
@api_view(["GET"])
def userView(request , id):
    return showUser(id)

@api_view(["GET" , "POST"])
def userPostsListCreateView(request , userId):
    if request.method=="GET":
        return showUserPosts(userId)
    else:
        postData = parseBody(request.body)
        return newUserPost(postData['content'] ,userId)
    
@api_view(["POST"])
def userCommentCreateView(request , userId , postId):
    commentData = parseBody(request.body)
    return newUserComment(commentData['content'] , userId , postId)


@api_view(["POST"])
def userLikeCreateView(request , userId , postId):
    return newUserLike(userId , postId)






