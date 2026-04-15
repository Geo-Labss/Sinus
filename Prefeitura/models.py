from django.db import models
from django_cpf_cnpj.fields import CNPJField 
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.br.models import BRPostalCodeField

class Prefeitura(models.Model):
    name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100) # razão social
    trade_name=models.CharField(max_length=100) # nome fantasia
    cnpj = CNPJField(masked=True) #masked.True salva com pontuação
    email = models.EmailField(max_length=254, unique=True)
    cep = BRPostalCodeField()

    def __str__(self):
        return self.name