
from main.utils import send
from comments.services import CommentService
from likes.services import LikeService

commentService = CommentService()
likeService = LikeService()


def showPostComments(postId):
    return send(commentService.toListOfDict(commentService.getAllCommentsByPostId(postId)))

def showPostLikes(postId):
    return send(likeService.toListOfDict(likeService.getAllLikesByPostId(postId)))


