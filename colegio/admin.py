from django.contrib import admin
from colegio.models import Materia, GradoAdmin, Grado, MateriaAdmin
# Register your models here.
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
