from flask import Flask
from flask import render_template
import a
import index
import funcionesrenfe as fr

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    s = "q taaaal"
    return render_template('prueba.html', name=s)

@app.route("/alumnos")
def lista_alumnos():
    return "Alumnos"

@app.route("/nombre/<s>")
def get_name(s):
    return render_template('index.html', name=s)

@app.route("/suma/<x>/<y>")
def suma():
    x=5
    y=2
    print(x+y)
    return render_template('prueba.html')

#@app.route("/setopc/<opc>")
#def setopc(opc):


@app.route("/selec_dest/")
def selec_dest():
    return fr.zonas


if __name__ == "__main__":
    app.run()