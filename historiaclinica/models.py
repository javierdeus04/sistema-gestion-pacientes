from datetime import datetime
from email.utils import format_datetime
from wsgiref.handlers import format_date_time
from django.db import models
from psycopg2 import DATETIME
from panel.models import Paciente


class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    resumen = models.CharField(max_length=30)
    contenido = models.TextField(max_length=3000, null=True, blank=True)
    firma = models.CharField(max_length=10)
    image = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False, related_name='registros')

    def __str__(self):
        return f"Paciente: {self.paciente.nombre} - Resumen sesion: {self.resumen} - {self.fecha} - Responsable: {self.firma}"


