from django.shortcuts import render
from web.forms import SolicitudForm
from django.views import View


def web_principal(request):
    return render(request, 'web/web_principal.html')

class SolicitudCreate(View):
    template_name = "web/solicitudpaciente_form.html"
    form_class = SolicitudForm
    initial = {"nombre":"", "apellido": "", "fecha_nacimiento":"", "numero_CI":"", "numero_contacto":"", "motivo_consulta":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form  = self.form_class(request.POST)
        template_name = "web/solicitud_exitosa.html"
    
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        
        return render(request, template_name, {"form": form})

