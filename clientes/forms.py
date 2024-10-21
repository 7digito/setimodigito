from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'nif', 'morada', 'codigo_postal', 'localidade', 'telefone', 'email', 'website']
