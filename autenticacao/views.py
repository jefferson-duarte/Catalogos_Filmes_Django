from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import UsuarioForm


class CadastraUsuario(CreateView):
    model = User
    form_class = UsuarioForm
    success_url = '/'


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
