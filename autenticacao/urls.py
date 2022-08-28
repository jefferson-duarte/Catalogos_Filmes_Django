from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.CadastraUsuario.as_view(), name='cadastro_usuario'),
    path('logar/', views.logar, name='logar_usuario'),
]
