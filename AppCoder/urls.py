from django.urls import path
from AppCoder import views

urlpatterns = [
    # path('AppCoder/', include('AppCoder.urls')),
    path('', views.inicio, name="Inicio"),
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name = "Entregables"),
    path('cursoFormulario', views.cursoFormulario, name="cursoFormulario"),
    path('leerProfesores', views.leerProfesores, name="leerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
]