from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=80) #equivalente de str
    comision = models.IntegerField()  #equivalente a int
    
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=80)
    email = models.EmailField()
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField()
    profesion = models.CharField(max_length=130)
    bio = models.TextField()
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=260)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False) #Equivalente a Bool (osea true o false)

    
    
