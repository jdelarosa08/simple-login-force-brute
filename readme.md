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
- Instalar Python 3.7  `brew install python3 ` (Mac.) --- Windows usar el instalador
- Creacion de un Environment con Virtualenv `Python3 -mvenv project`.
- Instalar dependencias, packages `pip install -r requirements.txt`.
- Crear una base de datos vacía.
```
cd src/
python
>>> from app import create_db
>>> create_db()
>>> exit()
```

- Correr la aplicacion `python app.py`
- Crear una nueva cuenta de usuario  http://127.0.0.1:5000/signup
- Iniciar sesion  http://127.0.0.1:5000/login
