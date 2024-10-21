from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404    
from .models import Cliente
from .forms import ClienteForm

def listar_clientes(request):
    clientes = Cliente.objects.all()  # Query para buscar todos os clientes
    paginator = Paginator(clientes, 10)  # Mostra 10 clientes por página

    page_number = request.GET.get('page')  # Obtém o número da página atual
    page_obj = paginator.get_page(page_number)  # Obtém os dados da página atual

    return render(request, 'clientes/listar_clientes.html', {'page_obj': page_obj})


def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Isso salvará o cliente no banco de dados
            return redirect('listar_clientes')  # Redireciona após salvar
    else:
        form = ClienteForm()  # Formulário vazio para GET

    return render(request, 'clientes/adicionar_cliente.html', {'form': form})

# View para editar um cliente
def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

# View para apagar um cliente
def apagar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/apagar_cliente.html', {'cliente': cliente})
