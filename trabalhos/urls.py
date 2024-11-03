from django.urls import path
from . import views

app_name = 'trabalhos'  # Nome do aplicativo para o namespace

urlpatterns = [
    path('', views.trabalhos_list, name='trabalhos_list'),  # Lista de trabalhos acessível em /trabalhos/
    path('<int:pk>/', views.trabalho_detail, name='trabalho_detail'),  # Detalhes de um trabalho em /trabalhos/<id>/
    path('new/', views.trabalho_create, name='trabalho_create'),  # Criar novo trabalho em /trabalhos/new/
    path('<int:pk>/edit/', views.trabalho_update, name='trabalho_update'),  # Editar trabalho em /trabalhos/<id>/edit/
    path('<int:pk>/delete/', views.trabalho_delete, name='trabalho_delete'),  # Excluir trabalho em /trabalhos/<id>/delete/
]
