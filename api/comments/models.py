from djongo import models
from users.models import User
from posts.models import Post

class Comment(models.Model):
    _id = models.ObjectIdField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="post")
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    class Meta:
        db_table = "comments"