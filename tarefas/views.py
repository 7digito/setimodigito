# tarefas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Tarefa
from .forms import TarefaForm

def listar_tarefas(request):
    # Pega todas as tarefas da base de dados
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def tarefas_home(request):
    # Filtra tarefas por estado
    tarefas_a_fazer = Tarefa.objects.filter(estado='a_fazer')         # Tarefas a fazer
    tarefas_em_progresso = Tarefa.objects.filter(estado='em_progresso')  # Tarefas em progresso
    tarefas_concluidas = Tarefa.objects.filter(estado='concluido')       # Tarefas concluídas
    
    # Prepara o contexto para renderização
    context = {
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_em_progresso': tarefas_em_progresso,
        'tarefas_concluidas': tarefas_concluidas,
    }
    
    return render(request, 'tarefas/tarefas.html', context)

def adicionar_tarefa(request):
    # Adiciona uma nova tarefa
    if request.method == 'POST':
        form = TarefaForm(request.POST)  # Cria um novo formulário com os dados enviados
        if form.is_valid():
            form.save()  # Salva a nova tarefa no banco de dados
            return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm()  # Se não for POST, cria um formulário vazio
    return render(request, 'tarefas/adicionar_tarefa.html', {'form': form})

def editar_tarefa(request, tarefa_id):
    # Edita uma tarefa existente
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)  # Busca a tarefa pelo ID
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)  # Preenche o formulário com os dados da tarefa
        if form.is_valid():
            form.save()  # Salva as alterações na tarefa
            return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    else:
        form = TarefaForm(instance=tarefa)  # Se não for POST, preenche o formulário com a tarefa existente
    return render(request, 'tarefas/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def apagar_tarefa(request, tarefa_id):
    # Deleta uma tarefa existente
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)  # Busca a tarefa pelo ID
    if request.method == 'POST':
        tarefa.delete()  # Deleta a tarefa
        return redirect('listar_tarefas')  # Redireciona para a lista de tarefas
    return render(request, 'tarefas/apagar_tarefa.html', {'tarefa': tarefa})

def update_task_status(request):
    # Atualiza o estado de uma tarefa via AJAX
    if request.method == 'POST':
        task_id = request.POST.get('task_id')  # Obtém o ID da tarefa
        new_status = request.POST.get('new_status')  # Obtém o novo estado

        # Verifica se a tarefa existe
        tarefa = get_object_or_404(Tarefa, id=task_id)
        
        # Atualiza o estado da tarefa
        tarefa.estado = new_status
        tarefa.save()

        return JsonResponse({'new_status': new_status})  # Retorna o novo estado em formato JSON
    return JsonResponse({'error': 'Invalid request'}, status=400)  # Retorna um erro se a requisição não for válida
