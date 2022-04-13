import re
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario

# Create your views here.
# def curso(request):
#     curso = Curso(nombre= "Desarrollo Web", camada = "11111")

#     curso.save()

#     documento = f"El curso es: {curso.nombre}, la camada: {curso.camada}"

#     return HttpResponse(documento)

# def cursos(request):
#     return render(request, "AppCoder/cursos.html")

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #acá llega toda la info del html
        print(miFormulario)
        
        if miFormulario.is_valid: #si pasó la verificación de django
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre = informacion['curso'], camada = informacion['camada'])
            curso.save()

            return render(request, "AppCoder/inicio.html") #vuelvo al inicio o a donde se desee
    else:
        miFormulario = CursoFormulario() #Formulario vacío para construir el html
    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

# Búsqueda camada
def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")
def buscar(request):
    # respuesta = f"Estoy buscando la camada nro {request.GET['camada'] }"
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada": camada})
    
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(request, "AppCoder/inicio.html", {"respuesta": respuesta})


# PROFESORES
def leerProfesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores
    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST) #acá llega toda la info del html
        print(miFormulario)
        
        if miFormulario.is_valid: #si pasó la verificación de django
            informacion = miFormulario.cleaned_data

            profesor = Profesor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion = informacion['profesion'] )
            profesor.save()

            return render(request, "AppCoder/inicio.html") #vuelvo al inicio o a donde se desee
    else:
        miFormulario = ProfesorFormulario() #Formulario vacío para construir el html
    return render(request, "AppCoder/profesores.html", {"miFormulario": miFormulario})

def eliminarProfesor(request, profesor_nombre):
        
    profesor = Profesor.objects.get(nombre=profesor_nombre)

    profesor.delete()

        #vuelvo al menú
    profesores = Profesor.objects.all()

    contexto = {"profesores": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

# def editarProfesor(request, profesor_nombre):
#     profesor = Profesor.objects.get(nombre=profesor_nombre)

#     if 
                                
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "AppCoder/entregables.html")