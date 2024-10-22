from django import forms
from .models import Dominio

class DominioForm(forms.ModelForm):
    class Meta:
        model = Dominio
        fields = ['nome', 'extensao', 'estado', 'data_criacao', 'cliente']  # Inclui 'data_criacao', remove 'data_expiracao'
        widgets = {
            'data_criacao': forms.DateTimeInput(attrs={'type': 'date'}),
        }
