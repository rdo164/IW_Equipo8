from django.db import models

# Create your models here.

class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.archivo.name

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_adquisicion = models.DateField()
    fecha_instalacion = models.DateField()
    
    def __str__(self):
        return self.marca
    
class Proceso(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    codOrdenFabricacion = models.IntegerField(default=0)
    codigoProceso = models.IntegerField(default=0)
    nombreProceso = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return self.nombreProceso
    
class Empleado(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre