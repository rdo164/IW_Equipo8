from django.contrib import admin
# Para poder visualizar las clases de nuestro modelo desde la app de DJango
from .models import Equipo, Proceso, Empleado
admin.site.register(Empleado)
admin.site.register(Equipo)
admin.site.register(Proceso)

# Register your models here.
