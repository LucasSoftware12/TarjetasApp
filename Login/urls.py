from django.urls import path
from Login import views
from .views import *

urlpatterns = [
    path("", Home, name="Home"),
]