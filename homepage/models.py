from django.db import models
from clientes.models import Cliente  # Importando o modelo Cliente

class Dominio(models.Model):
    ESTADOS = [
        ('ativo', 'Ativo'),
        ('suspenso', 'Suspenso'),
        ('expirado', 'Expirado'),
        ('terminado', 'Terminado'),
    ]
    
    EXTENSAO_OPCOES = [
        ('.com', '.com'),
        ('.pt', '.pt'),
        ('.net', '.net'),
        ('.org', '.org'),
        ('.bizz', '.bizz'),
    ]

    nome = models.CharField(max_length=255)
    extensao = models.CharField(max_length=10, choices=EXTENSAO_OPCOES)  # Adicionando as opções de extensão
    estado = models.CharField(max_length=10, choices=ESTADOS)
    data_criacao = models.DateTimeField()
    data_expiracao = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='dominios')

    def __str__(self):
        return f"{self.nome}.{self.extensao}"
    
    @property
    def antiguidade(self):
        return (datetime.now().date() - self.data_criacao).days // 365  # Calcula a antiguidade em anos
