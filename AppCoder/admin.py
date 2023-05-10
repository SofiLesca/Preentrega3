from django.contrib import admin

from AppCoder.models import Curso, Estudiante, Entregable, Profesor

admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)