from django.db import models

from django.contrib import admin
# Create your models here.

class Alumno(models.Model):
    nombres =   models.CharField(max_length=50)
    apellidos  =   models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    carnet= models.IntegerField()
    def __str__(self):
        return self.carnet


class Profesor(models.Model):
    nombres =   models.CharField(max_length=50)
    apellidos  =   models.CharField(max_length=50)
    especialidad  =   models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    dpi= models.IntegerField()
    telefono= models.IntegerField()
    direccion= models.CharField(max_length=50)
    def __str__(self):
        return self.dpi

class Materia(models.Model):
    nombre =   models.CharField(max_length=90)
    creditos =   models.IntegerField()
    def __str__(self):
        return self.nombre
