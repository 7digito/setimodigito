from django import forms
from .models import Dominio

class DominioForm(forms.ModelForm):
    class Meta:
        model = Dominio
        fields = ['nome', 'extensao', 'estado', 'data_expiracao']  # Remova 'data_criacao'
