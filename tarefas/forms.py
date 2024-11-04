from django import forms
from .models import Tarefa
from trabalhos.models import Trabalho  # Import do modelo Trabalho

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['trabalho', 'descricao', 'estado', 'prioridade']  # Substituir cliente por trabalho

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Atualização dos atributos do widget para o campo 'trabalho'
        self.fields['trabalho'].queryset = Trabalho.objects.all()  # Carrega todos os Trabalhos disponíveis
        self.fields['trabalho'].widget.attrs.update({'class': 'form-select'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-select'})
        self.fields['prioridade'].widget.attrs.update({'class': 'form-select'})
