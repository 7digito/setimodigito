from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Incluindo as URLs da app "homepage" como página inicial
    path('clientes/', include('clientes.urls')),  # URLs da app clientes
    path('tarefas/', include('tarefas.urls')),  # URLs da app tarefas
    path('dominios/', include('dominios.urls')),  # Incluindo as URLs da app dominios
]