from django.views.generic import CreateView
from .models import Produto
from .forms import ProdutoForm


class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/'
