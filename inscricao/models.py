from django.db import models
from formapg.models import Formapg
from categoria.models import Categoria
from vaqueiros.models import Vaqueiro
from eventos.models import Evento
from django.db.models.signals import post_save
from django.dispatch import receiver
from corrida.models import Corrida


class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT,  blank=True, null=True)
    senha = models.TextField(max_length=200)
    vaqueiro = models.ForeignKey(Vaqueiro, on_delete=models.PROTECT)
    esteira_vaqueiro = models.CharField(max_length=50)
    representacao = models.CharField(max_length=80)
    cidade= models.CharField(max_length=50)
    cavalo = models.CharField(max_length=40)
    esteira_cavalo = models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    forma_pg = models.ForeignKey(Formapg, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return "%s %s" % (self.vaqueiro, self.cavalo)


class Senha(models.Model):
    senha = models.CharField(max_length=4)
    adquirida = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.senha
