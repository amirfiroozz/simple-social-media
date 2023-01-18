from rest_framework.decorators import api_view
from main.utils import send
from comments.services import CommentService
from likes.services import LikeService

commentService = CommentService()
likeService = LikeService()


@api_view(["GET"])
def postCommentsListView(request , postId):
    return send(showPostComments(postId), 200)

@api_view(["GET"])
def postLikesListView(request , postId):
    return send(showPostLikes(postId), 200)


def showPostComments(postId):
    return commentService.toListOfDict(commentService.getAllCommentsByPostId(postId))

def showPostLikes(postId):
    return likeService.toListOfDict(likeService.getAllLikesByPostId(postId))





