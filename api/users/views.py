from rest_framework.decorators import api_view
from main.utils import send , sendError, parseBody
from main.errors import Error
from .services import UserServices
from posts.services import PostService
from likes.services import LikeService
from comments.services import CommentService


userService = UserServices()
postService = PostService()
commentService = CommentService()
likeService = LikeService()


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


def showAllusers():
    return send(userService.toListOfDict(userService.getAllUsers()))

def newUser(username):
    return send(userService.toDict(userService.newUser(username)))

def showUser(userId):
    user = getUser(userId)
    if user==None:
        return sendError(Error.userNotFoundedError())
    return send(userService.toDict(user))

def showUserPosts(userId):
    return send(postService.toListOfDict(postService.getAllPostByUserId(userId)))

def newUserPost(content , userId):
    user = getUser(userId)
    if user==None:
        return sendError(Error.userNotFoundedError())
    return send(postService.toDict(postService.newPost(content , user)))

def newUserComment(content ,userId , postId ):
    user = getUser(userId)
    if user==None:
        return sendError(Error.userNotFoundedError())
    post = getPost(postId)
    if post==None:
        return sendError(Error.postNotFoundedError())
    return send (commentService.toDict(commentService.newComment(content , post , user)))

def newUserLike(userId , postId ):
    user = getUser(userId)
    if user==None:
        return sendError(Error.userNotFoundedError())
    post = getPost(postId)
    if post==None:
        return sendError(Error.postNotFoundedError())
    return send(likeService.toDict(likeService.newLike(post , user)))

def getPost(postId):
    return postService.getPost(postId)

def getUser(userId):
    return userService.getUser(userId)



