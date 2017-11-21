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
    apellidos  =   models.CharField(max_length=70)
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
    #profesores   = models.ManyToManyField(Profesor, through='Imparte')
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre =   models.CharField(max_length=90)
    seccion =   models.CharField(max_length=10)
    materias   = models.ManyToManyField(Materia, through='Pertenece')
    def __str__(self):
        return self.nombre


#class Imparte (models.Model):
#    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
#    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class Pertenece (models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class PerteneceInLine(admin.TabularInline):
    model = Pertenece
    extra = 1

class GradoAdmin(admin.ModelAdmin):
    inlines = (PerteneceInLine,)


class MateriaAdmin (admin.ModelAdmin):
    inlines = (PerteneceInLine,)
