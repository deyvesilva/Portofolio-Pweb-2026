from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    origem = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.nome