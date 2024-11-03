from django.shortcuts import render, get_object_or_404, redirect
from .models import Trabalho
from .forms import TrabalhoForm

# View para listar todos os trabalhos
def trabalhos_list(request):
    """Renderiza uma lista de todos os trabalhos."""
    trabalhos = Trabalho.objects.all()  # Obtém todos os trabalhos
    return render(request, 'trabalhos/trabalhos_list.html', {'trabalhos': trabalhos})

# View para exibir os detalhes de um trabalho específico
def trabalho_detail(request, pk):
    """Renderiza os detalhes de um trabalho específico pelo seu ID (pk)."""
    trabalho = get_object_or_404(Trabalho, id=pk)  # Obtém o trabalho com o ID fornecido
    return render(request, 'trabalhos/trabalho_detail.html', {'trabalho': trabalho})

# View para criar um novo trabalho
def trabalho_create(request):
    """Renderiza o formulário para criação de um novo trabalho."""
    if request.method == 'POST':
        form = TrabalhoForm(request.POST, request.FILES)  # Cria o formulário com os dados do POST
        if form.is_valid():
            form.save()  # Salva o novo trabalho
            return redirect('trabalhos:trabalhos_list')  # Redireciona para a lista de trabalhos
        else:
            print(form.errors)  # Mostra os erros de validação no console para debug
    else:
        form = TrabalhoForm()  # Cria um formulário vazio
    return render(request, 'trabalhos/trabalho_form.html', {'form': form})

# View para atualizar um trabalho existente
def trabalho_update(request, pk):
    """
    Renderiza o formulário de atualização para um trabalho existente.
    Se a requisição for POST e o formulário for válido, atualiza o trabalho e redireciona para a lista de trabalhos.
    """
    trabalho = get_object_or_404(Trabalho, pk=pk)  # Obtém o trabalho a ser atualizado
    if request.method == 'POST':
        form = TrabalhoForm(request.POST, request.FILES, instance=trabalho)  # Preenche o formulário com os dados existentes
        if form.is_valid():
            form.save()  # Salva as alterações
            return redirect('trabalhos:trabalhos_list')  # Redireciona para a lista de trabalhos
    else:
        form = TrabalhoForm(instance=trabalho)  # Cria o formulário com dados do trabalho
    return render(request, 'trabalhos/trabalho_form.html', {'form': form})

# View para excluir um trabalho
def trabalho_delete(request, pk):
    """
    Renderiza uma confirmação para exclusão de um trabalho.
    Se a requisição for POST, exclui o trabalho e redireciona para a lista de trabalhos.
    """
    trabalho = get_object_or_404(Trabalho, pk=pk)  # Obtém o trabalho a ser excluído
    if request.method == 'POST':
        trabalho.delete()  # Exclui o trabalho
        return redirect('trabalhos:trabalhos_list')  # Redireciona para a lista de trabalhos
    return render(request, 'trabalhos/trabalho_confirm_delete.html', {'trabalho': trabalho})
