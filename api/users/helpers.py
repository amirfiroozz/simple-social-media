from main.utils import send , sendError
from main.errors import Error
from .services import UserServices
from posts.services import PostService
from likes.services import LikeService
from comments.services import CommentService

userService = UserServices()
postService = PostService()
commentService = CommentService()
likeService = LikeService()

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

def newUserLike(userId , postId):
    user = getUser(userId)
    if user==None:
        return sendError(Error.userNotFoundedError())
    
    post = getPost(postId)
    if post==None:
        return sendError(Error.postNotFoundedError())
    
    alreadyLiked = likeService.findLikeByUserIdAndPostId(postId , userId)
    print(alreadyLiked)
    if alreadyLiked!=None:
        return sendError(Error.alreayLikedError())
    
    return send(likeService.toDict(likeService.newLike(post , user)))

def getPost(postId):
    return postService.getPost(postId)

def getUser(userId):
    return userService.getUser(userId)