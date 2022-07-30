from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self) -> str:
        return self.nome
