from rest_framework.decorators import api_view
from main.utils import send , parseBody
from .services import UserServices
from posts.services import PostService


userService = UserServices()
postService = PostService()


@api_view(["GET","POST"])
def userCreateListView(request):
    if request.method=="GET":
        return send(showAllusers() , 200)
    else:
        userData = parseBody(request.body)
        return send(newUser(userData['username']) , 200)
        
@api_view(["GET"])
def userView(request , id):
    return send(showUser(id) , 200)

@api_view(["GET" , "POST"])
def userPostsListCreateView(request , userId):
    if request.method=="GET":
        return send(showUserPosts(userId) , 200)
    else:
        postData = parseBody(request.body)
        return send(newUserPost(postData['content'] ,userId),200)


def showAllusers():
    return userService.toListOfDict(userService.getAllUsers())

def newUser(username):
    return userService.toDict(userService.newUser(username))

def showUser(id):
    return userService.toDict(userService.getUser(id))

def showUserPosts(userId):
    return postService.toListOfDict(postService.getAllPostByUserId(userId))

def newUserPost(content , userId):
    return postService.toDict(postService.newPost(content , userService.getUser(userId)))


