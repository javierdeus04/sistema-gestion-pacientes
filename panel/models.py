from django.db import models

class Configuracion(models.Model):
    titulo_tab = models.CharField(max_length=30)
    nombre_clinica = models.CharField(max_length=20, default='Nombre Clinica')
    nombre_usuario = models.CharField(max_length=20, default='Nombre Usuario')
    logo = models.ImageField(upload_to="", null=True, blank=True)

    def __str__(self):
        return f'Configuracion pagina {self.nombre_usuario}'   



class Paciente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    numero_CI = models.IntegerField(null=True, blank=True)
    numero_contacto = models.IntegerField(null=True, blank=True)
    motivo_consulta = models.CharField(max_length=20)


    def __str__(self):
          return f'CI:{self.numero_CI} - {self.nombre} {self.apellido}'

