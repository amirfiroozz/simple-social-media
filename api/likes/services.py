from .models import Like
from bson import ObjectId

class LikeService:

    def newLike(self , post , user):
        like = Like(post = post  , user = user)
        return self.saveLike(like)

    def getAllLikesByPostId(self , postId):
        likes = Like.objects.filter(post=ObjectId(postId)).order_by('-created_at').all()
        return likes
    
    def findLikeByUserIdAndPostId(self , postId , userId):
        alreadyLiked = Like.objects.filter(post=postId , user = userId).first()
        return alreadyLiked

    def saveLike(self , like):
        like.save()
        return like
    

    def toDict(self , like):
        try:
            return {
                "_id":str(like._id),
                "username":like.user.username,
            }
        except:
            return like
    
    def toListOfDict(self , likes):
        return [self.toDict(l) for l in likes]



