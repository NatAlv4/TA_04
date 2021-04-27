#se agrego flask
from flask import Flask, render_template, send_file, request,redirect, url_for
import sqlite3

app = Flask('app')
#Creacion de base de datos y sus correspondientes base de datos
try:
  #conexión de la base de datos
  con = sqlite3.connect('database.db')
  #Creacion del cursor de la base de datos
  c= con.cursor() 
  #Se crea la tabla de usuarios   
  c.execute('CREATE TABLE IF NOT EXISTS users(nombre TEXT NOT NULL, apellido TEXT, email TEXT NOT NULL, password TEXT NOT NULL)')
  #Tabla de historia medica
  c.execute('CREATE TABLE IF NOT EXISTS medical(nombre TEXT NOT NULL, edad TEXT, sexo TEXT NOT NULL, contacto TEXT NOT NULL, medicamento TEXT NOT NULL, adicional TEXT NOT NULL)')
  con.commit()
  c.close()
except error:

    print(error)
finally:

    con.close()

'''
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
  c.execute('INSERT INTO userstable(nombre, apellido, email, password) VALUE (?,?,?,?)',(nombre, apellido, email, password))
  con.commit()
  c.close()

#funcion para seleccionar valores de las tablas
def login_user(nombre, apellido, email, password):
  c.execute('SELECT * FROM userstable WHERE email = ?  AND password = ?', (email, password))
  data = c.fetchall()
  return data
  c.close()
'''
#creación de rutas
@app.route('/')
def index():
 return render_template ("index.html")


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/login', methods = ('GET', 'POST'))
def login():
  if request.method == 'POST':
    #conexión con la base de datos
    con = sqlite3.connect('database.db')
    #Creacion del cursor
    c = con.cursor()
    email = request.form.get('email')
    password = request.form.get('password')
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    passw = c.fetchone()[-1]
    c.close()
    if passw==password:      
      return redirect(url_for('historia_medica'))  
    else:
      return redirect(url_for('login')) 
    
  return render_template("login.html")

@app.route('/log_out')
def log_out():
  return render_template("log_out.html")

@app.route('/sign_up', methods = ('GET', 'POST'))
def sign_up():
  if request.method == 'POST':
    #conexión con la base de datos
    con = sqlite3.connect('database.db')
    #Creacion del cursor
    c = con.cursor()
    nombre= request.form.get('nombre')
    apellido = request.form.get('apellido')
    email= request.form.get('correo')
    contraseña = request.form.get('contraseña1')
    contraseña2 = request.form.get('contraseña2')
    c.execute('INSERT INTO users(nombre, apellido, email, password) VALUES (?,?,?,?)', (nombre, apellido,email, contraseña))
    con.commit()
    c.close()
    return redirect(url_for('index'))
  
  return render_template("sign_up.html")    
    

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


''''
#funcion para insertar valores a las tablas
def add_userdata(nombre, sexo, contacto, medicamento,adicional):
  d.execute('INSERT INFO userstable(nombre, edad, sexo, contacto, medicamento, adicional) VALUE (?,?,?,?,?,?)',(nombre, sexo, contacto, medicamento,adicional))
  con.commit()
  d.close()

'''

@app.route('/historia_medica', methods = ('GET', 'POST'))
def historia_medica():
  
 if request.method == 'POST':
    con = sqlite3.connect('database.db')#base de datos para el alojamiento de archivos de usuario 
    c = con.cursor() #Se crea el cursor
    #Se obtienen los datos recuperados del formulario de sign up
    nombre=request.form.get('name')
    edad= request.form.get('edad')  
    sexo = request.form.get('role')
    contacto= request.form.get('contacto')
    medicamento = request.form.get('comment')
    adicional=request.form.get('adicional')
     #Se agregan los datos a la base de datos
    c.execute('INSERT INTO userstable(nombre, edad, sexo, contacto, medicamento, adicional) VALUES (?,?,?,?,?,?)', (nombre, edad,sexo, contacto, medicamento, adicional))
    con.commit()
    c.close()
    
    return redirect(url_for('index'))
   
 return render_template("historia_medica.html")  

  



  

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