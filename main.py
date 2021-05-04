#se agrego flask
from flask import Flask, render_template, send_file, request,redirect, url_for
import sqlite3
from datetime import datetime


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
  #Tabla de foro
  c.execute('CREATE TABLE IF NOT EXISTS foro(titulo TEXT NOT NULL, texto TEXT, nombre TEXT)')
  con.commit()
  c.close()

  
except error:

    print(error)
finally:

    con.close()

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
    password = request.form.get('password')
    data = c.execute('SELECT * FROM users WHERE email = ?', (email,))
    c.close()
    if data:
      return redirect(url_for('sign_up'))
    else:
      c = con.cursor()
      c.execute('INSERT INTO users(nombre, apellido, email, password) VALUES (?,?,?,?)', (nombre, apellido,email, password))
      con.commit()
      c.close()
      return redirect(url_for('index'))
  
  return render_template("sign_up.html")     


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
    c.execute('INSERT INTO medical(nombre, edad, sexo, contacto, medicamento, adicional) VALUES (?,?,?,?,?,?)', (nombre, edad,sexo, contacto, medicamento, adicional))
    con.commit()
    c.close()
    
    return redirect(url_for('servicios'))
   
 return render_template("historia_medica.html")  

@app.route('/servicios')
def servicios():
  return render_template("servicios.html")

#Ruta base del foro
@app.route('/foro')
def foro():
  #conexión base de datos
  con = sqlite3.connect('database.db')
  #Cursor
  c = con.cursor()
  
  #Se seleccionan los elementos de la base de datos
  c.execute('SELECT * FROM  foro')
  posts = c.fetchall()
  c.close()
  
  #posts=posts es para pasar todos los posts
  return render_template("foro.html", posts=posts) 

#Ruta donde se agregan los posts
@app.route('/agregar_entrada')
def agregar_entrada():
  
  return render_template("agregar_entrada.html")

@app.route('/crear', methods = ('GET', 'POST'))
def crear_post():  
  #conexión base de datos
  con = sqlite3.connect('database.db')
  #Cursor
  c = con.cursor()
  titulo = request.form.get("titulo")
  texto = request.form.get("texto")
  

  print (titulo, texto)

  c.execute('INSERT INTO foro(titulo, texto) VALUES(?,?)', (titulo, texto))
  con.commit()
  c.close()
  return  redirect(url_for('foro'))

@app.route('/calendar')
def calendar():  
  return render_template("calendar.html")


app.run(host='0.0.0.0', port=8080, debug=True)