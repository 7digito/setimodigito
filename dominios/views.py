from django.shortcuts import render, redirect, get_object_or_404
from .models import Dominio, Cliente  # Importando o modelo Cliente
from .forms import DominioForm  # Form para os domínios

# Lista de Domínios
def listar_dominios(request):
    dominios = Dominio.objects.all().order_by('nome')  # Obtendo todos os domínios
    return render(request, 'dominios/listar.html', {'dominios': dominios})

def adicionar_dominio(request):
    if request.method == 'POST':
        form = DominioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dominios')
    else:
        form = DominioForm()
    return render(request, 'dominios/adicionar.html', {'form': form})

# Editar Domínio
def editar_dominio(request, id):
    dominio = get_object_or_404(Dominio, pk=id)  # Aqui está o id
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
