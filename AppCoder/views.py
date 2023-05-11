from django.shortcuts import render,redirect
from django.urls import reverse


from AppCoder.models import Estudiante, Curso

def listar_estudiantes(request):
    contexto = {
        "estudiantes" : Estudiante.objects.all(),
    }
    http_response = render(
      request=request, 
    template_name='AppCoder/lista_estudiantes.html', 
      context=contexto,
  )
    return http_response

def listar_cursos(request):
    contexto = {
        "cursos" : Curso.objects.all(),
    }
    http_response = render(
      request=request, 
    template_name='AppCoder/lista_cursos.html', 
      context=contexto,
  )
    return http_response
  
def crear_curso(request):
  contexto = {}
  if request.method == "POST":
    data=request.POST
    nombre=data["nombre"]
    comision=data["comision"]
    curso=Curso.objects.create(nombre=nombre, comision=comision)
    curso.save()
    url_exitosa=reverse('lista_cursos')
    return redirect(url_exitosa)
  else:
    http_response = render(
      request=request, 
    template_name='AppCoder/formulario_1.html', 
      context=contexto,
  )
    return http_response
  
def crear_estudiante(request):
  contexto = {}
  if request.method == "POST":
    data=request.POST
    nombre=data["nombre"]
    apellido=data["apellido"]
    email=data["email"]
    dni=data["dni"]
    curso=Estudiante.objects.create(nombre=nombre, apellido=apellido, email=email,dni=dni)
    curso.save()
    url_exitosa=reverse('lista_estudiantes')
    return redirect(url_exitosa)
  else:
    http_response = render(
      request=request, 
    template_name='AppCoder/formulario_estudiantes.html', 
      context=contexto,
  )
    return http_response
  
def buscar_cursos(request):
  if request.method == "POST":
    data=request.POST
    busqueda=data["busqueda"]
    cursos = Curso.objects.filter(comision__exact=busqueda)
    contexto={
      "cursos":cursos,
    }
  http_response = render(
    request=request, 
    template_name='AppCoder/lista_cursos.html', 
    context=contexto,
  )
  return http_response