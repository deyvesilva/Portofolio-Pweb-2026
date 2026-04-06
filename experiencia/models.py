from django.db import models

class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    perfil = models.ForeignKey('perfil.Perfil', on_delete=models.CASCADE)

    tecnologias = models.ManyToManyField('tecnologia.Tecnologia', blank=True)
    competencias = models.ManyToManyField('competencia.Competencia', blank=True)

    def __str__(self):
        return self.empresa