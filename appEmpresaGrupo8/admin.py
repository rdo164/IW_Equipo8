from django.contrib import admin
from .models import Equipo, Proceso, Empleado

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Proceso)
admin.site.register(Empleado)