from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/apagar/<int:cliente_id>/', views.apagar_cliente, name='apagar_cliente'),
]
