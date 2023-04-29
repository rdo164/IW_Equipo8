from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Equipo, Proceso
from django.shortcuts import get_object_or_404
# Create your views here.

# índice de la página
def index(request):
    #           referenciar el título de la página
    # context = {'title_page': 'Seleccione una opción:'}
    return render(request, 'index.html')

# muestra todos los equipos
def index_equipo(request):
	equipos = Equipo.objects.order_by('marca')    
    # context = {'title_page': ' ', 'marca' }
	context = {'title_page': 'Listado de equipos', 'lista_equipos': equipos}
	return render(request, 'index_equipo.html', context)

# devuelve los detalles del equipo solicitado
def show_equipo(request, equipo_id):
    #                  .                                
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    # Título de la página
    context = {'equipo': equipo }
    return render(request, 'detail_equipo.html', context)

# devuelve los procesos
def index_proceso(request):
    #                                     models.py!
    procesos = Proceso.objects.order_by('nombreProceso')
    context = {'lista_procesos': procesos}
    return render(request, 'index_proceso.html', context)

# devuelve los detalles del proceso solicitado
def show_proceso(request, proceso_id):
    proceso= get_object_or_404(Proceso, pk=proceso_id)
    context = {'proceso': proceso }
    return render (request, 'detail_proceso.html', context)

# devuelve los empleados
def index_empleado(request):
    empleados = Empleado.objects.order_by('nombre')
    context = { 'lista_empleados': empleados}
    return render( request, 'index_empleado.html', context)


# devuelve los datos del empleado solicitado
def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    context = { 'empleado': empleado }
    return render(request, 'detail_empleado.html', context)