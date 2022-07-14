from flask_restful import Resource
from config import conexion
from models.participante import Participante

class ParticipanteController(Resource):
    #Esta clase funciona como controlador, al definir un método get
    def get(self):
        resultado = conexion.session.query(Participante)
        return{"message":"example message"}
    #los únicos datos que se pueden retornar son diccionarios, arreglos, string, booleans, int
    def post(self):
        return{
            "message":"Ingreso al post"
        }