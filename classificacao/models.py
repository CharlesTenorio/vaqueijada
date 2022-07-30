from django.db import models

from categoria.models import Categoria

from eventos.models import Evento


class Classificacao(models.Model):
    corrida = models.IntegerField()
    eventos = models.ForeignKey(Evento, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    senha = models.CharField(max_length=10, blank=True, null=True)
    vaqueiro = models.CharField(max_length=40, default='Vaqueiro')
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.vaqueiro)


