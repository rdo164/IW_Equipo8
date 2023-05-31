from django.views import View
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
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class EquipoListView(ListView):
    model = Equipo
    template_name = 'index_equipo.html'
    context_object_name = 'lista_equipos'
    ordering = 'marca'

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'detail_equipo.html'
    context_object_name = 'equipo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_empleados'] = Empleado.objects.order_by('proceso')
        return context

class ProcesoListView(ListView):
    model = Proceso
    template_name = 'index_proceso.html'
    context_object_name = 'lista_procesos'
    ordering = 'nombreProceso'

class ProcesoDetailView(DetailView):
    model = Proceso
    template_name = 'detail_proceso.html'
    context_object_name = 'proceso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_empleados'] = Empleado.objects.order_by('proceso')
        return context

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'index_empleado.html'
    context_object_name = 'lista_empleados'
    ordering = 'nombre'

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'detail_empleado.html'
    context_object_name = 'empleado'

# Métodos para añadir empleados, procesos y equipos:

def add_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            empleado = form.save()
            return redirect('empleado-list')
    else:
        form = EmpleadoForm()
    return render(request, 'add_empleado.html', {'form': form})

def add_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipo-list')
    else:
        form = EquipoForm()
    return render(request, 'add_equipo.html', {'form': form})

def add_proceso(request):
    if request.method == 'POST':
        form = ProcesoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proceso-list')
    else:
        form = ProcesoForm()
    return render(request, 'add_proceso.html', {'form': form})

# Borrar creaciones anteriores:

def borrar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, id=proceso_id)
    if request.method == 'POST':
        proceso.delete()
        return redirect('proceso-list')
    return render(request, 'confirmar_borrar_proceso.html', {'proceso': proceso})

def borrar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipo-list')
    return render(request, 'confirmar_borrar_equipo.html', {'equipo': equipo})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado-list')
    return render(request, 'confirmar_borrar_empleado.html', {'empleado': empleado})

# Modificar creaciones anteriores:

def modificar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipo-detail', pk=equipo_id)
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'modificar_equipo.html', {'form': form})

def modificar_proceso(request, proceso_id):
    proceso = get_object_or_404(Proceso, pk=proceso_id)
    if request.method == 'POST':
        form = ProcesoForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            return redirect('proceso-detail', pk=proceso_id)
    else:
        form = ProcesoForm(instance=proceso)
    return render(request, 'modificar_proceso.html', {'form': form})

def modificar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado-detail', pk=empleado_id)
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

def borrar_archivo(request, archivo_id):
    archivo = get_object_or_404(Archivo, pk=archivo_id)
    
    if request.method == 'POST':
        archivo.delete()
        return redirect('mostrar_archivos')
    
    context = {'archivo': archivo}
    return render(request, 'borrar_archivo.html', context)
     