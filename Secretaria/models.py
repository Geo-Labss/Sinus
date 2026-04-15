from django.db import models
from django_cpf_cnpj.fields import CNPJField 
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.br.models import BRPostalCodeField

class Secretaria(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(region='BR')
    cep = BRPostalCodeField()

    def __str__(self):
        return self.name