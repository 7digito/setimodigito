from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Tarefa, Trabalho
from .forms import TarefaForm
import json

def listar_tarefas(request):
    tarefas = Tarefa.objects.select_related('trabalho__cliente').all()  # Ensure you're fetching related objects efficiently
    tarefas_por_trabalho = {}

    for tarefa in tarefas:
        trabalho = tarefa.trabalho
        if trabalho not in tarefas_por_trabalho:
            tarefas_por_trabalho[trabalho] = []
        tarefas_por_trabalho[trabalho].append(tarefa)

    context = {
        'tarefas_por_trabalho': tarefas_por_trabalho,
        'search_query': request.GET.get('search', ''),
    }

    return render(request, 'tarefas/listar_tarefas.html', context)  # Altere para o nome do seu template

def tarefas_home(request):
    """View para exibir tarefas em um layout de Kanban, divididas por estado."""
    tarefas_a_fazer = Tarefa.objects.filter(estado='a_fazer')
    tarefas_em_progresso = Tarefa.objects.filter(estado='em_progresso')
    tarefas_concluidas = Tarefa.objects.filter(estado='concluido')

    context = {
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_em_progresso': tarefas_em_progresso,
        'tarefas_concluidas': tarefas_concluidas,
    }

    return render(request, 'tarefas/tarefas.html', context)

def adicionar_tarefa(request):
    """View para adicionar uma nova tarefa."""
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/adicionar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    """View para editar uma tarefa existente."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa editada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def apagar_tarefa(request, tarefa_id):
    """View para excluir uma tarefa."""
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'tarefas/apagar_tarefa.html', {'tarefa': tarefa})

@csrf_exempt
def update_task_status(request):
    """View para atualizar o status de uma tarefa via JSON."""
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        task_id = data.get('task_id')
        new_status = data.get('new_status')

        tarefa = get_object_or_404(Tarefa, id=task_id)
        tarefa.estado = new_status
        tarefa.save()

        return JsonResponse({
            'success': True,
            'message': 'Status atualizado com sucesso'
        })
