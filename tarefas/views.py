from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm
import json

def listar_tarefas(request):
    search_query = request.GET.get('search', '')
    tarefas = Tarefa.objects.all()
    
    if search_query:
        tarefas = tarefas.filter(descricao__icontains=search_query)

    return render(request, 'tarefas/listar_tarefas.html', {
        'tarefas': tarefas,
        'search_query': search_query
    })


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

@csrf_exempt  # Adicione isso temporariamente para testar se é um problema de CSRF
def update_task_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Decode o body primeiro
            task_id = data.get('task_id')
            new_status = data.get('new_status')
            
            print(f"Dados recebidos: {data}")  # Para debug
            
            if not task_id or not new_status:
                return JsonResponse({
                    'error': 'Task ID and new status are required'
                }, status=400)

            tarefa = Tarefa.objects.get(id=task_id)
            tarefa.estado = new_status
            tarefa.save()

            return JsonResponse({
                'success': True,
                'message': 'Status atualizado com sucesso'
            })

        except json.JSONDecodeError as e:
            print(f"Erro de JSON: {str(e)}")  # Para debug
            return JsonResponse({
                'error': f'Invalid JSON: {str(e)}'
            }, status=400)
        except Exception as e:
            print(f"Erro: {str(e)}")  # Para debug
            return JsonResponse({
                'error': str(e)
            }, status=500)

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)