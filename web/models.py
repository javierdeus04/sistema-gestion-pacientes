from django.db import models

class SolicitudPaciente(models.Model):
    nombre_y_apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    numero_CI = models.IntegerField()
    numero_contacto = models.IntegerField()
    motivo_consulta = models.TextField(max_length=100)
    fecha_solicitada = models.DateField()

    
