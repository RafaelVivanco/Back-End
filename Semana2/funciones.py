
def idioma():
    print("SELECCIONAR IDIOMA")
    print("ESPAÑOL", "FRANCÉS", "ITALIANO", "JAPONÉS")
    eleccion_idioma = input("Escribe tu opción: ")
    
    if eleccion_idioma == "ESPAÑOL":
        print("Hola {}, un gusto".format("Rafael"))
    elif eleccion_idioma == "FRANCÉS":
        print("Bonjour {}, ravi de vous rencontrer.".format("Rafael"))
    elif eleccion_idioma == "JAPONÉS":
        print("こんにちは {}, はじめまして".format("Rafael"))
    elif eleccion_idioma == "ITALIANO":
        print("Ciao {}, a piacere".format("Rafael"))
    else:
        print("Vuelve a escribir tu idioma, recuerda que debe estar en mayúsculas")
        idioma()
        

idioma()

# def saludar(nombre):
#     print("Hola {}, un gusto".format(nombre))

# saludar("Rafael")
