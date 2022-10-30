from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from panel.models import Configuracion

@login_required
def principal(request):
    configuracion = Configuracion.objects.first()    
    return render(request, 'panel/principal.html', {'configuracion': configuracion})

class UsuarioLogin(LoginView):
    template_name = 'panel/login.html'
    next_page = reverse_lazy("index")

class UsuarioLogout(LogoutView):
    template_name = 'panel/logout.html'
