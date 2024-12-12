from django.contrib import admin
from .models import Tarea
#Importamos la clase Tarea de modelos

# Registramos la Base tareas en el proyecto
admin.site.register(Tarea)