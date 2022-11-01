from django.contrib import admin
from django.urls import path, include
from historiaclinica.views import CreateRegistro, hc_panel, ListRegistro, DetailRegistro, SearchRegistroByFirma, hc_search

urlpatterns = [
    path('', hc_panel, name='hc-panel'),
    path('hc-list', ListRegistro.as_view(), name='hc-list'),
    path('hc-create', CreateRegistro.as_view(), name='hc-create'),
    path('hc-detail/<int:pk>', DetailRegistro.as_view(), name='hc-detail'),
    path('hc-search/', hc_search, name="hc-search"),
    path('hc-search-by-firma/', SearchRegistroByFirma.as_view(), name='hc-search-by-firma')
]
