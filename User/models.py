from django.db import models
from datetime import datetime, date

# Create your models here.


class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=20)
    #agregamos un passwor mas¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?¿?

    def __str__(self):
        return self.nombre


class nota(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=400)
    fecha = models.DateField()
    check = models.BooleanField(default=False, verbose_name="realizado")
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo