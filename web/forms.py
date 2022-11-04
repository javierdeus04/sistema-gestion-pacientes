from django import forms
from django.contrib.admin import widgets
from web.models import SolicitudPaciente

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudPaciente
        fecha_de_nacimiento = forms.DateField(label="fecha de nacimiento")
        fields = ['nombre_y_apellido', 'fecha_nacimiento']

        def __init__(self, *args, **kwargs):
            super(SolicitudForm, self).__init__(*args, **kwargs)
            self.fields['mydate'].widget = widgets.AdminDateWidget()


