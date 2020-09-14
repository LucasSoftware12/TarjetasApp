from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
#from User.models import *
from User.forms import usuarioForm
# Create your views here.


def Home(request):

    if request.method == "POST":
        User_form = usuarioForm(request.POST)
        if User_form.is_valid():
            User_form.save()
            return redirect('Home')#no me redirecciona es para arreglar T_T
    else:
        User_form = usuarioForm()
    return render(request,'login/index.html',{'User_form':User_form})

''' User_nombre = request.POST["nombre"]
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
        print("no se creo nada che un bajon")'''


