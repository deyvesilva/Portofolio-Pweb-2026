from django.db import models

class MakingOf(models.Model):
    registos = models.ImageField(upload_to='makingof/', null=True, blank=True)

    decisoes = models.CharField(max_length=255)
    erros = models.CharField(max_length=255)
    justificacoes = models.CharField(max_length=255)
    uso_ia = models.CharField(max_length=255)

    projeto = models.ForeignKey('projeto.Projeto', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"MakingOf {self.id}"