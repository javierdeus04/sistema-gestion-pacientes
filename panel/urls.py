from django.contrib import admin
from django.urls import path

from panel.views import UsuarioLogin, UsuarioLogout, principal

urlpatterns = [
    path('', principal, name='index'),
    path('login/', UsuarioLogin.as_view(), name='panel-login'),
    path('logout/', UsuarioLogout.as_view(), name='panel-logout'),
]