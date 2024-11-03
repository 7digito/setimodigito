from django.db import models
from django.utils import timezone
from datetime import timedelta
from clientes.models import Cliente  # Importa o modelo Cliente

class Trabalho(models.Model):
    # Definição das opções para o tipo de trabalho
    TIPOS_DE_TRABALHO = [
        ('web', 'Web'),
        ('design', 'Design'),
        ('consultoria', 'Consultoria'),
    ]
    
    # Definição das opções para prioridade
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    
    # Definição das opções para estado de trabalho
    ESTADOS_DE_TRABALHO = [
        ('standby', 'Standby'),
        ('iniciado', 'Iniciado'),
        ('concluido', 'Concluído'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='trabalhos')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField(blank=True, null=True)
    prazo = models.PositiveIntegerField(blank=True, null=True)  # Prazo em dias
    tipo_trabalho = models.CharField(max_length=20, choices=TIPOS_DE_TRABALHO)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, blank=True, null=True)
    estado_trabalho = models.CharField(max_length=20, choices=ESTADOS_DE_TRABALHO, default='standby')
    teve_proposta = models.BooleanField(default=False, blank=True, null=True)
    numero_proposta = models.CharField(max_length=20, blank=True, null=True)
    pdf_proposta = models.FileField(upload_to='trabalhos_pdfs/', blank=True, null=True)

    data_entrega = models.DateField(null=True, blank=True)
    validade_em_dias = models.PositiveIntegerField(default=30)  # Prazo de validade padrão
    data_expiracao = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para atualizar a data de entrega e 
        calcular a data de expiração quando o estado é 'concluido'.
        """
        if self.estado_trabalho == 'concluido' and not self.data_entrega:
            self.data_entrega = timezone.now().date()
            if self.prazo:  # Verifique se prazo não é None
                self.data_expiracao = self.data_entrega + timedelta(days=self.prazo)  # Usar o novo campo prazo
        super().save(*args, **kwargs)

    def __str__(self):
        """Retorna uma representação em string do objeto Trabalho."""
        return f"{self.titulo} - {self.cliente.nome}"
