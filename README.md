# Proyecto para sistema de gestión de pacientes
Versión desarrollada en Python 3.10.6.

Esta aplicación permite manejar una base de datos con las siguientes funciones:
- Creacion de perfiles de pacientes con informacion e historia clinica.
- Visualizacion de todas los perfiles en forma de lista por orden alfabetico.
- Edicion de la informacion de dichos perfiles.
- Eliminacion de perfiles (con su consecuente eliminacion de su historia clinica)
- Realizacion de búsquedas en la base de datos por nombre de paciente.
- Creacion de registros por consulta o sesion, permitiendo en la misma adjuntar informacion en formato de imagen (paraclinica) en caso de ser necesario, y agregando dichos registros a la historia clinica del paciente.
- Visualizacion de todos los registros en forma de lista por orden de antiguedad (de mas nuevo a mas antiguo).
- Consulta de registros.

## Pasos para su instalación:

1° Clonar el proyecto desde GitHub: `git clone https://github.com/javierdeus04/sistema-gestion-pacientes' o descargar el archivo comprimido que contiene la carpeta del proyecto.

2° En la ruta correspondiente a la carpea del proyecto:
- Realizar las migraciones: `python manage.py migrate`
- Correr el servidor: `python manage.py runserver`

3° En el navegador ir al localhost :8000/ para confirmar que la aplicación funciona correctamente.

## Recorriendo la app:
- Ingresar a http://127.0.0.1:8000/admin/ para acceder al sitio de administrador
- Ingresar a http://127.0.0.1:8000/ppal/ para acceder al menú principal
