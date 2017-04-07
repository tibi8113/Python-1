from flask import Flask
from flask import render_template
import funcionesrenfe as fr

app = Flask(__name__)
app.debug = True

@app.route("/")
def principal():
    return render_template('prueba.html')

@app.route("/opc/<billete>")
def hello(billete):
    koxme = fr.print_dest()
    return render_template('dest.html', billete=billete, estaciones=koxme)


@app.route("/destinos")
def destinos():
    fr.print_dest()

if __name__ == "__main__":
    app.run()