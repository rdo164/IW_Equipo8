from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Empleado, Equipo, Proceso
from django.shortcuts import get_object_or_404
from django import forms
from .forms import EmpleadoForm, EquipoForm, ProcesoForm
from django.urls import reverse_lazy

# Create your views here.

# índice de la página
def index(request):
    #           referenciar el título de la página
    # context = {'title_page': 'Seleccione una opción:'}
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
    procesos = Proceso.objects.order_by('nombreProceso')
    context = {'lista_procesos': procesos}
    return render(request, 'index_proceso.html', context)

# devuelve los detalles del proceso solicitado
def show_proceso(request, proceso_id):
    # para poder mostrar los empleados asociados al proceso 
    empleados = Empleado.objects.order_by('proceso')
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    context = {'proceso': proceso, 'lista_empleados': empleados}
    #                                               si devuelves más de un context se reformate todo.
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

# Métodos para añadir empleados, procesos y equipos:

def add_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save()
            return redirect('index_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'add_empleado.html', {'form': form})

def add_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_equipo')
    else:
        form = EquipoForm()
    return render(request, 'add_equipo.html', {'form': form})

def add_proceso(request):
    if request.method == 'POST':
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_proceso')
    else:
        form = ProcesoForm()
    return render(request, 'add_proceso.html', {'form': form})

# Borrar creaciones anteriores:

def borrar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    if request.method == 'POST':
        proceso.delete()
        return redirect('index_proceso')
    return render(request, 'confirmar_borrar_proceso.html', {'proceso': proceso})

def borrar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('index_equipo')
    return render(request, 'confirmar_borrar_equipo.html', {'equipo': equipo})

# Modificar creaciones anteriores:

def modificar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('detail_equipo', equipo_id=equipo_id)
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'modificar_equipo.html', {'form': form})

def modificar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    if request.method == 'POST':
        form = ProcesoForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            return redirect('detail_proceso', proceso_id=proceso_id)
    else:
        form = ProcesoForm(instance=proceso)
    return render(request, 'modificar_proceso.html', {'form': form})


     