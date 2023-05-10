from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {
        "estudiantes/" : [
            {"nombre": "Sofia","apellido":"Lescaffette"},
            {"nombre": "Sofi","apellido":"Lescaffett"},
            {"nombre": "Sofa","apellido":"Lescaffete"},
            {"nombre": "Soia","apellido":"Lescafete"},
        ] 
    }
    http_response = render(
      request=request, 
    template_name='AppCoder/lista_estudiantes.html', 
      context=contexto,
  )
    return http_response

def listar_cursos(request):
    contexto = {
        "cursos/" :[
            {"nombre": "Python","comision":"123"},
            {"nombre": "CSS","comision":"111"},
            {"nombre": "HTML","comision":"222"},
            {"nombre": "C++","comision":"333"},
        ] 
    }
    http_response = render(
      request=request, 
    template_name='AppCoder/lista_cursos.html', 
      context=contexto,
  )
    return http_response