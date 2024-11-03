from django.contrib import admin
from .models import Trabalho

@admin.register(Trabalho)
class TrabalhoAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('titulo', 'cliente', 'tipo_trabalho', 'prioridade', 'estado_trabalho', 'data_inicio', 'prazo', 'data_entrega', 'data_expiracao')
    
    # Fields to search for in the admin list view
    search_fields = ('titulo', 'cliente__nome', 'numero_proposta')
    
    # Filters for easier navigation
    list_filter = ('tipo_trabalho', 'prioridade', 'estado_trabalho', 'data_inicio', 'prazo')

    # Display PDF link in detail view if available
    readonly_fields = ('pdf_proposta',)

    # Function to display PDF link in list view if exists
    def pdf_link(self, obj):
        if obj.pdf_proposta:
            return format_html('<a href="{}" target="_blank">Ver PDF</a>', obj.pdf_proposta.url)
        return "Nenhum PDF disponível"
    pdf_link.short_description = "PDF Proposta"
    
    # Optional: Adding ordering by start date and deadline
    ordering = ('data_inicio', 'prazo')
