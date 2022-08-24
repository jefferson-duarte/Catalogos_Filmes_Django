from django.views.generic import CreateView, ListView
from .models import Produto
from .forms import ProdutoForm


class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/'


class ProdutoLista(ListView):
    model = Produto

    def get_context_data(self, **produtos):
        context = super().get_context_data(**produtos)
        return context
