from django.db import models

#cria dados com o banco de dados

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    matricula = models.CharField(max_length=100, default=0000)
    curso = models.CharField(max_length=100,default="Vazio")
    periodo = models.CharField(max_length=100, default="Primeiro")


