from django import forms
from .models import Empleado, Equipo, Proceso, Archivo

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['equipo', 'proceso', 'dni', 'nombre', 'apellidos', 'email', 'telefono']
        
        
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['modelo', 'marca', 'categoria', 'fecha_adquisicion', 'fecha_instalacion']
        widgets = {
            'fecha_adquisicion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_instalacion': forms.DateInput(attrs={'type': 'date'})
        }
        
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['equipo', 'codOrdenFabricacion', 'codigoProceso', 'nombreProceso', 'referencia', 'fechaInicio', 'fechaFin']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'type': 'date'})
        }
        labels = {
            'equipo': 'Equipo',
            'codOrdenFabricacion': 'Código de Orden de Fabricación',
            'codigoProceso': 'Código de Proceso',
            'nombreProceso': 'Nombre de Proceso',
            'referencia': 'Referencia',
            'fechaInicio': 'Fecha de Inicio',
            'fechaFin': 'Fecha de Fin',
        }

class EmailForm(forms.Form):
    destinatario = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']