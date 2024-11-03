from django import forms
from .models import Trabalho

class TrabalhoForm(forms.ModelForm):
    """Formulário para o modelo Trabalho."""
    
    class Meta:
        model = Trabalho
        fields = [
            'cliente', 'titulo', 'descricao', 'data_inicio', 
            'prazo', 'tipo_trabalho', 'prioridade', 
            'estado_trabalho', 'teve_proposta', 
            'numero_proposta', 'pdf_proposta'
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite a descrição...'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Selecione a data de início'}),
            'prazo': forms.NumberInput(attrs={'placeholder': 'Digite o prazo em dias', 'min': 0}),  # Alterado para NumberInput
            'pdf_proposta': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }
        labels = {
            'teve_proposta': 'Teve Proposta?',
            'numero_proposta': 'Número da Proposta',
            'pdf_proposta': 'Arquivo PDF',  # Label atualizado para consistência
        }
        
    def __init__(self, *args, **kwargs):
        """Inicializa o formulário e define a etiqueta vazia para o cliente."""
        super().__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = "Selecione um cliente"  # Define o rótulo vazio
        self.fields['estado_trabalho'].initial = 'standby'  # Define o estado inicial
