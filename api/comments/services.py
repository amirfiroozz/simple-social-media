from .models import Comment
from bson import ObjectId

class CommentService:

    def newComment(self , content , post , user):
        comment = Comment(content = content , post = post  , user = user)
        return self.saveComment(comment)

    def getAllCommentsByPostId(self , postId):
        comments = Comment.objects.filter(post=ObjectId(postId)).order_by('-created_at').all()
        return comments

    def saveComment(self , comment):
        comment.save()
        return comment
    

    def toDict(self , comment):
        return {
            "_id":str(comment._id),
            "content":comment.content,
            "username":comment.user.username,
        }
    
    def toListOfDict(self , comments):
        return [self.toDict(c) for c in comments]



