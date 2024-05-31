from django.contrib import admin
from .models import Genero, Alumno, Ramo, Seccion, AlumnoSeccion

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Ramo)
admin.site.register(Seccion)
admin.site.register(AlumnoSeccion)