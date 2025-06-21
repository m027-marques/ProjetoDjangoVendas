from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario

def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        # Always handle potential NoneType if data isn't guaranteed
        vendas_str = request.POST.get('vendas')
        meta_str = request.POST.get('meta')

        # Convert to float, providing defaults or raising errors if conversion fails
        # Using a try-except block is more robust for production
        try:
            vendas = float(vendas_str) if vendas_str else 0.0
            meta = float(meta_str) if meta_str else 0.0
        except ValueError:
            # Handle cases where conversion to float fails (e.g., non-numeric input)
            # You might want to add an error message to the user here
            return render(request, 'index.html', {'error_message': 'Por favor, insira valores numéricos válidos para vendas e meta.'})

        funcionario = Funcionario.objects.create(nome=nome, vendas=vendas, meta=meta)
        funcionario.save()
        return redirect('analisar', funcionario_id=funcionario.id)
    return render(request, 'index.html')


def historico(request):
    # FIX: Changed 'object' to 'objects'
    dados = Funcionario.objects.all()
    # FIX: Context should be a dictionary with a key
    return render(request, 'historico.html', {'dados': dados})


# Salvar funcionário (não utilizado diretamente pois já está no index)
def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        vendas = float(request.POST.get('vendas'))
        meta = float(request.POST.get('meta'))
        Funcionario.objects.create(nome=nome, vendas=vendas, meta=meta)
        return redirect('historico')
    return redirect('index')

# Analisar se bateu a meta
def analisar(request, funcionario_id):
    funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
    meta_batida = funcionario.vendas >= funcionario.meta
    bonus = round(funcionario.vendas * 0.15, 2) if meta_batida else 0
    contexto = {
    'nome': funcionario.nome,
    'meta_batida': meta_batida,
    'bonus': bonus
    }
    return render(request, 'resultado.html', contexto)