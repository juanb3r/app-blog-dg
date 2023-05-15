# Lets Do it Now
API RESTful para una plataforma de blog con funcionalidades avanzadas utilizando Django REST Framework y Python como lenguaje de programación principal.

## Acerca del proyecto
La plataforma de blog consta de varias entidades: Usuarios, Perfiles, Entradas (Posts), Comentarios y Likes. Los Usuarios pueden tener roles de administrador, editor o blogger. Los Usuarios tienen un Perfil asociado con información adicional como la biografía y la imagen de perfil. Las Entradas están asociadas a un Usuario (el autor) e incluyen un título, contenido, fecha de publicación, categoría y una lista de etiquetas (tags). Los Comentarios están vinculados a un Usuario (la persona que comenta) y a una Entrada, e incluyen el texto del comentario. Los Usuarios pueden dar Like tanto a Entradas como a Comentarios.

## Requisitos del proyecto:
1.	Modelado de Datos: Diseña e implementa modelos de datos para Usuario, Perfil, Entrada, Comentario y Like.
2.	Autenticación y Autorización: Implementa un sistema de autenticación y autorización que permita a los administradores gestionar todos los recursos, a los editores gestionar Entradas, Comentarios y Likes, y a los bloggers crear y gestionar sus propias Entradas, Comentarios y Likes.
3.	API Endpoints: Implementa los siguientes endpoints:
    ●	CRUD de Usuarios y Perfiles
    ●	CRUD de Entradas
    ●	CRUD de Comentarios
●	CRUD de Likes
4.	Serialización: Emplea los serializadores de Django REST para manejar la conversión entre modelos y JSON.
5.	Filtros y Paginación: Implementa filtros que permitan buscar entradas por título, autor, categoría y etiquetas. Además, implementa la paginación en los endpoints que devuelven múltiples recursos.
6.	Pruebas: Desarrolla pruebas unitarias y de integración para los modelos, la autenticación, la autorización y los endpoints de la API. Asegúrate de cubrir tanto los casos de éxito como los de error.
7.	Documentación: Documenta todos los endpoints de la API utilizando Django REST Swagger o similar.


### Construido con
* Lenguaje: Python 3.10.5
* Framework: Django REST Framework 
* Base de dato: sqlite3


<!-- GETTING STARTED -->
## Iniciando

Este es un ejemplo de como deberian instalar el proyecto localmente dada las instruciones.


### Intalacion 

1. Instalar virtualEnv e instalarlo
```sh
$ virtualenv -p python3 venv
```
```sh
$ source venv/bin/activate
```
2. Instalar requirements.txt
```sh
$ pip3 install -r requirements.txt
```
### Base de datos
1. Las migraciones encarga de crear nuevas migraciones en función de los cambios que haya realizado en sus modelos
```sh
$ python manage.py makemigrations
```
2. Encargado de aplicar y desaplicar migraciones.
```sh
$ python manage.py migrate
```

### Correr la api
1. Inicio del servidor 
```sh
$ python manage.py runserver
```

### Documentacion de la API

La documentacion esta hecha cumpliendo los estadares de OpenAPI con ayuda del Django y Usage.

La ruta de la documentacion se encuentra disponible en http://localhost:8000/docs
