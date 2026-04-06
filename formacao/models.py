from django.db import models

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.CharField(max_length=255)

    perfil = models.ForeignKey('perfil.Perfil', on_delete=models.CASCADE)
    competencias = models.ManyToManyField('competencia.Competencia', blank=True)

    def __str__(self):
        return self.nome