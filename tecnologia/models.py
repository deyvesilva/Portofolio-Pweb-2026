from django.db import models

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