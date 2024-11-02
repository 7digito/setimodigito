from django.db import models
from django.utils import timezone
from datetime import timedelta
from clientes.models import Cliente  # Certifique-se de que o caminho está correto

class Proposta(models.Model):
    ESTADOS = [
        ('solicitada', 'Solicitada'),
        ('em_processo', 'Em Processo'),
        ('entregue', 'Entregue'),
        ('aprovada', 'Aprovada'),
        ('sem_resposta', 'Sem Resposta'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='propostas')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='solicitada')
    pdf = models.FileField(upload_to='propostas_pdfs/', blank=True, null=True)

    # New fields for delivery and expiration
    data_entrega = models.DateField(null=True, blank=True)
    validade_em_dias = models.PositiveIntegerField(default=30)  # Default validity period
    data_expiracao = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Set the delivery and expiration dates if the state is changed to 'Entregue'
        if self.estado == 'entregue' and not self.data_entrega:
            self.data_entrega = timezone.now().date()
            self.data_expiracao = self.data_entrega + timedelta(days=self.validade_em_dias)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} - {self.cliente.nome}"
