from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm


class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/'


class ProdutoLista(ListView):
    model = Produto
    queryset = Produto.objects.all().order_by('-pk')

    def get_context_data(self, **produtos):
        context = super().get_context_data(**produtos)
        return context


class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/lista/'


class ProdutoDeleta(DeleteView):
    model = Produto
    success_url = '/lista/'
