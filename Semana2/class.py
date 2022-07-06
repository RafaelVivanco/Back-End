class Persona:
    #atributos
    estatura = 170
    colorOjos = "Café"
    colorCabello = "Negro"
    raza = "Indígena"
    fechaNacimiento = "2005-10-12"

    def saludar(self):
        print("Hola buenos días")

# personaRafael = Persona()
# print(personaRafael.colorCabello)

# personaSamy = Persona()
# personaSamy.raza = "Negro"
# print(personaSamy.raza)

# personaSamy.saludar()

class Brawler:
    def __init__(self, nombre , health , damage , calidad):
        self.nombre = nombre
        self.health = health
        self.damage = damage
        self.calidad = calidad
    
    def info(self):
        print(self.nombre)
        print(self.health)
        print(self.damage)
        print(self.calidad)

brawlerNita = Brawler("Nita", 4500, 1500, "camino de trofeos")
brawlerLeon = Brawler("Leon", 4000, 2300, "legendario")

print(brawlerNita.nombre)
print(brawlerLeon.calidad)
brawlerLeon.info()


