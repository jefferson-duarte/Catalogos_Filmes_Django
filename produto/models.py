from django.contrib.auth.models import User
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)
    data_lancamento = models.DateField(null=True, blank=True)
    duracao = models.IntegerField(null=True, blank=True)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
