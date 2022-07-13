from flask_restful import Resource

class ParticipanteController(Resource):
    #Esta clase funciona como controlador, al definir un método get
    def get(self):
        return{"example message"}