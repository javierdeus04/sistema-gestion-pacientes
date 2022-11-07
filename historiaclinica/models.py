from datetime import datetime
from email.utils import format_datetime
from wsgiref.handlers import format_date_time
from django.db import models
from psycopg2 import DATETIME
from panel.models import Paciente
from django.contrib.auth.admin import User


class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    firma = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='registros')
    resumen = models.CharField(max_length=30)
    contenido = models.TextField(max_length=3000, null=True, blank=True)    
    image = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    image_dos = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    image_tres = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False, related_name='registros')

    def __str__(self):
        return f"Paciente: {self.paciente.nombre} - Resumen sesion: {self.resumen} - {self.fecha}"


