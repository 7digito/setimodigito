from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),  # Home page
    path('clientes/', include('clientes.urls')),  # Client-related URLs
    path('tarefas/', include('tarefas.urls')),  # Task-related URLs
    path('dominios/', include('dominios.urls')),  # Domain-related URLs
    path('trabalhos/', include('trabalhos.urls')),  # Include URLs from the 'trabalhos' app
]
