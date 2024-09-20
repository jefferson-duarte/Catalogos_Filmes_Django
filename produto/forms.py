from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = (
            'nome',
            'categoria',
            'valor',
            'quantidade',
            'descricao',
            'data_lancamento',
            'duracao',
            'capa',
        )

        widgets = {
            'data_lancamento': forms.DateInput(attrs={'type': 'date'}),
        }
