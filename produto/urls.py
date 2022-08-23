from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoCreate.as_view(), name='index'),
]
