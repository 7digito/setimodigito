from django.contrib import admin
from .models import Proposta

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'prazo', 'estado', 'data_criacao')
    search_fields = ('titulo', 'cliente__nome')
    list_filter = ('estado', 'prazo')
