# PILARES
# 1. Abstracción (buscar similitudes y eliminar diferencias)
# 2. Encapsulamiento
# 3. Herencia
# 4. Polimorfismo

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__serie = marca+modelo
#se pone "__" antes del atributo para hacerlo privado (que no se pueda imprimir fuera el class)
    def mostrarSerie(self):
        print(self.__serie)

auto = Vehiculo("Kia", "Picanto")
camion = Vehiculo("Volvo", "F30")
print(auto.marca)
auto.mostrarSerie()
#así si se puede mostrar el atributo privado