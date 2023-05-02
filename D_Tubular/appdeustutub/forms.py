from .models import Empleado, Equipo, Proceso
from django import forms


# Metodo para que aparezcan todos los datos a añadir segun el modelo al que se refiera

class equipoAnadirForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class empleadoAnadirForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class procesoAnadirForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = '__all__'




    
    