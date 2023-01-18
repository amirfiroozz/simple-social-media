from .views import *
from django.urls import path

urlpatterns = [
    path('' , userCreateListView),
    path('<str:id>' , userView),
]