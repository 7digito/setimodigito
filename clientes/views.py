from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.http import JsonResponse
from django.urls import reverse

def listar_clientes(request):
    # Obtenha o parâmetro de pesquisa da URL
    search_query = request.GET.get('search', '')

    # Filtrar os clientes com base na pesquisa
    if search_query:
        clientes = Cliente.objects.filter(nome__icontains=search_query).order_by('nome')
    else:
        clientes = Cliente.objects.all().order_by('nome')

    # Verifica se é uma requisição AJAX e retorna apenas o HTML da lista de clientes
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = ""
        for cliente in clientes:
            editar_url = reverse('editar_cliente', args=[cliente.id])
            detalhes_url = reverse('detalhes_cliente', args=[cliente.id])
            html += f"""
            <tr>
                <td>{cliente.nome}</td>
                <td>{cliente.nif}</td>
                <td>{cliente.email}</td>
                <td>{cliente.telefone}</td>
                <td>
                    <a href="{editar_url}" class="btn btn-sm btn-primary">
                        <i class="bi bi-pencil" style="color: #ffffff;"></i>
                    </a>
                    <a href="#" class="btn btn-sm btn-danger" data-bs-toggle="modal" data-bs-target="#deleteModal"
                       data-nome="{cliente.nome}" data-id="{cliente.id}"
                       onclick="setDeleteData('{cliente.nome}', '{cliente.id}')">
                        <i class="bi bi-trash" style="color: #ffffff;"></i>
                    </a>
                    <a href="{detalhes_url}" class="btn btn-sm btn-warning">
                        <i class="bi bi-info-circle" style="color: #ffffff;"></i>
                    </a>
                </td>
            </tr>
            """
        if not clientes:
            html = "<tr><td colspan='5'>Nenhum cliente encontrado.</td></tr>"
        return JsonResponse({'html': html})

    # Renderiza o template completo em requisições normais
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes, 'search_query': search_query})


def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o cliente no banco de dados
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
        return redirect('listar_clientes')  # Redireciona para a lista de clientes
    # Não é necessário renderizar uma página para confirmação, pois estamos usando um modal

# Nova view para mostrar detalhes de um cliente
def detalhes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)  # Obtém o cliente ou retorna 404 se não encontrado
    return render(request, 'clientes/detalhes_cliente.html', {'cliente': cliente})
