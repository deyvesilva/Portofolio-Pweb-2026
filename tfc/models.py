from django.db import models

class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    ano = models.IntegerField()
    link = models.URLField(blank=True)

    tecnologias = models.ManyToManyField('tecnologia.Tecnologia', blank=True)

    def __str__(self):
        return self.titulo