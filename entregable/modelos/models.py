from django.db import models

# Create your models here.

class Familiares(models.Model):
    name = models.CharField(max_length=40)
    dni = models.IntegerField()
    birth_date = models.DateField()