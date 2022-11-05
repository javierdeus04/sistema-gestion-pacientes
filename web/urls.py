from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from web.views import web_principal, SolicitudCreate


urlpatterns = [
    path('', web_principal),
    path('solicitudes', SolicitudCreate.as_view())
]
   