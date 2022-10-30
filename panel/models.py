from django.db import models

class Configuracion(models.Model):
    titulo_tab = models.CharField(max_length=30)
    nombre_clinica = models.CharField(max_length=20, default='Nombre Clinica')
    nombre_usuario = models.CharField(max_length=20, default='Nombre Usuario')

    def __str__(self):
        return f'Configuracion pagina {self.nombre_usuario}'   



class Paciente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    numero_ci = models.IntegerField()
    numero_contacto = models.IntegerField()
    motivo_consulta = models.CharField(max_length=20)


    def __str__(self):
          return f'{self.nombre} {self.apellido} - CI:{self.numero_ci}'

