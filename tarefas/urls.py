from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('tarefas/adicionar/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('tarefas/editar/<int:tarefa_id>/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/apagar/<int:tarefa_id>/', views.apagar_tarefa, name='apagar_tarefa'),
    path('tarefas/home/', views.tarefas_home, name='tarefas_home'),
    path('update-task-status/', views.update_task_status, name='update_task_status'),
]
