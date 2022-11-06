from django import forms
from django.contrib.admin import widgets
from web.models import SolicitudPaciente

class SolicitudForm(forms.ModelForm):
    
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%Y"], 
                                            widget=forms.TextInput(attrs={'placeholder': 'Ej: 30/12/1995'}))
    disponibilidad_horaria_inicial = forms.TimeField(input_formats=['%H:%M'],
                                            widget=forms.TextInput(attrs={'placeholder': 'Ej: 06:00'}))
    disponibilidad_horaria_final = forms.TimeField(input_formats=['%H:%M'],
                                            widget=forms.TextInput(attrs={'placeholder': 'Ej: 17:30'}))

    class Meta:
        model = SolicitudPaciente        
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'numero_CI', 'numero_contacto', 'motivo_consulta',
                'disponibilidad_horaria_inicial', 'disponibilidad_horaria_final']

        


