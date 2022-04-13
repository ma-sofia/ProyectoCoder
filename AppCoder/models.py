from django.db import models

# Create your models here.
# esquema de la base de 
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()  
    profesion = models.CharField(max_length=30)

#con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre {self.nombre} - Apellido {self.apellido} - E-mail {self.email} - Profesión {self.profesion}"

class Entregado(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()









