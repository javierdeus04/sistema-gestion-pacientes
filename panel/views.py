from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from web.models import SolicitudPaciente
from panel.models import Configuracion, Paciente

@login_required
def base(request):
    configuracion = Configuracion.objects.first()
    return render (request, 'panel/panel_base.html', {'configuracion': configuracion})

@login_required
def principal(request):
    configuracion = Configuracion.objects.first()
    solicitud_list = SolicitudPaciente.objects.all()   
    return render(request, 'panel/principal.html', {"solicitud_list": solicitud_list, 'configuracion': configuracion})

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    ordering = ['nombre']
    paginate_by = 10
    
    def get_context_data(self,*args, **kwargs): 
        context = super(PacienteList, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context
        
class PacienteDetail(LoginRequiredMixin, DetailView):
    model = Paciente
    
    def get_context_data(self,*args, **kwargs): 
        context = super(PacienteDetail, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'numero_CI', 'numero_contacto', 'motivo_consulta']
    success_url = '/principal/paciente-list'
    
    def get_context_data(self,*args, **kwargs): 
        context = super(PacienteCreate, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context
 

class PacienteUpdate(LoginRequiredMixin, UpdateView):
  model = Paciente
  success_url = reverse_lazy("paciente-list")
  fields = ["nombre", "apellido", "numero_contacto", "motivo_consulta"]
  
  def get_context_data(self,*args, **kwargs): 
        context = super(PacienteUpdate, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy("paciente-list")
    
    def get_context_data(self,*args, **kwargs): 
        context = super(PacienteDelete, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class PacienteSearch(LoginRequiredMixin, ListView):
    
    def get_context_data(self,*args, **kwargs): 
        context = super(PacienteSearch, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context
    
    def get_queryset(self):
        paciente_nombre = self.request.GET.get('nombre')
        return Paciente.objects.filter(nombre__icontains=paciente_nombre)
        

class UsuarioLogin(LoginView):
    template_name = 'panel/login.html'
    next_page = reverse_lazy("index")

class UsuarioLogout(LogoutView):
    template_name = 'panel/logout.html'

class UsuarioSignUp(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User   
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "registration/signup.html"
    success_url = reverse_lazy("panel-login")




    


