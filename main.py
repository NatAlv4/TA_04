#se agrego flask
from flask import Flask, render_template, send_file, request,redirect, url_for, session
import sqlite3
from datetime import datetime
#se importa extensión Flask Mail
from flask_mail import Mail, Message


app = Flask('app')
#Creacion de base de datos y sus correspondientes base de datos
app.secret_key = "hola123"
#SMTP permite enviar correos, en este caso se usan los ajustes de GMAIL
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
#protocolo TLS es de encriptado de datos servidor-usuario, de acuerdo al protocolo es asignado el numero de puerto
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#Nombre de usuario del servidor smtp
app.config['MAIL_USERNAME'] = mail_username="elproyectowhy@gmail.com"
#Contraseña del usuario del servidor smtp
app.config['MAIL_PASSWORD'] = mail_password="hola123@"
#Se crea un default sender, para que todos los correos salgan del mismo correo
app.config['MAIL_DEFAULT_SENDER'] = "elproyectowhy@gmail.com"
#se define la variable mail, la cual se usa una vez definida la ruta 
mail=Mail(app)

app.secret_key = "hola123"
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
  #Tabla del calendario
  c.execute('CREATE TABLE IF NOT EXISTS eventos(titulo TEXT, fecha TEXT, email TEXT, comentario TEXT)')
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
    session["email"] = email #Se guarda el email en la sesion
    password = request.form.get('password')
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    passw = c.fetchone()[-1]
    c.close()
    if passw==password:      
      return redirect(url_for('servicios'))  
    else:
      return redirect(url_for('Los datos ingresados no concuerdan, intentalo de nuevo'))
    
    
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
@app.route('/password_recovery')
def 
'''
@app.route('/historia_medica', methods = ('GET', 'POST'))
def historia_medica():
  if  "email" in session: #Se verifica que se haya iniciado sesion, para poder acceder a la historia medica
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
  else:
    return redirect(url_for('login'))
      
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
  if  "email" in session: #Se verifica que se haya iniciado sesion, para poder acceder a la historia medica
    return render_template("agregar_entrada.html")
  else:
    return ('No has iniciado sesion, intentalo de nuevo')  

@app.route('/crear', methods = ('GET', 'POST'))
def crear_post():  
  #conexión base de datos
  con = sqlite3.connect('database.db')
  #Cursor
  c = con.cursor()
  titulo = request.form.get("titulo")
  texto = request.form.get("texto")
  

  c.execute('INSERT INTO foro(titulo, texto) VALUES(?,?)', (titulo, texto))
  con.commit()
  c.close()
  return  redirect(url_for('foro'))

@app.route('/calendar')
def calendar():  
  return render_template("calendar.html")

@app.route('/agenda')
def agenda():
  if  "email" in session: #Se verifica que se haya iniciado sesion, para poder acceder a la agenda
  #conexión base de datos
    con = sqlite3.connect('database.db')
    #Cursor
    c = con.cursor()

    #c.execute('SELECT * FROM eventos WHERE  email = ?', (email,))
    #events = c.fetchall()
    #c.close()
    return render_template("agenda.html") #events=events)  
  else:  
    return redirect ('login')  

@app.route('/agregar_evento')
def agregar_evento():
  return render_template("agregar_evento.html")

@app.route('/crear_evento',  methods = ('GET', 'POST'))
def crear_evento():
  if  "email" in session:
    #conexión base de datos
    con = sqlite3.connect('database.db')
    #Cursor
    c = con.cursor()

    titulo = request.form.get("titulo")
    fecha = request.form.get("fecha")
    email = session["email"]
    comment = request.form.get("comment")

    
    c.execute('INSERT INTO eventos(titulo, fecha, email, comentario) VALUES (?,?,?,?)', (titulo, fecha, email, comment))
    return redirect ('agenda')
  else:  
    return redirect ('login')  


  
@app.route('/contact', methods = ('GET', 'POST'))
def contact():
  #se obtienen los datos ingresados con el metodo get
  if request.method == 'POST':
     name1 = request.form.get("name1")
     lastname1 = request.form.get("lastname1")
     email1 = request.form.get("email1")
     message1 = request.form.get("message1")
    #se crea instancia Message se definen nomnre de destinatario correo y cuerpo de mensaje
     msg = Message(
            subject=f"Mail from {name1}", body=f"Name: {name1}\nE-Mail: {email1}\n\n\n\n{message1}", sender=mail_username, recipients=['elproyectowhy@gmail.com'])
    #se llama la variable main y se envia con los ajustes aplicados en msg 
     mail.send(msg)
     return render_template("contact.html", success=True)
  return render_template("contact.html")


app.run(host='0.0.0.0', port=8080, debug=True)