from config import conexion
from sqlalchemy import VARCHAR, Column, PrimaryKeyConstraint, types

class Participante(conexion.Model):
    # ahora esta clase tendrá un comportamiento en forma de tabla en el bd
    # (todos los atributos que declare que sean propios de la bd serán columnas
    # parámetro = column(tipo = tipo.String(varchar))
    id = Column(type_ = types.Integer, autoincrement = True, primary_key = True)
    nombre = Column(type_ = types.String(50), nullable = False)
    apellido = Column(type_ = types.String(50), nullable = False)
    telefono = Column(type_ = types.String(10), nullable = False)
    password = Column(type_ = types.Text, nullable = False)
    zona = Column(type_ = types.Enum("SUPER VIP", "VIP", "GENERAL"),
    default = "GENERAL", nullable = False)
    comentario = Column(type_ = types.Text)
    telefono = Column(type_ = types.String(45), nullable = False)