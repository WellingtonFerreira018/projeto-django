from django.shortcuts import render
from .models import Usuario
from .models import Interesse
from PIL import Image
import os

def home(request):    
    return render(request, 'usuarios/home.html')

def usuarios(request):

    #Salvando usuarios
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibir usuarios
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar para pagina de listar usario
    return render(request, 'usuarios/usuarios.html', usuarios)
    
def sobre(request):
    return render(request, 'usuarios/sobre.html')

def interesse(request):
    
    if request.method == 'POST':

        novo_interesse = Interesse()
        novo_interesse.titulo = request.POST.get('titulo')
        novo_interesse.categoria = request.POST.get('categoria')
        novo_interesse.descricao = request.POST.get('descricao')
        novo_interesse.imagem = request.FILES.get('file')
        novo_interesse.save()

    interesses = {
        "interesses": Interesse.objects.all(),
        "image": Interesse.objects.all()
    }

    return render(request, 'usuarios/interesses.html', interesses)