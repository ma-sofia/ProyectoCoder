from django.contrib import admin

from AppCoder.models import *

# Register your models here.
# user sofipc pass 123
# user nuevoUser pass django123

admin.site.register(Curso)

admin.site.register(Estudiante)

admin.site.register(Profesor)

admin.site.register(Entregado)


