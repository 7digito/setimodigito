from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm
import json

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def tarefas_home(request):
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
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'tarefas/apagar_tarefa.html', {'tarefa': tarefa})

def update_task_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_id = data.get('task_id')
            new_status = data.get('new_status')

            tarefa = get_object_or_404(Tarefa, id=task_id)
            tarefa.estado = new_status
            tarefa.save()

            return JsonResponse({'new_status': new_status})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
