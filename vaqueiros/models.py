from django.db import models

class Vaqueiro(models.Model):
    nome = models.CharField(max_length=50)
    documento = models.CharField(max_length=25, unique=True)
    telefone = models.CharField(max_length=30)
    nome_guerra = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
