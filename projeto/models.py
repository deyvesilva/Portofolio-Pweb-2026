from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    github = models.URLField()
    imagem = models.ImageField(upload_to='projetos/', null=True, blank=True)

    uc = models.ForeignKey('unidadeCurricular.UnidadeCurricular', on_delete=models.CASCADE)

    tecnologias = models.ManyToManyField('tecnologia.Tecnologia', blank=True)
    competencias = models.ManyToManyField('competencia.Competencia', blank=True)

    def __str__(self):
        return self.nome