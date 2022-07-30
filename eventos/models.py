from django.db import models
from webvaquejada.settings import DIA_SEMANA


class Evento(models.Model):
    numero = models.PositiveIntegerField(verbose_name='Numero da planilha')
    evento = models.CharField(max_length=50)
    pontuacao_maxima = models.PositiveIntegerField(default=3)
    data_evento = models.DateTimeField(verbose_name="data rodizio")
    dia_semana = models.CharField(choices=DIA_SEMANA, max_length=50,default='---',
                                  verbose_name='Dia da Semana')

    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Rodizio'
        ordering=('numero', )

    def __str__(self) -> str:
        return self.evento
