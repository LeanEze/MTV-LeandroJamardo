from django.db import models
from unittest.util import _MAX_LENGTH

class Familiar(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    DNI = models.IntegerField(max_length=10)
    edad = models.IntegerField(max_length=3)