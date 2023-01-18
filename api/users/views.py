from rest_framework.decorators import api_view
from main.utils import send , parseBody
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
    
@api_view(["POST"])
def userCommentCreateView(request , userId , postId):
    commentData = parseBody(request.body)
    return send(newUserComment(commentData['content'] , userId , postId),200)


@api_view(["POST"])
def userLikeCreateView(request , userId , postId):
    return send(newUserLike(userId , postId),200)


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

def newUserComment(content ,userId , postId ):
    return commentService.toDict(commentService.newComment(content , postService.getPost(postId) , userService.getUser(userId)))

def newUserLike(userId , postId ):
    return likeService.toDict(likeService.newLike(postService.getPost(postId) , userService.getUser(userId)))



