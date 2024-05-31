from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)


class Alumno(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno) 

class Ramo(models.Model):
    id_ramo  = models.AutoField(db_column='idRamo', primary_key=True) 
    ramo     = models.CharField(max_length=20, blank=False, null=False)
    creditos = models.IntegerField()
    escuela  = models.CharField(max_length=45)

    def __str__(self):
        return str(self.ramo)

class Seccion(models.Model):
    id_seccion         = models.AutoField(db_column='idSeccion', primary_key=True) 
    codigo_seccion     = models.CharField(max_length=20, blank=False, null=False)
    id_ramo            = models.ForeignKey('Ramo',on_delete=models.CASCADE, db_column='idRamo') 

    def __str__(self):
        return str(self.codigo_seccion)

class AlumnoSeccion(models.Model):
    id_alumnoseccion  = models.AutoField(db_column='idAlumnoSeccion', primary_key=True) 
    id_seccion        = models.ForeignKey('Seccion',on_delete=models.CASCADE, db_column='idSeccion') 
    id_alumno         = models.ForeignKey('Alumno',on_delete=models.CASCADE, db_column='rut') 

    def __str__(self):
        return str(self.id_alumno)+" - "+str(self.id_seccion)