# tarefas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()  # Pega todas as tarefas
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a nova tarefa
            return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm()
    return render(request, 'tarefas/adicionar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()  # Salva as alterações na tarefa
            return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def apagar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()  # Deleta a tarefa
        return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    return render(request, 'tarefas/apagar_tarefa.html', {'tarefa': tarefa})
