# tarefas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),  # URL para listar tarefas
    path('tarefas/adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),  # URL para adicionar uma nova tarefa
    path('tarefas/editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),  # URL para editar uma tarefa
    path('tarefas/apagar/<int:tarefa_id>/', views.apagar_tarefa, name='apagar_tarefa'),  # URL para apagar uma tarefa
    path('tarefas/home/', views.tarefas_home, name='tarefas_home'),  # URL para a página inicial de tarefas
    path('update-task-status/', views.update_task_status, name='update_task_status'),  # URL para atualizar o estado da tarefa
]
