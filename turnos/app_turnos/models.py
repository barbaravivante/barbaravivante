from django.db import models

# Create your models here.
class Turno(models.Model):

    nombre = models.CharField(max_length=40)
    domicilio = models.CharField(max_length=40)

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=40)
    email = models.CharField(max_length=20)

class Profesionales(models.Model):

    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    turno= models.CharField(max_length=40)              