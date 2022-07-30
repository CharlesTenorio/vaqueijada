from django.db import models

class Formapg(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nome
