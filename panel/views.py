from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User

from historiaclinica.models import Registro
from panel.models import Configuracion, Paciente

@login_required
def principal(request):
    configuracion = Configuracion.objects.first()    
    return render(request, 'panel/principal.html', {'configuracion': configuracion})
    

class PacienteList(LoginRequiredMixin, ListView):
    model = Paciente
    ordering = ['nombre']
    paginate_by = 10

    def config(request):
        configuracion = Configuracion.objects.first()
        render(request, 'panel/paciente_list.html', {'configuracion': configuracion})

class PacienteDetail(LoginRequiredMixin, DetailView):
    model = Paciente

class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    fields = ['nombre', 'apellido', 'fecha_de_nacimiento', 'numero_CI', 'numero_contacto', 'motivo_consulta']
    success_url = '/principal/paciente-list'

class PacienteUpdate(LoginRequiredMixin, UpdateView):
  model = Paciente
  success_url = reverse_lazy("paciente-list")
  fields = ["nombre", "apellido", "numero_contacto", "motivo_consulta"]

class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    success_url = reverse_lazy("paciente-list")

class PacienteSearch(LoginRequiredMixin, ListView):
    def get_queryset(self):
        paciente_nombre = self.request.GET.get('nombre')
        return Paciente.objects.filter(nombre__icontains=paciente_nombre)
    
class UsuarioLogin(LoginView):
    template_name = 'panel/login.html'
    next_page = reverse_lazy("index")

class UsuarioLogout(LogoutView):
    template_name = 'panel/logout.html'

class UsuarioSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("panel-login")
    template_name = "panel/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username']
    success_url = reverse_lazy("panel-login")




    


