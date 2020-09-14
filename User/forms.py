from django import forms
from .models import usuario
from django.db import models


class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        password2=models.CharField(max_length=20)
        fields = ["nombre", "email", "password"]
