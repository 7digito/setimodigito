from django.shortcuts import render
from dominios.models import Dominio  # Importando o modelo Dominio da app 'dominios'
from datetime import datetime, timedelta
from tarefas.models import Tarefa


def homepage(request):
    # Define a data para um ano a partir de hoje
    um_ano = datetime.now() + timedelta(days=365)
    
    # Filtra os domínios que vão expirar no próximo ano
    proximos_dominios = Dominio.objects.filter(data_expiracao__lte=um_ano).order_by('data_expiracao')[:5]
    ultimas_tarefas = Tarefa.objects.order_by('-id')[:5]  # Obtém as 5 últimas tarefas

    return render(request, 'homepage/homepage.html', {
        'proximos_dominios': proximos_dominios,
        'ultimas_tarefas' : ultimas_tarefas,
        })
