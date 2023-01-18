from djongo import models
from users.models import User

class Post(models.Model):
    _id = models.ObjectIdField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="user")
    class Meta:
        db_table = "posts"




