from django.db import models

class Parque(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=25, unique=True)
    telefone = models.CharField(max_length=30)
    contato = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome