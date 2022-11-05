from django import forms
from django.contrib.admin import widgets
from web.models import SolicitudPaciente

class SolicitudForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%Y"], 
                                            widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))

    class Meta:
        model = SolicitudPaciente        
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'numero_CI', 'numero_contacto', 'motivo_consulta']

        


