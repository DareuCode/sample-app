# importamos los métodos Flask y request de la librería flask
from flask import Flask
from flask import request

# importamos render_templete
from flask import render_template

# Crear una instancia de la clase Flask.
sample = Flask(__name__)

# Definir un método para mostrar la dirección IP del cliente
@sample.route("/")
def main():
	# retornamos el templete renderizado.
	return render_template("index.html")

# Configurar la aplicación para que se ejecute localmente.
if __name__ == "__main__":
	sample.run(host="0.0.0.0", port=5050)
