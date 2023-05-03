from django import forms
from .models import Empleado, Equipo, Proceso

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['equipo', 'proceso', 'dni', 'nombre', 'apellidos', 'email', 'telefono']
        
class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['modelo', 'marca', 'categoria', 'fecha_adquisicion', 'fecha_instalacion']
        
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['equipo', 'codOrdenFabricacion', 'codigoProceso', 'nombreProceso', 'referencia', 'fechaInicio', 'fechaFin']