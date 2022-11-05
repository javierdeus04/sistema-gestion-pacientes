from django.shortcuts import render
from web.forms import SolicitudForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from web.models import SolicitudPaciente


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


class SolicitudList(LoginRequiredMixin, ListView):
    model = SolicitudPaciente
    ordering = ['nombre']
    paginate_by = 10    



