from django.urls import path
from .views import (
    listar_dominios, 
    adicionar_dominio, 
    editar_dominio, 
    excluir_dominio,
    listar_dominios_expirando,
    detalhes_dominio  # Importando a nova view
)

urlpatterns = [
    path('', listar_dominios, name='listar_dominios'),
    path('adicionar/', adicionar_dominio, name='adicionar_dominio'),
    path('editar/<int:id>/', editar_dominio, name='editar_dominio'),
    path('excluir/<int:dominio_id>/', excluir_dominio, name='excluir_dominio'),  # Corrigido para 'dominio_id'
    path('expirando/', listar_dominios_expirando, name='listar_dominios_expirando'),
    path('detalhes/<int:id>/', detalhes_dominio, name='detalhes_dominio'),  # Adicionando a URL de detalhes
]