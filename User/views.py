from django.shortcuts import render
from User.models import *


# Create your views here.

#fuciona creando notas de id_usuario=1 y con el usuario de id=1
def mostrar_notas(request):
    user = usuario.objects.get(id=1)
    todos = nota.objects.filter(id_usuario=1)
    ctx = {"usuario_nombre": user.nombre, "notas": todos}
    return render(request, "notas.html", ctx)
