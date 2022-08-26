from django.shortcuts import render
from django.contrib.auth.models import User


def cadastro_usuario(request):
    
    return render(request, 'autenticacao/cadastro_usuario.html')
