from django.contrib.messages.views import SuccessMessageMixin
from django.forms import BaseForm
from django.http.response import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProdutoForm
from .models import Produto


class ProdutoCreate(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/cadastro/'

    def get_success_message(self, cleaned_data):
        return f'Filme "{self.object.nome}" foi criado com sucesso!'

    def form_valid(self, form: BaseForm) -> HttpResponse:
        form.instance.user = self.request.user

        return super().form_valid(form)


class ProdutoLista(ListView):
    model = Produto
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        qs = Produto.objects.filter(user=user)

        return qs


class ProdutoUpdate(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = '/'
    success_message = 'Filme %(nome)s foi alterado com sucesso!'


class ProdutoDeleta(SuccessMessageMixin, DeleteView):
    model = Produto
    success_url = '/'
    success_message = 'Filme excluído com sucesso!'
