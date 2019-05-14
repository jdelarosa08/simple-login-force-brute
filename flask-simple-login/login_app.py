"""
Simple Modulo Web para Login
Implementado con Python, Flask y Flask-Sqlalchemy
Haciendo uso de libreria werkzeug.security para el hashing de contraseñas.

1. Crear nuevo usuario con el formulario de registro.
2. Autenticar usuario con formulario de inicio de sesión
3. Enviar usuario autorizado a la página de inicio

Con las sgtes Validaciones:
•   Usuario y contraseña Vacía.
•   Usuarios y Contraseña Correcta.
•   Usuario y Contraseña Incorrecta.
•   Usuario Bloqueado.
•   Intentos Fallido de inicio de sesión.

"""
# librerias
from flask import Flask, render_template, request, url_for, redirect, flash, \
session, abort
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


# Para asignar un nombre a la base de dato.
db_name = "auth.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# SECRET_KEY Esto es requerido para trabajar con las Sesiones Flash y Flask Sqlalchemy
app.config['SECRET_KEY'] = 'M-8_+vng#^DfTw7H' # Ingresar una Clave secreta de alta nivel, Aqui

db = SQLAlchemy(app)

# Creando el Modelo para Usuario
class User(db.Model):
   uid = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(100), unique=True, nullable=False)
   pass_hash = db.Column(db.String(100), nullable=False)
   failed = db.Column(db.Integer, nullable=True)

   def __repr__(self):
       return '' % self.usuario


def create_db():
   """ # Ejecutar esto primero para crear una nueva db en el directorio. """
   db.create_all()

# Método para creación de usuario y decorador para los request.
@app.route("/signup/", methods=["GET", "POST"])
def signup():
   """
   Este metodo implementa:
   - La funcionalidad de registro.
   - Permite crear un nombre de usuario y contraseña para un nuevo usuario.
    - Realiza un Hash a la contraseña con utilizando werkzeug.security.
    - Almacena el nombre de usuario y la contraseña hash dentro de la base de datos.
    - El nombre de usuario debe ser único de lo contrario, se genera una execcion de sqlalchemy.exc.IntegrityError.
   """

   if request.method == "POST":
       username = request.form['username']
       password = request.form['password']

       if not (username and password):
           flash("EL Usuario y/o Contraseña no pueden estar vacío.")
           return redirect(url_for('signup'))
       else:
           username = username.strip()
           password = password.strip()

       # Devuelve la Contraseña hashada en formato: method$salt$hashedvalue
       hashed_pwd = generate_password_hash(password, 'sha256')

       new_user = User(username=username, pass_hash=hashed_pwd, failed=0)
       db.session.add(new_user)

       try:
           db.session.commit()
       except sqlalchemy.exc.IntegrityError:
           flash("El Usuario {u} no esta disponible.".format(u=username))
           return redirect(url_for('signup'))

       flash("El Usuario ha sido Creado.")
       return redirect(url_for("login"))

   return render_template("signup.html")

# Método para Inicio de sesión y sus decorador para los diferentes request.
@app.route("/", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
   """
    Proporciona funcionalidad de inicio de sesión al representar el formulario de inicio de sesión en la solicitud de obtención.
    En las entradas se verifica el hash de la contraseña de db para el nombre de usuario y la contraseña de entrada dados.
    En la  entrada se verifica los intentos fallidos del usuario y de superar el máximo bloquear este.
    Si el usuario, el hash  y el número de intentos son menor al valor asignado , redirige al usuario autorizado a la página de inicio;
    Página de inicio de sesión con mensaje de error.
   """

   if request.method == "POST":
       username = request.form['username']
       password = request.form['password']

       if not (username and password):
           flash("El Usuario o Contraseña no pueden estar vacíos.")
           return redirect(url_for('login'))
       else:
           username = username.strip()
           password = password.strip()

       user = User.query.filter_by(username=username).first()
       if user:
           failed = user.failed
      
           if user and check_password_hash(user.pass_hash, password) and failed < 5:
               user.failed = 0
               print(user.failed)
               db.session.commit()
               session[username] = True
               return redirect(url_for("user_home", username=username))
          
           elif user and check_password_hash(user.pass_hash, password) == False and failed < 5:
               user.failed = failed + 1
               print(user.failed)
               db.session.commit()
               flash("Usuario y/o Contraseña Inválida.")
          
           elif user and failed == 5:
               flash("Usuario Bloqueado")

       else:
           flash("Usuario y/o Contraseña Inválida.")
      
   db.session.commit()
   return render_template("login_form.html")

# Método para home y decorador para el request con un usuario.
@app.route("/user/<username>/")
def user_home(username):
   """
   Página Principal para Usuarios Autorizados.
   """
   if not session.get(username):
       abort(401)
   return render_template("user_home.html", username=username)

# Método para Cierre de sesión y decorador para el request con un usuario.
@app.route("/logout/<username>")
def logout(username):
   """ Cerrar sesión de usuario y redirigir a la página de inicio de sesión con un mensaje de éxito."""
   session.pop(username, None)
   flash("Su sesión ha sido cerrada.")
   return redirect(url_for('login'))


if __name__ == "__main__":
   app.run(port=5000, debug=True)










