from django.db import models
from clientes.models import Cliente
from datetime import datetime

class Dominio(models.Model):
    ESTADOS = [
        ('ativo', 'Ativo'),
        ('suspenso', 'Suspenso'),
        ('expirado', 'Expirado'),
        ('terminado', 'Terminado'),
    ]

    EXTENSOES = [
        ('.com', '.com'),
        ('.pt', '.pt'),
        ('.net', '.net'),
        ('.org', '.org'),
        ('.bizz', '.bizz'),
    ]

    nome = models.CharField(max_length=255)
    extensao = models.CharField(max_length=10, choices=EXTENSOES)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    data_criacao = models.DateTimeField()
    data_expiracao = models.DateTimeField()

    # Adicionando um related_name único
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dominios_dominio')

    @property
    def antiguidade(self):
        return (datetime.now().year - self.data_criacao.year)

    def save(self, *args, **kwargs):
        if self.estado == 'ativo':
            now = datetime.now()
            if self.data_criacao.month < now.month or (self.data_criacao.month == now.month and self.data_criacao.day <= now.day):
                self.data_expiracao = self.data_criacao.replace(year=now.year + 1)
            else:
                self.data_expiracao = self.data_criacao.replace(year=now.year)
        super(Dominio, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome}.{self.extensao}"
