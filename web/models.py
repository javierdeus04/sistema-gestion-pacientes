from django.db import models

class SolicitudPaciente(models.Model):

    fecha_creacion = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    numero_CI = models.IntegerField()
    numero_contacto = models.IntegerField()
    motivo_consulta = models.TextField(max_length=3000)
    

    def __str__(self):
        return f'Fecha: {self.fecha_creacion} - {self.numero_CI} - {self.nombre} {self.apellido}'

    
    

    
