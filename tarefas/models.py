from django.db import models
from trabalhos.models import Trabalho  # Importar o modelo Trabalho

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

    trabalho = models.ForeignKey(Trabalho, on_delete=models.CASCADE, related_name="tarefas")
    descricao = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS_TAREFA, default='a_fazer')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.get_estado_display()}"
