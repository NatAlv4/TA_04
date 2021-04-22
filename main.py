#se agrego flask
from flask import Flask, render_template, send_file, request, redirect, url_for, flash

#------------------------------------------nuevo 

from .models import User
#la siguiente libreria y los elemento importados permiten procesar la contraseña de modo que esta sea aprobada rspecto al usuario en el login sin que esta sea revelada en caso de que la contraseña ingresada sea la incorrecta
from werkzeug.security import generate_password_hash, check_password_hash  


#esta libreria nos ayuadara en la verificacion de datos en la base de datos,de modo que no se repitan entradas
from os import path

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "base_de_datos.db"

def create.app():
  app.config['SQLAlchemy_DATABASE.URI'] = f'sql_lite:///{DB_NAME}'
  db.init_app(app)

  from .models import User, note
  create_datebase(app)

#se verifica si la base de datos esta creada, en caso de que no, se crea 
def create_datebase(app):
  if not path('Templates/' + DB_NAME):
    db.create_all(app=app)
    print('base de datos creada!')


# se importa verificador de contraseñas
from werkzeug.security import generate_password_hash, check_password_hash

#------------------------------------------nuevo

app = Flask('app')

#creación de rutas
@app.route('/')
def index():
 return render_template ("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

#Se crea ruta de login, para procesar datos de inicio de sesion
@app.route('/login', methods = ["GET", "POST"])
def login():
  #solicitar email y password
  email = request.form.get('email')
  password = request.form.get('password')
  return render_template("login.html")
  

#Se crea ruta de sign up, para procesar datos de registro
@app.route('/sign_up', methods=['GET', 'POST'])
#Se crea la funcion para identificar si se han enviado los datos del formulario (con POST)

def sign_up():
  if request.method == 'POST':
    nombre= request.form.get('nombre')
    apellido = request.form.get('apellido')
    email= request.form.get('email')
    contraseña1 = request.form('contraseña1')
    contraseña2 = request.form('contraseña2')

    #Se validan los datos  

    if len(email) < 4:
      flash("El correo debe de contener más de 3 caracteres.", category = 'error')
    elif len(nombre) < 2:
      flash("El nombre debe de contener mínimo 2 caracteres.", category = 'error')
    elif  contraseña1 != contraseña2:
      flash("Las contraseñas deben de coincidir.", category= 'error')
    elif len(contrtaseña) <7:
      flash("La contraseña debe de contener por lo menos 7 caracteres", category = 'error')
    else:
      #------------------------------------------nuevo 
      #creacion de nuevo usuario
      new_user = User(email=email, nombre=nombre, contraseña= generate_password_hash(contraseña1, method='sha256' ))
      db.sesion .add(new_user)
      db.session.commit()
      #------------------------------------------nuevo 

      flash("Cuenta creada :D", category= 'success')
       #Añadimos el usuario a la base de datos
       
    #se usa el parametro para redirigir al usuario a la pagina de inicio luego de completar el formulario
    next = request.args.get('next', None)
    if next:
      #si no se llena el fomrulario, se devuelve a la pagina de registro
      return redirect(next)
    return redirect(url_for('/')) 
  return render_template("sign_up.html")



# creamos una ruta de acceso para procesar la recuperacion de la contraseña
@app.route('/Pswrd_R', methods = ["GET", "POST"] )
def password():
  return render_template("Password_Recovery.html")

#definimos la funcion que identificará los datos enviados en el formulario

def recovery():
  if request.method == 'POST':
    username = reques.form.get['nombre de usuario']
    email= request.form.get['correo electronico'] 

    # el siguiete bloque if relacionara el nombre de ususario y el correo electronico para verificar que los datos de cuenta a cambiar sean los correctos

''' pendiente por determinar la ruta de llamada del username y email
    if username != ###: 
      flash('el nombre de usuario esta incorrecto', category='error')
    elif email != ###:
      flash('El correo electronico esta incorrecto', category='error')
    else:
      flash('datos verificados correctamente')

  return render_template("Password_Recovery.html")
'''   


app.run(host='0.0.0.0', port=8080, debug=True)