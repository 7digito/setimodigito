from django.db import models
from clientes.models import Cliente  # Importe o modelo Cliente

class Dominio(models.Model):
    ESTADOS = [
        ('ativo', 'Ativo'),
        ('suspenso', 'Suspenso'),
        ('expirado', 'Expirado'),
        ('terminado', 'Terminado'),
    ]

    nome = models.CharField(max_length=255)
    extensao = models.CharField(max_length=10)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    data_criacao = models.DateTimeField(auto_now_add=True)  # Este campo é criado automaticamente
    data_expiracao = models.DateTimeField()

    # Adicionando o campo cliente como ForeignKey
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dominios')

    def __str__(self):
        return f"{self.nome}.{self.extensao}"
