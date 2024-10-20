from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models

class Cliente(models.Model):
    # id = models.CharField(primary_key=True, max_length=10)
    nome = models.CharField(max_length=255)
    nif = models.CharField(max_length=9, verbose_name='Número de Identificação Fiscal')
    morada = models.CharField(max_length=255, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    localidade = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    cliente_desde = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

