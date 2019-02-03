from django.urls import path
from .views import *

from . import views
urlpatterns = [
    path("todo/", home, name="home"), 
    path("add", addTodo, name="add"),
    path("complete/<id>", completetodo, name="complete" )
]
