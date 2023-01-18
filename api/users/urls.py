from .views import *
from django.urls import path

urlpatterns = [
    path('' , userCreateListView),
    path('<str:id>' , userView),
    path('<str:userId>/posts' , userPostsListCreateView),
    path('<str:userId>/posts/<str:postId>/comments' , userCommentCreateView),
    path('<str:userId>/posts/<str:postId>/likes' , userLikeCreateView),

]