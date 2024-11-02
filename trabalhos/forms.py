from django import forms
from .models import Proposta

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = ['cliente', 'titulo', 'descricao', 'prazo', 'estado', 'pdf']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite a descrição...'}),
            'prazo': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Selecione uma data'}),
            'pdf': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }

    def __init__(self, *args, **kwargs):
        super(PropostaForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].empty_label = "Selecione um cliente"
        
        # Set initial state for new proposals
        if self.instance and self.instance.pk:  # If it's an existing instance
            self.fields['estado'].widget.attrs['readonly'] = True  # Make the state field read-only for existing instances
        else:
            self.fields['estado'].initial = 'solicitada'  # Default to 'solicitada' for new proposals

    def clean_estado(self):
        """
        Prevent changes to estado if the proposal is already created.
        """
        if self.instance and self.instance.pk:  # Existing proposal
            return self.instance.estado  # Return the existing estado, disallowing changes
        return self.cleaned_data['estado']  # For new proposals, allow state to be set
