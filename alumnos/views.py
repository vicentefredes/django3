from django.shortcuts import render, redirect
from .models import Alumno, Genero, Ramo, Seccion

from .forms import RamoForm, SeccionForm

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
        alumnos = Alumno.objects.all().order_by('apellido_paterno')
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

        if alumno.id_genero.genero == "Masculino":
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminado"
        else:
            mensaje = f"{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno} ha sido eliminada"

        alumnos = Alumno.objects.all().order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    
    except:
        mensaje = f"ERROR: el rut {pk} no existe"
        alumnos = Alumno.objects.all().order_by('apellido_paterno')
        context = {'alumnos': alumnos, 'mensaje': mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    

def crud_ramos(request):
    ramos = Ramo.objects.all().order_by('escuela', 'ramo')
    context = {'ramos': ramos}
    return render(request, 'alumnos/ramos_list.html', context)


def ramosAdd(request):
    context = {}

    if request.method == "POST":
        form = RamoForm(request.POST)

        if form.is_valid:
            form.save()

            #limpiando form
            form=RamoForm()

            mensaje = f"El ramo ha sido agregado"

            context = {'mensaje':mensaje, 'form':form}
            return render(request, 'alumnos/ramos_add.html', context)
        else:
            print(form.errors)
            
    else:
        form = RamoForm()
        context = {'form':form}
        return render(request, 'alumnos/ramos_add.html', context)

def ramos_del(request, pk):
    errores = []

    ramos = Ramo.objects.all().order_by('escuela', 'ramo')

    try:
        ramo = Ramo.objects.get(id_ramo=pk)

        context = {}

        if ramo:
            ramo.delete()
            mensaje = f"El ramo {ramo.ramo} ha sido eliminado"
            context = {'ramos':ramos, 'mensaje':mensaje, 'errores':errores}
            return render(request, 'alumnos/ramos_list.html', context)
    
    except:
        ramos = Ramo.objects.all().order_by('escuela', 'ramo')
        mensaje = "ERROR: el id no existe"
        context = {'ramos': ramos, 'mensaje': mensaje}
        return render(request, 'alumnos/ramos_list.html', context)
    

def ramos_edit(request, pk):

    try:
        ramo = Ramo.objects.get(id_ramo=pk)

        context = {}

        if ramo:
            if request.method == "POST":
                form = RamoForm(request.POST, instance=ramo)
                form.save()
                mensaje = f"Los datos del ramo han sido actualizados"
                context = {'ramo':ramo, 'mensaje':mensaje, 'form':form}
                return render(request, 'alumnos/ramos_edit.html', context)
            
            else:
                form = RamoForm(instance=ramo)
                mensaje = ""
                context = {'ramo':ramo, 'mensaje':mensaje, 'form':form}
                return render(request, 'alumnos/ramos_edit.html', context)
        
    except:
        ramos = Ramo.objects.all().order_by('escuela', 'ramo')
        mensaje = "ERROR: el id no existe"
        context = {'ramos': ramos, 'mensaje': mensaje}
        return render(request, 'alumnos/ramos_list.html', context)
    


def crud_secciones(request):
    secciones = Seccion.objects.all().order_by('id_ramo', 'codigo_seccion')
    context = {'secciones': secciones}
    return render(request, 'alumnos/secciones_list.html', context)


def seccionesAdd(request):
    context = {}

    if request.method == "POST":
        form = SeccionForm(request.POST)

        if form.is_valid:
            form.save()

            #limpiando form
            form=SeccionForm()

            mensaje = f"La seccion ha sido agregada"

            context = {'mensaje':mensaje, 'form':form}
            return render(request, 'alumnos/secciones_add.html', context)
        else:
            print(form.errors)
            
    else:
        form = SeccionForm()
        context = {'form':form}
        return render(request, 'alumnos/secciones_add.html', context)

def secciones_del(request, pk):
    errores = []

    secciones = Seccion.objects.all().order_by('id_ramo', 'codigo_seccion')

    try:
        seccion = Seccion.objects.get(id_seccion=pk)

        context = {}

        if seccion:
            seccion.delete()
            mensaje = f"La sección {seccion.codigo_seccion} ha sido eliminada"
            context = {'secciones':secciones, 'mensaje':mensaje, 'errores':errores}
            return render(request, 'alumnos/secciones_list.html', context)
    
    except:
        secciones = Seccion.objects.all().order_by('id_ramo', 'codigo_seccion')
        mensaje = "ERROR: el id no existe"
        context = {'secciones': secciones, 'mensaje': mensaje}
        return render(request, 'alumnos/secciones_list.html', context)
    

def secciones_edit(request, pk):

    try:
        seccion = Seccion.objects.get(id_seccion=pk)

        context = {}

        if seccion:
            if request.method == "POST":
                form = SeccionForm(request.POST, instance=seccion)
                form.save()
                mensaje = f"Los datos de la seccion han sido actualizados"
                context = {'seccion':seccion, 'mensaje':mensaje, 'form':form}
                return render(request, 'alumnos/secciones_edit.html', context)
            
            else:
                form = SeccionForm(instance=seccion)
                mensaje = ""
                context = {'seccion':seccion, 'mensaje':mensaje, 'form':form}
                return render(request, 'alumnos/secciones_edit.html', context)
        
    except:
        secciones = Seccion.objects.all().order_by('id_ramo', 'codigo_seccion')
        mensaje = "ERROR: el id no existe"
        context = {'secciones': secciones, 'mensaje': mensaje}
        return render(request, 'alumnos/secciones_list.html', context)
