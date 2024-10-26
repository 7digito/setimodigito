from django.db import models
from clientes.models import Cliente  # Importar o modelo Cliente

class Tarefa(models.Model):
    ESTADOS_TAREFA = [
        ('a_fazer', 'A Fazer'),
        ('em_progresso', 'Em Progresso'),
        ('concluido', 'Concluído'),
    ]
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_TAREFA, default='pendente')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.get_estado_display()}"
