from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from historiaclinica.models import Registro

@login_required
def hc_panel(request):
    return render(request, 'historiaclinica/hc-panel.html')

class ListRegistro(LoginRequiredMixin, ListView):
    model=Registro
    ordering = ['-fecha']
    paginate_by = 20

class CreateRegistro(LoginRequiredMixin, CreateView):
    model=Registro
    fields = ['resumen', 'contenido', 'firma', 'image']
    success_url = reverse_lazy("hc-list")

class DetailRegistro(LoginRequiredMixin, DetailView):
    model=Registro

@login_required
def hc_search(request):
    return render(request, 'historiaclinica/hc-search.html')

class SearchRegistroByFirma(LoginRequiredMixin, ListView):
    def get_queryset(self):
        registro_firma = self.request.GET.get('firma')
        return Registro.objects.filter(firma__icontains=registro_firma)

    