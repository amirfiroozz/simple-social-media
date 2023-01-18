from .models import Post
from bson import ObjectId

class PostService:

    def newPost(self , content , user):
        post = Post(content = content , user = user)
        return self.savePost(post)

    def savePost(self , post):
        post.save()
        return post
    
    def getAllPostByUserId(self , userId):
        posts = Post.objects.filter(user=ObjectId(userId)).all()
        return posts

    def getPost(self , id):
        post = Post.objects.filter(_id=ObjectId(id)).first()
        return post

    def toDict(self , post:Post):
        return {
            "_id":str(post._id),
            "content":post.content
        }
    
    def toListOfDict(self , posts):
        return [self.toDict(p) for p in posts]



