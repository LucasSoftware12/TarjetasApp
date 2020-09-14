from django import forms
from .models import usuario


class usuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ["nombre", "email", "password"]
