from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import UsuarioForm


class CadastraUsuario(SuccessMessageMixin, CreateView):
    model = User
    form_class = UsuarioForm
    success_url = '/auth/logar/'
    success_message = "Usuário cadastrado com sucesso!"


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)

        if user:
            login(request, user)
            messages.add_message(
                request,
                constants.SUCCESS,
                f'Usuario "{usuario}" logado com sucesso.'
            )
            return redirect('lista_produtos')

        else:
            messages.add_message(
                request,
                constants.ERROR,
                'Usuário ou senha inválidos.'
            )

            return redirect('logar_usuario')

    return render(request, 'auth/login.html')


def sair(request):
    logout(request)
    return redirect('logar_usuario')
