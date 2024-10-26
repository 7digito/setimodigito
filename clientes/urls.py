from django.urls import path
from .views import listar_clientes, adicionar_cliente, editar_cliente, apagar_cliente, detalhes_cliente  # Importar a nova view

urlpatterns = [
    path('', listar_clientes, name='listar_clientes'),  # URL para listar clientes
    path('adicionar/', adicionar_cliente, name='adicionar_cliente'),  # URL para adicionar cliente
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),  # URL para editar cliente
    path('apagar/<int:cliente_id>/', apagar_cliente, name='apagar_cliente'),  # URL para apagar cliente
    path('detalhes/<int:cliente_id>/', detalhes_cliente, name='detalhes_cliente'),  # URL para detalhes do cliente
]