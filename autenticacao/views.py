from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import UsuarioForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants


class CadastraUsuario(SuccessMessageMixin, CreateView):
    model = User
    form_class = UsuarioForm
    success_url = '/'


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = authenticate(request, username=usuario, password=senha)

        if not user:
            messages.add_message(
                request,
                constants.ERROR,
                'Usuário ou senha inválidos.'
            )
            return redirect('logar_usuario')
        else:
            login(request, user)
            return redirect('lista_produtos')

    return render(request, 'auth/login.html')
