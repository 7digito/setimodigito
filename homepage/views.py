from django.shortcuts import render
from dominios.models import Dominio
from datetime import datetime, timedelta
from tarefas.models import Tarefa

def homepage(request):
    # Define a data para um ano a partir de hoje
    um_ano = datetime.now() + timedelta(days=365)
    
    # Filtra os domínios que vão expirar no próximo ano
    proximos_dominios = Dominio.objects.filter(data_expiracao__lte=um_ano).order_by('data_expiracao')[:5]

    # Filtra as tarefas por estado
    tarefas_a_fazer = Tarefa.objects.filter(estado='a_fazer').order_by('-id')[:5]
    tarefas_em_progresso = Tarefa.objects.filter(estado='em_progresso').order_by('-id')[:5]
    tarefas_concluidas = Tarefa.objects.filter(estado='concluido').order_by('-id')[:5]

    return render(request, 'homepage/homepage.html', {
        'proximos_dominios': proximos_dominios,
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_em_progresso': tarefas_em_progresso,
        'tarefas_concluidas': tarefas_concluidas,
    })
