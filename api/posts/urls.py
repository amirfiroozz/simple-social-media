from django.urls import path
from .views import *

urlpatterns = [
    path('<str:postId>/comments' , postCommentsListView),
    path('<str:postId>/likes' , postLikesListView),
]