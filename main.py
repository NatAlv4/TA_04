from flask import Flask, render_template, send_file
app = Flask('app')
#se agrego flask

@app.route('/')
def index():
 return render_template ("index.html")


@app.route('/about')
def about():
  return render_template("about.html")


app.run(host='0.0.0.0', port=8080, debug=True)
