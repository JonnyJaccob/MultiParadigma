from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255) #varchar
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)