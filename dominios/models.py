from django.db import models

class Dominio(models.Model):
    ESTADOS = [
        ('ativo', 'Ativo'),
        ('suspenso', 'Suspenso'),
        ('expirado', 'Expirado'),
        ('terminado', 'Terminado'),
    ]

    nome = models.CharField(max_length=255)
    extensao = models.CharField(max_length=10)  # Ex: .com, .net
    estado = models.CharField(max_length=10, choices=ESTADOS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_expiracao = models.DateField()

    def __str__(self):
        return f"{self.nome}{self.extensao} ({self.estado})"
