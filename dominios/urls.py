from django.urls import path
from .views import listar_dominios, adicionar_dominio, editar_dominio, excluir_dominio

urlpatterns = [
    path('', listar_dominios, name='listar_dominios'),
    path('adicionar/', adicionar_dominio, name='adicionar_dominio'),
    path('editar/<int:id>/', editar_dominio, name='editar_dominio'),
    path('excluir/<int:id>/', excluir_dominio, name='excluir_dominio'),
]
