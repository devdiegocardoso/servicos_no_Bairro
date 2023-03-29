from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    servico_nome = models.CharField(max_length=200,verbose_name='Serviço',unique=True)
    def __str__(self) -> str:
        return self.servico_nome

class Subcategoria(models.Model):
    subcategoria_nome = models.CharField(max_length=200,verbose_name='Nome da Subcategoria',unique=True)
    servico = models.ForeignKey(Servico,on_delete=models.CASCADE,related_name='subcategorias',related_query_name='subcategoria')
    def __str__(self) -> str:
        return self.subcategoria_nome

class Bairro(models.Model):
    bairro_nome = models.CharField(max_length=200,verbose_name='Nome do Bairro')
    def __str__(self) -> str:
        return self.bairro_nome

class Prestador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prestadores', related_query_name='prestador',blank=True)
    prestador_nome = models.CharField(max_length=200,verbose_name='Nome do Prestador')
    prestador_sobrenome = models.CharField(max_length=200,verbose_name='Sobrenome do Prestador')
    prestador_telefone = models.CharField(max_length=200,verbose_name='Telefone do Prestador')
    servicos = models.ManyToManyField(Subcategoria,related_name='prestadores',related_query_name='prestador',verbose_name='Serviços Prestados',blank=True)
    bairros = models.ManyToManyField(Bairro,related_name='prestadores',related_query_name='prestador',verbose_name='Bairros Atendidos',blank=True)
    def __str__(self) -> str:
        return self.prestador_nome + ' ' + self.prestador_sobrenome

    class Meta:
        verbose_name_plural = "prestadores"