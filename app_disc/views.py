from django.shortcuts import render
from .models import Interesse, Categoria

def home(request):    
    return render(request, 'home.html')
    
def sobre(request):
    return render(request, 'sobre.html')

def interesse(request):
    
    if request.method == 'POST':
        novo_interesse = Interesse()
        nova_categoria = Categoria()

        novo_interesse.titulo = request.POST.get('titulo')
        if novo_interesse.titulo:
            novo_interesse.titulo = request.POST.get('titulo')
            novo_interesse.descricao = request.POST.get('descricao')
            tipoCategoria = request.POST.get('categoria')

            categoria = Categoria.objects.filter(id=tipoCategoria)
            novo_interesse.categoria = categoria[0]
            novo_interesse.cat = categoria[0]
            novo_interesse.imagem = request.FILES.get('file')
            novo_interesse.save()

        else:
            nova_categoria.categoria = request.POST.get('nome_cat')
            nova_categoria.descricacao = request.POST.get('descricao_cat')
            nova_categoria.save()

    interesses = {
        "interesses": Interesse.objects.all(),
        "categorias": Categoria.objects.all(),
    }

    return render(request, 'interesses.html', interesses)
