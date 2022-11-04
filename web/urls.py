from django.conf.urls.static import static
from django.urls import path, include
from web.views import web_principal, SolicitudCreate


urlpatterns = [
    path('', web_principal, name="web-principal"),
    path('', SolicitudCreate.as_view(), name='solicitud-paciente'),
    
]   