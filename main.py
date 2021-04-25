#se agrego flask
from flask import Flask, render_template, send_file, request,redirect, url_for
import sqlite3

app = Flask('app')


#import sql alchemy
#from flask_sqlalchemy import SQLAlchemy

#conexión de la base de datos
con = sqlite3.connect('database.db')
#Creacion del cursor de la base de datos
c = con.cursor()    
  
#Creacion de las tablas en la base de datos
def create_usertable():
  c.execute('CREATE TABLE IF NOT EXISTS userstable(id integer PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT, email TEXT NOT NULL, password TEXT NOT NULL)')
  con.commit()
  c.close()
#funcion para insertar valores a las tablas
def add_userdata(nombre, apellido, email, password):
  c.execute('INSERT INFO userstable(nombre, apellido, email, password) VALUE (?,?,?,?)',(nombre, apellido, email, password))
  con.commit()
  c.close()

#funcion para seleccionar valores de las tablas
def login_user(nombre, apellido, email, password):
  c.execute('SELECT * FROM userstable WHERE email = ?  AND password = ?', (email, password))
  data = c.fetchall()
  return data
  c.close()

#creación de rutas
@app.route('/')
def index():
 return render_template ("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/login', methods=['GET','POST'])
def login():

  #------------
  #conexion con la base de detos
  con = sqlite3.connect('database.db')
  cursorObj = con.cursor()

  #se crean la variables de correo y contraseña que seran definidas apartir del con tenido de la tabla
  email = request.form.get('correo')
  password = request.form.get('contraseña1')

  #de la tabla se llama todo el contenido de la misma que esta bajo la etiqueta de email y contraseña
  c.execute('SELECT * FROM userstable WHERE email = ?  AND password = ?', (email, password))
  data = c.fetchall()

  

  if email is not userstable:
    print('el correo introducido es no ha sido registrado')
  elif email != correo :
    print = ('el correo ingresado no coincide')
  elif password != password :
    print = ('La contraseña no coincide')
  else:
    print = ('Acceso exitoso')

  return data
  c.close()

  #-------------

  return render_template("login.html")

@app.route('/sign_up', methods = ('GET', 'POST'))
def sign_up():
  if request.method == 'POST':
    con = sqlite3.connect('datauser.db')#Se conecta a la base de datos
    c = con.cursor() #Se crea el cursor
    #Se obtienen los datos recuperados del formulario de sign up
    nombre= request.form.get('nombre')  #Se guarda en una variable los datos ingresados en el formulario, para posteriormente agregarlo a la base de datos 
    apellido = request.form.get('apellido')
    email= request.form.get('correo')
    contraseña = request.form.get('contraseña1')
     #Se agregan los datos a la base de datos
    c.execute('INSERT INTO userstable(nombre, apellido, email, password) VALUES (?,?,?,?)', (nombre, apellido,email, contraseña))
    con.commit()
    c.close()

    next = request.args.get('next', None)
    if next:
      return redirect(next)
    return redirect(url_for('index'))
  
  return render_template("sign_up.html")  

@app.route('/historia_medica', methods = ('GET', 'POST'))
def historia_medica():
  return render_template("historia_medica.html")
  ''''
if request.method == 'POST':
    con = sqlite3.connect('datauser.db')#base de datos para el alojamiento de archivos de usuario 
    c = con.cursor() #Se crea el cursor
    #Se obtienen los datos recuperados del formulario de sign up
    nombre= request.form.get('nombre')  #Se guarda en una variable los datos ingresados en el formulario, para posteriormente agregarlo a la base de datos 
    apellido = request.form.get('apellido')
    email= request.form.get('correo')
    contraseña = request.form.get('contraseña1')
     #Se agregan los datos a la base de datos
    c.execute('INSERT INTO userstable(nombre, apellido, email, password) VALUES (?,?,?,?)', (nombre, apellido,email, contraseña))
    con.commit()
    c.close()
  
  '''


''''
#este codigo define los datos de usuario
def add_user():
    user_form = UserForm()

    if request.method == 'POST':
        if user_form.validate_on_submit():
            # Get validated data from form
            name = user_form.name.data # You could also have used request.form['name']
            email = user_form.email.data # You could also have used request.form['email']

            # save user to database
            user = User(name, email)
            db.session.add(user)
            db.session.commit()

            flash('User successfully added')
            return redirect(url_for('show_users'))
'''

@app.route('/Pswrd_R')
def password():
  return render_template("Password_Recovery.html")

  

'''
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

'''


  
app.run(host='0.0.0.0', port=8080, debug=True)