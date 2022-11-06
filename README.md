# Sistema de gestión de pacientes - Javier Deus
Versión desarrollada en Python 3.10.6.

Esta aplicación permite manejar, a quien tenga un usuario registrado, una base de datos con las siguientes funciones:
- Creación de perfiles de pacientes con sus datos personales y su historia clínica.
- Visualización de todas los perfiles en forma de lista por orden alfabético.
- Edición de los perfiles de los pacientes.
- Eliminación de perfiles (con la consecuente eliminación de la historia clínica correspondiente)
- Búsqueda en la base de datos por nombre de paciente.
- Creación de registro por sesión de tratamiento, permitiendo adjuntar archivos en formato de imagen (paraclínica) en caso de ser requerido, siendo dicho registro agregado de forma automática a la historia clínica del paciente correspondiente.
- Visualización de los registros de todos los pacientes en forma de lista por orden de antiguedad (de mas nuevo a mas antiguo).
- Visualización en detalle de cada registro.
- Actualización de datos del usuario
Para las siguientes funciones adicionales se requieren permisos de ¨superuser¨:
- Registrar nuevos usuarios
- Acceder al sitio administrativo de django, desde donde se podrá gestionar usuarios y cargar configuraciones de aspecto personalizadas.
Quién no cuente con usuario registrado será redirigido a la web principal, desde la cual se podrá:
- Leer la información correspondiente a la empresa/emprendimiento.
- Crear un formulario de solicitud de consulta.
- Ingresar al login.

## Pasos para su instalación y funcionamiento:

1° Clonar el proyecto desde GitHub: `git clone https://github.com/javierdeus04/sistema-gestion-pacientes' o descargar el archivo comprimido que contiene la carpeta del proyecto.
2° Desde la terminal de comandos de sistema (ubicados en la ruta correspondiente a la carpea del proyecto), ejecutar los siguientes acciones:
- Instalación de django: `pip install django`
- Instalación de WhiteNoise: `pip install whitenoise`
- Instalación de Pillow: `pip install Pillow`
- Realizar las migraciones: `python manage.py migrate`
- Correr el servidor: `python manage.py runserver`
- Crear un usuario con los permisos necesarios: `python manage.py createsuperuser`
3° En el navegador ir al localhost :8000/ para confirmar que la aplicación funciona correctamente.

## Recorriendo la app:
- Ingresar a /admin para acceder al sitio de administrador de django
- Ingresar a /principal para acceder a la página principal de gestión de pacientes
' Ingresar a /nombre-de-clinica para acceder a la web de la clínica
