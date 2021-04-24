#se agrego flask
from flask import Flask, render_template, send_file
import sqlite3
app = Flask('app')

#importa sql alchemy
#from flask_sqlalchemy import SQLAlchemy

#conexión de la base de datos
con = sqlite3.connect('database.db')
#Creacion del cursor de la base de datos
c = con.cursor()


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'


#variable que permite hacer consultas a la base de datos
#db = SQLAlchemy(app)


#creación de rutas
@app.route('/')
def index():
 return render_template ("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/sign_up')
def sign_up():
  return render_template("sign_up.html")

@app.route('/Pswrd_R')
def password():
  return render_template("Password_Recovery.html")

  

""""
@app.route('/sign_up')
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
      flash("Cuenta creada :D", category= 'success')
       #Añadimos el usuario a la base de datos
  return render_template("sign_up.html")

"""


  
app.run(host='0.0.0.0', port=8080, debug=True)