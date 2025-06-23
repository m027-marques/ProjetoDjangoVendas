#logica das paginas. define os dados que serao exebidos

from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario

#funçao para pag inicial com formulario de cadastro
def index(request):
    if request.method == "POST":
        nome= request.POST.get("nome")
        vendas = float(request.POST.get("vendas"))
        meta = float(request.POST.get("meta"))
        funcionario = (Funcionario.objects.create(nome=nome, vendas=vendas,meta=meta))
        return redirect("analisar", funcionario_id=funcionario.id)
    return render(request, "index.html")

#funçao para pag historico
def historico(request):
    dados = Funcionario.objects.all()
    return render(request,"historico.html", {"dados":dados})

#funçao para pag Salvar # Salvar funcionário (não utilizado diretamente pois já está no index)
def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        vendas = float(request.POST.get('vendas'))
        meta = float(request.POST.get('meta'))
        Funcionario.objects.create(nome=nome, vendas=vendas, meta=meta)
        return redirect('historico.html')
    return redirect('index')

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
