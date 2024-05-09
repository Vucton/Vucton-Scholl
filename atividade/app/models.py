from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    idade = models.IntegerField()
    rg = models.CharField(max_length=18)
