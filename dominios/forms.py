from django import forms
from .models import Dominio

class DominioForm(forms.ModelForm):
    class Meta:
        model = Dominio
        # Remover 'data_criacao' do formulário, já que ele é não-editável
        fields = ['nome', 'extensao', 'estado', 'data_expiracao', 'cliente']
