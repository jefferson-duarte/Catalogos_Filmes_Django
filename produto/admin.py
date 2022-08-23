from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'categoria', 'valor', 'quantidade',
    ]

    list_editable = [
        'categoria', 'valor', 'quantidade',
    ]
