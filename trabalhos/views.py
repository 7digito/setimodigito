from django.shortcuts import render, get_object_or_404, redirect
from .models import Proposta
from .forms import PropostaForm

# View para listar todas as propostas
def propostas_list(request):
    """
    Exibe uma lista de todas as propostas, com possibilidade de pesquisa.
    """
    propostas = Proposta.objects.all()  # Obtém todas as propostas
    return render(request, 'trabalhos/propostas_list.html', {'propostas': propostas})

# View para exibir os detalhes de uma proposta específica
def proposta_detail(request, pk):
    """
    Exibe os detalhes de uma proposta específica, com visualização de campos somente leitura.
    """
    proposta = get_object_or_404(Proposta, id=pk)  # Carrega a proposta existente
    context = {
        'proposta': proposta,
    }
    return render(request, 'trabalhos/proposta_detail.html', context)

# View para criar uma nova proposta
def proposta_create(request):
    """
    Cria uma nova proposta. Se o método for POST, valida e salva o formulário.
    """
    if request.method == 'POST':
        form = PropostaForm(request.POST, request.FILES)  # Cria o formulário com os dados recebidos
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva a nova proposta no banco de dados
            return redirect('trabalhos:propostas_list')  # Redireciona para a lista de propostas
    else:
        form = PropostaForm()  # Cria um formulário vazio se não for um POST

    return render(request, 'trabalhos/proposta_form.html', {'form': form})

# View para atualizar uma proposta existente
def proposta_update(request, pk):
    """
    Atualiza uma proposta existente. Se o método for POST, valida e salva as alterações.
    """
    proposta = get_object_or_404(Proposta, pk=pk)  # Obtém a proposta a ser atualizada
    if request.method == 'POST':
        form = PropostaForm(request.POST, request.FILES, instance=proposta)  # Cria o formulário com os dados da proposta
        if form.is_valid():  # Verifica se o formulário é válido
            # Check if state is being changed to 'entregue'
            if 'estado' in form.cleaned_data and form.cleaned_data['estado'] == 'entregue':
                proposta.save()  # Save the proposal first to update entrega date
            form.save()  # Salva as alterações no banco de dados
            return redirect('trabalhos:propostas_list')  # Redireciona para a lista de propostas
    else:
        form = PropostaForm(instance=proposta)  # Carrega o formulário com os dados da proposta existente

    return render(request, 'trabalhos/proposta_form.html', {'form': form})

# View para excluir uma proposta
def proposta_delete(request, pk):
    """
    Exclui uma proposta após confirmação. Se o método for POST, realiza a exclusão.
    """
    proposta = get_object_or_404(Proposta, pk=pk)  # Obtém a proposta a ser excluída
    if request.method == 'POST':
        proposta.delete()  # Exclui a proposta do banco de dados
        return redirect('trabalhos:propostas_list')  # Redireciona para a lista de propostas
    return render(request, 'trabalhos/proposta_confirm_delete.html', {'proposta': proposta})
