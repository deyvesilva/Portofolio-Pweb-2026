from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    bio = models.CharField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.nome