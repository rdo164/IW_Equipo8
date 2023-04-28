from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Equipo, Proceso
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    #           referenciar el título de la página
    # context = {'title_page': 'Seleccione una opción:'}
    return render(request, 'index.html')

# muestra los equipos
def index_equipo(request):
	equipos = Equipo.objects.order_by('marca')    
    # context = {'title_page': ' ', 'marca' }
	context = {'lista_equipos': equipos}
	return render(request, 'index_equipo.html', context)
