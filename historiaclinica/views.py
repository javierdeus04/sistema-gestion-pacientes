from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from historiaclinica.models import Registro
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.admin import User
from historiaclinica.forms import RegForm
from django.views import View
from panel.models import Configuracion




@login_required
def hc_panel(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'historiaclinica/hc-panel.html', {'configuracion': configuracion})

class ListRegistro(LoginRequiredMixin, ListView):
    model=Registro
    ordering = ['-fecha']
    paginate_by = 20

    def get_context_data(self,*args, **kwargs): 
        context = super(ListRegistro, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class CreateRegistro(LoginRequiredMixin, View):
    template_name = 'historiaclinica/registro_form.html'
    initial = {'paciente':'', 'resumen':'', 'contenido': '', 'image':'', 'image_dos':'', 'image_tres':''}
    form_class = RegForm
    
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form, 'configuracion': Configuracion.objects.first()})

    def post(self, request):
        current_user = get_object_or_404(User, pk=request.user.pk)
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                reg = form.save(commit=False)
                reg.user = current_user
                reg.save()
                return redirect('hc-list')
        else:
            form = self.form_class()
        return render(request, 'historiaclinica/registro_form.html')

    


class DetailRegistro(LoginRequiredMixin, DetailView):
    model=Registro
    

    def get_context_data(self,*args, **kwargs): 
        context = super(DetailRegistro, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context



    
