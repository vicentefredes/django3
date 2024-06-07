from django.shortcuts import render, redirect
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

def crud(request):
    alumnos = Alumno.objects.all().order_by('apellido_paterno')
    context = {'alumnos':alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"
        
        objGenero = Genero.objects.get(id_genero=genero)

        obj = Alumno.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=apaterno,
            apellido_materno=amaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero, # Asociar el genero correctamente
            telefono=telefono,
            email=email,
            direccion=direccion,
            activo=activo
            )

        obj.save()

        if objGenero.genero == 'Masculino':
            mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregado exitosamente"
        else:
            mensaje = f"{nombre} {apaterno} {amaterno} ha sido agregada exitosamente"

        context = {'mensaje': mensaje}

        #return redirect('crud')
        return render(request, 'alumnos/alumnos_add.html', context)
    
def alumnos_findEdit(request, pk):

    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context = {'alumno':alumno, 'generos':generos}

        if alumno:
            return render(request, 'alumnos/alumnos_edit.html', context)
        else:
            mensaje = f"ERROR: el rut {pk} no existe"
            context = {'mensaje': mensaje}
            return render(request, 'alumnos/alumnos_list.html', context)


def alumnosUpdate(request):
    if request.method != "POST":
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos}
        return render(request, 'alumnos/alumnos_list.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apaterno = request.POST["apaterno"]
        amaterno = request.POST["amaterno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"
        
        objGenero = Genero.objects.get(id_genero = genero)

        alumno = Alumno()

        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=apaterno
        alumno.apellido_materno=amaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=activo

        alumno.save()
    
        mensaje = f"Los datos de {nombre} {apaterno} {amaterno} han sido actualizados exitosamente"

        generos = Genero.objects.all()

        context = {'mensaje': mensaje, 'generos':generos, 'alumno':alumno}

        #return redirect('crud')
        return render(request, 'alumnos/alumnos_edit.html', context)



def alumnos_del(request, pk):
    context = {}

    try:
        alumno = Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminado"
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        alumnos = Alumno.objects.all()
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)