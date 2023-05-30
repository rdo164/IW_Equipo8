from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Empleado, Equipo, Proceso, Archivo
from django.shortcuts import get_object_or_404
from django import forms
from .forms import EmpleadoForm, EquipoForm, ProcesoForm, EmailForm, ArchivoForm
from django.urls import reverse_lazy
from .utils import enviar_email
import os

# Create your views here.

# índice de la página
def index(request):
    return render(request, 'index.html')

# muestra todos los equipos
def index_equipo(request):
	equipos = Equipo.objects.order_by('marca')    
	context = { 'lista_equipos': equipos}
	return render(request, 'index_equipo.html', context)

# devuelve los detalles del equipo solicitado
def show_equipo(request, equipo_id):
    #                  .     
    empleados = Empleado.objects.order_by('proceso')
                          
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    context = {'equipo': equipo, 'lista_empleados': empleados}
    return render(request, 'detail_equipo.html', context)

# devuelve los procesos
def index_proceso(request):
    procesos = Proceso.objects.order_by('nombreProceso')
    context = {'lista_procesos': procesos}
    return render(request, 'index_proceso.html', context)

# devuelve los detalles del proceso solicitado
def show_proceso(request, proceso_id):
    empleados = Empleado.objects.order_by('proceso')
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    context = {'proceso': proceso, 'lista_empleados': empleados}
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

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('index_empleado')
    return render(request, 'confirmar_borrar_empleado.html', {'empleado': empleado})

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

def modificar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('detail_empleado', empleado_id=empleado_id)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'modificar_empleado.html', {'form': form})

# Enviar emails

def enviar_email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            destinatario = form.cleaned_data['destinatario']
            asunto = form.cleaned_data['asunto']
            contenido = form.cleaned_data['contenido']
            enviar_email(destinatario, asunto, contenido)
            return redirect('confirmacion_envio')  # Redirige a la página de confirmación
    else:
        form = EmailForm()
    
    context = {'form': form}
    return render(request, 'email_form.html', context)

def confirmacion_envio(request):
    return render(request, 'confirmacion_envio.html')

# Subir archivos con opción de descarga

def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mostrar_archivos')
    else:
        form = ArchivoForm()
    
    context = {'form': form}
    return render(request, 'subir_archivo.html', context)

def mostrar_archivos(request):
    archivos = Archivo.objects.all()
    context = {'archivos': archivos}
    return render(request, 'mostrar_archivos.html', context)

def descargar_archivo(request, archivo_id):
    archivo = Archivo.objects.get(pk=archivo_id)
    response = HttpResponse(archivo.archivo, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{archivo.archivo.name}"'
    return response
     