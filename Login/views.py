from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from User.models import *

# Create your views here.


def Home(request):

    if request.method == "POST":
        User_nombre = request.POST["nombre"]
        User_email = request.POST["email"]
        User_password = request.POST["password"]
        print("crear usuario")
        user = usuario.objects.create_user(
            nombre=User_nombre, password=User_password, email=User_email
        )
        usuario.save()
        print("User created!")
        return redirect("/")
    else:
        return render(request, "login/index.html")
        print("no se creo nada che un bajon")


