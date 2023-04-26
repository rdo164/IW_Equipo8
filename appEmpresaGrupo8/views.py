from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipo, Proceso, Empleado
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def index_equipo(request):
	equipos = Equipo.objects.order_by('marca')
	context = {'lista_equipos': equipos}
	return render(request, 'index_equipo.html', context)

def show_equipo(request, equipo_id):
	equipo = get_object_or_404(Equipo, pk=equipo_id)
	context = {'equipo': equipo }
	return render(request, 'detail_equipo.html', context)

def index_proceso(request):
	procesos = Proceso.objects.order_by('nombreProceso')
	context = {'lista_procesos': procesos}
	return render(request, 'index_proceso.html', context)

def show_proceso(request, proceso_id):
	proceso = get_object_or_404(Proceso, pk=proceso_id)
	context = {'proceso': proceso }
	return render(request, 'detail_proceso.html', context)

def index_empleado(request):
	empleados = Empleado.objects.order_by('nombre')
	context = {'lista_empleados': empleados}
	return render(request, 'index_empleado.html', context)

def show_empleado(request, empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	context = {'empleado': empleado}
	return render(request, 'detail_empleado.html', context)