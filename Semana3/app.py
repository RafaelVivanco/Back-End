from flask import Flask
from config import conexion
from models.participante import Participante
# environ > devuelve variables de entorno en un diccionario
from os import environ
# load_dotenv carga las variables declaradas del .env como si fueran variables de entorno para que puedan ser accedidas
# por el environ
from dotenv import load_dotenv
#se coloca esto para que la función reconozca la carpeta .env
load_dotenv()

app = Flask(__name__)

#URI = dialecto (mysql):// usuario:password@host:puerto/basededatos
app.config["SQLALCHEMY_DATABASE_URI"] = environ["DATABASE_URL"]

# Inicializo mi conexion de mi sqlalchemy con la bd pero sin conectarme
conexion.init_app(app)

#Se activa o desactiva el seguimiento a las modificaciones (Evitar Warnings)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Se ejecuta la creacióm y se crean las tablas PERO sin o hay ninguna tabla por
#crear entonces no lanara error de credencial inválido
conexion.create_all(app=app)

if __name__ == "__main__":
    app.run(debug=True)