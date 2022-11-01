from django.contrib import admin
from django.urls import path

from panel.views import (PacienteCreate, PacienteDelete, PacienteDetail, PacienteSearch, PacienteUpdate, 
                        UsuarioLogin, UsuarioLogout, UsuarioSignUp, principal, PacienteList, ProfileUpdate)

urlpatterns = [
    path('', principal, name='index'),
    path('login/', UsuarioLogin.as_view(), name='panel-login'),
    path('logout/', UsuarioLogout.as_view(), name='panel-logout'),
    path('paciente-list/', PacienteList.as_view(), name='paciente-list'),
    path('paciente-ficha/<int:pk>', PacienteDetail.as_view(), name='paciente-ficha'),
    path('paciente-create/', PacienteCreate.as_view(), name='paciente-create'),
    path('paciente-update/<int:pk>', PacienteUpdate.as_view(), name='paciente-update'),
    path('paciente-delete/<int:pk>', PacienteDelete.as_view(), name='paciente-delete'),
    path('paciente-search', PacienteSearch.as_view(), name='paciente-search'),
    path('signup', UsuarioSignUp.as_view(), name='usuario-signup'),
    path('user-profile/<int:pk>', ProfileUpdate.as_view(), name="profile-update"),
]