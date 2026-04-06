from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    ano = models.IntegerField()
    link = models.URLField(blank=True)
    ano = models.PositiveIntegerField()

    rating = models.IntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)],
    help_text="Classificação de 1 a 5"
)

    tecnologias = models.ManyToManyField('tecnologia.Tecnologia', blank=True)

    def __str__(self):
        return self.titulo