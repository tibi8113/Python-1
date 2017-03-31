from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    s = "q taaaal"
    return render_template('index.html', name=s)

@app.route("/alumnos")
def lista_alumnos():
    return "Alumnos"

@app.route("/nombre/<s>")
def get_name(s):
    return render_template('index.html', name=s)

if __name__ == "__main__":
    app.run()