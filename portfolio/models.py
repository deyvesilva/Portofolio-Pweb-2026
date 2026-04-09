from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#Licenciatura 
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    universidade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
 #Perfil
class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    bio = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome 
    
#Tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)

    nivel = models.IntegerField(
        choices=[
            (1, '1 - Básico'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5 - Avançado'),
        ],
        help_text="Nível da tecnologia (de 1 a 5)", null=True
    )

    def __str__(self):
        return self.nome
    #Competencia
class Competencia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    #Unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='ucs/', null=True, blank=True)

    licenciatura = models.ForeignKey('licenciatura', on_delete=models.CASCADE)
    
    docente_nome = models.CharField(max_length=100, null = True, blank = True)
    docente_pagina = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.nome
    #Projecto
class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField(null=True,blank=True)
    data_fim = models.DateField(null=True, blank=True)
    github = models.URLField()
    logo = models.ImageField(upload_to='projetos/', null=True, blank=True)

    uc = models.ForeignKey('unidadeCurricular', on_delete=models.CASCADE)

    tecnologias = models.ManyToManyField('tecnologia', blank=True)
    competencias = models.ManyToManyField('competencia', blank=True)

    def __str__(self):
        return self.nome
    #Experiencia
class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    perfil = models.ForeignKey('perfil', on_delete=models.CASCADE)

    tecnologias = models.ManyToManyField('tecnologia', blank=True)
    competencias = models.ManyToManyField('competencia', blank=True)

    def __str__(self):
        return self.empresa
    #Formação
class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    data = models.DateField()
    descricao = models.CharField(max_length=255)

    perfil = models.ForeignKey('perfil', on_delete=models.CASCADE)
    competencias = models.ManyToManyField('competencia', blank=True)

    def __str__(self):
        return self.nome
    #TFC
class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    ano = models.PositiveIntegerField()

    rating = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)],
    help_text="Classificação de 1 a 5",null=True)

    tecnologias = models.ManyToManyField('tecnologia', blank=True)

    def __str__(self):
        return self.titulo
    
    #MakingOf
class MakingOf(models.Model):
    registos = models.ImageField(upload_to='makingof/', null=True, blank=True)

    decisoes = models.CharField(max_length=255)
    erros = models.CharField(max_length=255)
    justificacoes = models.CharField(max_length=255)
    uso_ia = models.CharField(max_length=255)

    projeto = models.ForeignKey('projeto', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"MakingOf {self.id}"