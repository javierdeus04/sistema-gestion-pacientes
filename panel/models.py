from django.db import models
from django.contrib.auth.admin import User

class Configuracion(models.Model):
    titulo_tab = models.CharField(max_length=30)
    nombre_clinica = models.CharField(max_length=20, default='Nombre Clinica')
    logo = models.ImageField(upload_to="logos", null=True, blank=True)
    slogan = models.CharField(max_length=50, default='slogan')

    def __str__(self):
        return f'Configuracion pagina {self.nombre_clinica}' 


class Paciente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    numero_CI = models.IntegerField(null=True, blank=True)
    numero_contacto = models.IntegerField(null=True, blank=True)
    motivo_consulta = models.CharField(max_length=20)    

    def __str__(self):
          return f'{self.numero_CI} - {self.nombre} {self.apellido}'
          

class Registro(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='registros')
    resumen = models.CharField(max_length=30)
    contenido = models.TextField(max_length=3000, null=True, blank=True)    
    image = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    image_dos = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    image_tres = models.ImageField(upload_to="paraclinica", null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False, blank=False, related_name='registros')

    def __str__(self):
        return f"Paciente: {self.paciente.nombre} - Resumen sesion: {self.resumen} - {self.fecha}"

