from django.shortcuts import render
from web.forms import SolicitudForm
from django.views import View
from django.views.generic import DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from web.models import SolicitudPaciente
from django.urls import reverse_lazy
from panel.models import Configuracion
from django.contrib.auth.decorators import login_required



def web_principal(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'web/web_principal.html', {"configuracion": configuracion})

class SolicitudCreate(View):
    template_name = "web/solicitudpaciente_form.html"
    form_class = SolicitudForm
    initial = {}
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        configuracion = Configuracion.objects.first()
        return render(request, self.template_name, {"form": form, "configuracion": configuracion})

    def post(self, request):
        form  = self.form_class(request.POST)        
        template_name = "web/solicitud_exitosa.html"
        configuracion = Configuracion.objects.first()
    
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        
        return render(request, template_name, {"form": form, "configuracion": configuracion})

class SolicitudList(LoginRequiredMixin, ListView):
    model = SolicitudPaciente
    ordering = ['fecha_creacion']
    paginate_by = 5
    
    def get_context_data(self,*args, **kwargs): 
        context = super(SolicitudList, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class SolicitudDetail(LoginRequiredMixin, DetailView):
    model = SolicitudPaciente
    
    def get_context_data(self,*args, **kwargs): 
        context = super(SolicitudDetail, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class SolicitudDelete(LoginRequiredMixin, DeleteView):
    model = SolicitudPaciente
    success_url = reverse_lazy("index")

    def get_context_data(self,*args, **kwargs): 
        context = super(SolicitudDelete, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

@login_required
def about(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'web/about.html', {'configuracion': configuracion})

