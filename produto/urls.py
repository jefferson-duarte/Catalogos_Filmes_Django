from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoCreate.as_view(), name='cadastro_produto'),
    path('lista/', views.ProdutoLista.as_view(), name='lista_produtos'),
    path('editar/<int:pk>/', views.ProdutoUpdate.as_view(), name='edita_produto'),  # noqa
    path('deletar/<int:pk>/', views.ProdutoDeleta.as_view(), name='deleta_produto'),  # noqa
]
