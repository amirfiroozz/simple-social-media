from djongo import models
from users.models import User
from posts.models import Post

class Like(models.Model):
    _id = models.ObjectIdField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "likes"