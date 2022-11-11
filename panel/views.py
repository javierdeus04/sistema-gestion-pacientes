from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from web.models import SolicitudPaciente
from panel.models import Configuracion, Paciente, Registro
from panel.forms import RegForm
from django.shortcuts import get_object_or_404, redirect

@login_required
def base(request):
    configuracion = Configuracion.objects.first()
    return render (request, 'panel/panel_base.html', {'configuracion': configuracion})


@login_required
def principal(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'panel/principal.html', {'configuracion': configuracion})


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


class ListRegistro(LoginRequiredMixin, ListView):
    model=Registro
    ordering = ['-fecha']
    paginate_by = 20

    def get_context_data(self,*args, **kwargs): 
        context = super(ListRegistro, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context


class CreateRegistro(LoginRequiredMixin, View):
    template_name = 'panel/registro_form.html'
    initial = {}
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
        return render(request, 'registro_form.html')

    
class DetailRegistro(LoginRequiredMixin, DetailView):
    model=Registro
    
    def get_context_data(self,*args, **kwargs): 
        context = super(DetailRegistro, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context


class UsuarioLogin(LoginView):
    template_name = 'panel/login.html'
    next_page = reverse_lazy("index")

    def get_context_data(self,*args, **kwargs): 
        context = super(UsuarioLogin, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context
    
class UsuarioLogout(LogoutView):
    template_name = 'panel/logout.html'

    def get_context_data(self,*args, **kwargs): 
        context = super(UsuarioLogout, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class UsuarioSignUp(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"

    def get_context_data(self,*args, **kwargs): 
        context = super(UsuarioSignUp, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context

class ProfileUpdate(UpdateView):
    model = User   
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "registration/signup.html"
    success_url = reverse_lazy("panel-login")

    def get_context_data(self,*args, **kwargs): 
        context = super(ProfileUpdate, self).get_context_data(*args,**kwargs) 
        context['configuracion'] = Configuracion.objects.first() 
        return context




    


