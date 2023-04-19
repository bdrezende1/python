from django.db import models

# Create your models here.
class Produtos(models.Model):
    categoria = models.CharField(max_length=30)
    produto = models.CharField(max_length=255)
    quantidade = models.IntegerField()