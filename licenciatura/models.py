from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    universidade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome