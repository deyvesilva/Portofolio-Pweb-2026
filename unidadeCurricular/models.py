from django.db import models

class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='ucs/', null=True, blank=True)

    licenciatura = models.ForeignKey('licenciatura.Licenciatura', on_delete=models.CASCADE)

    docente_nome = models.CharField(max_length=100, null = True, blank = True)
    docente_pagina = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.nome