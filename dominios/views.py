from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Dominio, Cliente
from .forms import DominioForm

# Lista de Domínios
def listar_dominios(request):
    query = request.GET.get('search', '')  # Captura a consulta de pesquisa
    if query:
        # Filtra domínios baseado na pesquisa
        dominios = Dominio.objects.filter(nome__icontains=query).order_by('nome')
    else:
        # Obtém todos os domínios se não houver consulta
        dominios = Dominio.objects.all().order_by('nome')

    return render(request, 'dominios/listar.html', {
        'dominios': dominios,  # Passa todos os domínios para o template
        'search_query': query  # Passa a consulta de pesquisa para o template
    })

# Adicionar Domínio
def adicionar_dominio(request):
    clientes = Cliente.objects.all()  # Carregar todos os clientes
    if request.method == 'POST':
        form = DominioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dominios')
    else:
        form = DominioForm()
    return render(request, 'dominios/adicionar.html', {'form': form, 'clientes': clientes})

# Editar Domínio
def editar_dominio(request, id):
    dominio = get_object_or_404(Dominio, pk=id)  # Obtendo o domínio pelo id
    clientes = Cliente.objects.all()  # Obtendo todos os clientes
    if request.method == 'POST':
        form = DominioForm(request.POST, instance=dominio)
        if form.is_valid():
            form.save()
            return redirect('listar_dominios')
    else:
        form = DominioForm(instance=dominio)
    return render(request, 'dominios/editar.html', {
        'form': form,
        'dominio': dominio,
        'clientes': clientes  # Passando a lista de clientes para o template
    })

# Excluir Domínio
def excluir_dominio(request, dominio_id):
    dominio = get_object_or_404(Dominio, id=dominio_id)
    if request.method == 'POST':
        dominio.delete()
        return redirect('listar_dominios')
    return render(request, 'dominios/excluir.html', {'dominio': dominio})

# Detalhes do Domínio
def detalhes_dominio(request, id):
    dominio = get_object_or_404(Dominio, pk=id)  # Obtém o domínio pelo ID
    return render(request, 'dominios/detalhes.html', {'dominio': dominio})

# Homepage com Domínios categorizados por expiração
def homepage(request):
    # Data atual
    hoje = timezone.now().date()

    # Prazos para categorização
    proximo_mes = hoje + timedelta(days=30)
    proximos_tres_meses = hoje + timedelta(days=90)

    # Filtrando domínios de acordo com a data de expiração
    dominios_proximo_mes = Dominio.objects.filter(data_expiracao__lte=proximo_mes, data_expiracao__gte=hoje)
    dominios_proximos_tres_meses = Dominio.objects.filter(data_expiracao__lte=proximos_tres_meses, data_expiracao__gt=proximo_mes)
    dominios_mais_tarde = Dominio.objects.filter(data_expiracao__gt=proximos_tres_meses)

    context = {
        'dominios_proximo_mes': dominios_proximo_mes,
        'dominios_proximos_tres_meses': dominios_proximos_tres_meses,
        'dominios_mais_tarde': dominios_mais_tarde,
    }
    
    return render(request, 'homepage.html', context)

# Função para listar domínios expirando
def listar_dominios_expirando(request):
    hoje = timezone.now().date()
    proximo_mes = hoje + timedelta(days=30)
    
    # Filtrando domínios que expiram dentro de 30 dias
    dominios_expirando = Dominio.objects.filter(data_expiracao__lte=proximo_mes, data_expiracao__gte=hoje)

    return render(request, 'dominios/expirando.html', {'dominios_expirando': dominios_expirando})
