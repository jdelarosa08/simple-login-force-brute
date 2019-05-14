## Simple Modulo Web para Login
### Implementado con Python, Flask y Flask-Sqlalchemy
### Haciendo uso de libreria werkzeug.security para el hashing de contraseñas.

1. Crear nuevo usuario con el formulario de registro.
2. Autenticar usuario con formulario de inicio de sesión
3. Enviar usuario autorizado a la página de inicio

Con las sgtes Validaciones:
•   Usuario y contraseña Vacía.
•   Usuarios y Contraseña Correcta.
•   Usuario y Contraseña Incorrecta.
•   Usuario Bloqueado.
•   Intentos Fallido de inicio de sesión.


###

## Getting Started
- Instalar Python 3.7  `brew install python3 ` Mac
- Creacion de un Environment con Virtualenv `Python3 -mvenv project`
- Instalar dependencias, packages `pip -r install requirements.txt`
- Crear una base de datos vacía
```
cd flask-simple-login/
python
>>> from login_app import create_db
>>> create_db()
```

- Correr la aplicacion `python login_app.py`
- crear una nueva cuenta de usuario  http://127.0.0.1:5000/signup
- Iniciar sesion  http://127.0.0.1:5000/login
