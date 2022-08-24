from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm
from django.contrib.messages.views import SuccessMessageMixin


class ProdutoCreate(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/'
    success_message = 'Filme %(nome)s foi criado com sucesso!'


class ProdutoLista(ListView):
    model = Produto
    queryset = Produto.objects.all().order_by('-pk')

    def get_context_data(self, **produtos):
        context = super().get_context_data(**produtos)
        return context


class ProdutoUpdate(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/lista/'
    success_message = 'Filme %(nome)s foi alterado com sucesso!'


class ProdutoDeleta(SuccessMessageMixin, DeleteView):
    model = Produto
    success_url = '/lista/'
    success_message = 'Filme excluído com sucesso!'
