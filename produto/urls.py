from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoCreate.as_view(), name='cadastro_produto'),
    path('lista/', views.ProdutoLista.as_view(), name='lista_produtos')
]
