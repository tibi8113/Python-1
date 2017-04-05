from flask import Flask
from flask import render_template


app = Flask(__name__)
app.debug = True

@app.route("/")
def principal():
    return render_template('prueba.html')

@app.route("/opc/<billete>")
def hello(billete):
    return "Has seleccionado la opción: " + billete


if __name__ == "__main__":
    app.run()