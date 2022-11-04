from django.shortcuts import render
from web.forms import SolicitudForm
from django.views import View


def web_principal(request):
    return render(request, 'web/web_principal.html')

class SolicitudCreate(View):
    template_name = "web-principal.html"
    form_class = SolicitudForm
    initial = {"nombre_y_apellido":"", "fecha_nacimiento":""}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form  = self.form_class(request.POST)
    
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        
        return render(request, self.template_name, {"form": form})

