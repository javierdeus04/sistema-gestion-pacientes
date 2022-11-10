from django import forms
from historiaclinica.models import Registro

class RegForm(forms.ModelForm):    
    
    class Meta:
        model = Registro
        fields = ['paciente', 'resumen', 'contenido', 'image', 'image_dos', 'image_tres']