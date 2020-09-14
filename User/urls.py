from django.urls import path
from .views import *

urlpatterns = [
    path("", mostrar_notas),
]
