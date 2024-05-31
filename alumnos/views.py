from django.shortcuts import render
from . models import Alumno, Genero

# Create your views here.

def index(request):
    alumnos = Alumno.objects.all().order_by('apellido_paterno')
    context={'alumnos':alumnos}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno ORDER BY apellido_paterno')
    context={'alumnos':alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)