from django.db import models
from localflavor.br.models import BRPostalCodeField

class StatusOcorrencia(models.TextChoices):
    ABERTA = 'AB'
    EM_ANDAMENTO = 'EA'
    FINALIZADA = 'FI'
    CANCELADA = 'CA'

class Occorrencia(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=450)
    cep = BRPostalCodeField()

    status = models.CharField(
        max_length=2,
        choices=StatusOcorrencia.choices,
        default=StatusOcorrencia.EM_ANDAMENTO #Status padrão 
    )

    Usuario = models.ForeignKey('Usuario', on_delete=models.RESTRICT, related_name='occurences')

    Prefeitura = models.ForeignKey('Prefeitura', on_delete=models.RESTRICT, related_name='occurences')

    def __str__(self):
        return f"{self.category} - {self.status}"