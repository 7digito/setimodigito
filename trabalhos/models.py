from django.db import models
from django.utils import timezone
from datetime import timedelta
from clientes.models import Cliente

class Trabalho(models.Model):
    TIPOS_DE_TRABALHO = [
        ('web', 'Web'),
        ('design', 'Design'),
        ('consultoria', 'Consultoria'),
    ]
    
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]
    
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
    teve_proposta = models.BooleanField(default=False)
    numero_proposta = models.CharField(max_length=20, blank=True, null=True)
    pdf_proposta = models.FileField(upload_to='trabalhos_pdfs/', blank=True, null=True)

    data_entrega = models.DateField(null=True, blank=True)
    validade_em_dias = models.PositiveIntegerField(default=30)  # Prazo de validade padrão
    data_expiracao = models.DateField(null=True, blank=True)

    @property
    def data_limite(self):
        """Calcula a data limite com base na data de início e no prazo."""
        if self.data_inicio and self.prazo:
            return self.data_inicio + timedelta(days=self.prazo)
        return None

    def save(self, *args, **kwargs):
        """Salva o trabalho e atualiza a data de entrega e data de expiração, se necessário."""
        if self.estado_trabalho == 'concluido':
            if not self.data_entrega:
                self.data_entrega = timezone.now().date()
            if self.prazo:  # Verifica se o prazo não é None
                self.data_expiracao = self.data_entrega + timedelta(days=self.validade_em_dias)  # Usar validade em dias
        else:
            self.data_entrega = None  # Reseta data de entrega se não está concluído
            self.data_expiracao = None  # Reseta data de expiração se não está concluído

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} - {self.cliente.nome if self.cliente else 'Cliente Desconhecido'}"
