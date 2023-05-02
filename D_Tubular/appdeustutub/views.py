from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleado, Equipo, Proceso
from django.shortcuts import get_object_or_404
# Create your views here.

# índice de la página
def index(request):
    #           referenciar el título de la página
    return render(request, 'index.html')

# muestra todos los equipos
def index_equipo(request):
	equipos = Equipo.objects.order_by('marca')    
    #                          titulo de index_equipo
	context = {'title_page': 'Listado de equipos', 'lista_equipos': equipos}
	return render(request, 'index_equipo.html', context)

# devuelve los detalles del equipo solicitado
def show_equipo(request, equipo_id):
    #                  .     
    empleados = Empleado.objects.order_by('proceso')
                          
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    #                               Título de la página
    context = {'equipo': equipo, 'lista_empleados': empleados}
    return render(request, 'detail_equipo.html', context)

# devuelve los procesos
def index_proceso(request):
    #                                     models.py!
    procesos = Proceso.objects.order_by('nombreProceso')
    context = {'title_page': 'Listado de procesos:', 'lista_procesos': procesos}
    return render(request, 'index_proceso.html', context)

# devuelve los detalles del proceso solicitado
def show_proceso(request, proceso_id):
    # para poder mostrar los empleados asociados al proceso 
    empleados = Empleado.objects.order_by('proceso')
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    #                             titulo del html
    context = {'title_page': 'Detalles del proceso','proceso': proceso, 'lista_empleados': empleados}
    #                                               si devuelves más de un context se reformate todo.
    return render (request, 'detail_proceso.html', context)

# devuelve los empleados
def index_empleado(request):
    empleados = Empleado.objects.order_by('nombre')
    context = { 'title_page': 'Listado de empleados:', 'lista_empleados': empleados}
    return render( request, 'index_empleado.html', context)


# devuelve los datos del empleado solicitado
def show_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    context = { 'empleado': empleado }
    return render(request, 'detail_empleado.html', context)

     