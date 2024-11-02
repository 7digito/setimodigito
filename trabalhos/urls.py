from django.urls import path
from . import views

app_name = 'trabalhos'
urlpatterns = [
    path('propostas/', views.propostas_list, name='propostas_list'),
    path('propostas/<int:pk>/', views.proposta_detail, name='proposta_detail'),
    path('propostas/new/', views.proposta_create, name='proposta_create'),
    path('propostas/<int:pk>/edit/', views.proposta_update, name='proposta_update'),
    path('propostas/<int:pk>/delete/', views.proposta_delete, name='proposta_delete'),
]
