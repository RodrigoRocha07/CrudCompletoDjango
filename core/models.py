from django.db import models

#cria dados com o banco de dados

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome