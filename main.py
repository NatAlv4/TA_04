#se agrego flask
from flask import Flask, render_template, send_file

app = Flask('app')

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
app.run(host='0.0.0.0', port=8080, debug=True)
