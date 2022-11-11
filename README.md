# Sistema de gestión de pacientes - Javier Deus
Versión desarrollada en Python 3.10.6.

Esta aplicación permite manejar una base de datos con las siguientes funciones (requiere permisos de usuario):
- Creación de perfil de paciente con sus datos personales.
- Visualización de los perfiles en forma de lista por orden alfabético.
- Visualización de cada perfil de paciente en detalle.
- Edición del perfil de paciente.
- Eliminación del perfil de paciente (con la consecuente eliminación de los registros de sesión asociados).
- Búsqueda del perfil de paciente por su nombre.
- Creación de registro por sesión de tratamiento, permitiendo adjuntar archivos en formato de imagen (paraclínica) en caso de ser requerido.
- Visualización de los registros en forma de lista por orden de antiguedad (de más nuevo a más antiguo).
- Visualización de cada registro en detalle.
- Visualización de las solicitudes de consulta en forma de lista por orden de antiguedad (de más antigua a más nueva).
- Visualización de cada solicitud de consulta en detalle.
- Eliminación de la solicitud de consulta.
- Actualización de datos del usuario logueado.

Para las siguientes funciones adicionales se requieren permisos de ¨superuser¨:
- Registro de nuevo usuario
- Acceso al sitio administrativo de django (gestión de usuarios, carga de configuraciones de aspecto personalizadas, etc).

Quién no cuente con usuario registrado será redirigido a la web principal, que cuenta con las siguientes funciones:
- Visualización de la información correspondiente a la empresa/emprendimiento.
- Creación de formulario de solicitud de consulta.
- Ingreso al login.

## Pasos para su instalación y funcionamiento:

1° Desde la terminal de comandos de sistema clonar el proyecto desde GitHub: `git clone https://github.com/javierdeus04/sistema-gestion-pacientes` o descargar el archivo comprimido que contiene la carpeta del proyecto.

2° Desde la terminal de comandos de sistema (ubicados en la ruta correspondiente a la carpea del proyecto), ejecutar las siguientes acciones:
- Instalación de django: `pip install django`
- Instalación de WhiteNoise: `pip install whitenoise`
- Instalación de Pillow: `pip install Pillow`
- Realizar las migraciones: `python manage.py migrate`
- Correr el servidor: `python manage.py runserver`
- Crear un usuario con los permisos necesarios: `python manage.py createsuperuser`

3° En el navegador ir al localhost:8000 para confirmar que la aplicación funciona correctamente (Page not found 404) 

## Recorriendo la app:
- Ingresar a localhost:8000/admin para acceder al sitio de administrador de django
- Ingresar a localhost:8000/principal para acceder a la página principal de gestión de pacientes
- Ingresar a localhost:8000/web-princiapl para acceder a la web pública
