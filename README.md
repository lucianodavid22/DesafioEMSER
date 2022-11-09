# DesafioEMSER
<p>Desarrollado con Python 3.11.0 y Django 4.0.4</p>
<br>
## Introducción
Este repositorio es una prueba técnica la cual consiste en desarrollar una página web que contenga un formulario donde se puedan cargar personas a una base de datos. Para este desafio se me fue requerido desarrollarlo en Python y Django, tecnologías las cuales desconocía, por lo que es mi primer aplicación web usando las mismas.
<br>
## Instalación del proyecto
Primero que nada debes tener instalado Python en su versión 3.11.0 y Django en su versión 4.0.4, luego debes copiar el siguiente comando en tu consola o terminal:
<br>
```bash
git clone https://github.com/lucianodavid22/DesafioEMSER.git
```
<br>
Una vez clonado el repositorio, usa el siguiente comando para levantar el servidor:
<br>
```bash
python manage.py runserver
```
<br>
En ese momento tendrás la aplicación corriendo en el puerto 8000:
<br>
http://localhost:8000/
<br>
pero para poder usar la aplicación deberás de ir a /form/registro/:
<br>
http://localhost:8000/form/registro/
<br>
Ahí podrás comenzar a hacer uso de la misma, llenando el formulario con los datos a guardar y presionando en el botón "CARGAR" para poder asi guardar los datos ingresados en la base de datos. Esto te llevará a la pantalla de "usuario guardado exitosamente" en la cual hay un único botón "VOLVER" que te devolverá a la página del formulario con la lista de usuarios cargados.
