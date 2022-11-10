# Desafío EMSER
Desarrollado con Python 3.11.0 y Django 4.0.4

Estilos aplicados con CSS

## Introducción
Este repositorio es una prueba técnica la cual consiste en desarrollar una página web que contenga un formulario donde se puedan cargar personas a una base de datos. Para este desafio se me fue requerido desarrollar en Python y Django, tecnologías en las cuales no tenía conocimientos y debí de estudiarlas y aprenderlas en poco tiempo, por lo que es mi primer aplicación web usando las mismas.

## Instalación del proyecto
Primero que nada debes tener instalado Python en su versión 3.11.0 y Django en su versión 4.0.4, luego debes copiar y pegar el siguiente comando en tu consola o terminal para clonar el repositorio:

```bash
git clone https://github.com/lucianodavid22/DesafioEMSER.git
```

Una vez clonado el repositorio, accede al mismo y utiliza el siguiente comando para levantar el servidor:

```bash
python manage.py runserver
```

En ese momento tendrás la aplicación corriendo en el puerto 8000, pero para poder hacer uso de la misma deberás de ir a /form/registro/:

http://localhost:8000/form/registro/

Ahí podrás comenzar a almacenar usuarios, llenando el formulario con los datos a guardar y presionando en el botón "CARGAR" para poder asi guardar los datos ingresados en la base de datos, esto te llevará a la pantalla de "USUARIO GUARDADO EXITOSAMENTE" en la cual se encuentra un único botón "VOLVER" que te devolverá a la página del formulario con la lista de usuarios cargados, donde ya se encontrará listado el usuario que acabas de ingresar.
