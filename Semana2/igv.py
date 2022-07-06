# igv = 0.18
# def GetIgv():
#     producto_igv = producto * igv
#     print("El igv de tu producto es: {}".format(producto_igv))
#     print("Y el precio sin igv sería:", producto - producto_igv)

# producto = int(input("Determina el precio de tu producto con igv: "))
# print("¿Quiéres sacar el igv de tu producto?", "SI O NO")
# elección = input().upper()

# if elección == "SI":
#     GetIgv()
# else:
#     print("Ok te dejo")


def CalcularSalarioMínimo(profesion, experiencia):
    salarioMínimo = 1050
    if profesion == "Desarrollador":
        if experiencia == "Basica":
            salarioMínimo = 3000
        elif experiencia == "Media":
            salarioMínimo = 6000
        elif experiencia == "Avanzada":
            salarioMínimo = 7000
    elif profesion == "Marketing":
        if experiencia == "Basica":
            salarioMínimo = 2500
        elif experiencia == "Media":
            salarioMínimo = 4150
        elif experiencia == "Avanzada":
            salarioMínimo = 6020
    return salarioMínimo

profesion, experiencia = "Desarrollador", "Media"
salario = CalcularSalarioMínimo(profesion, experiencia)
# print(salario)

Electrodomésticos = []

def registrarElectrodomésticos(objeto, precio, lugar, marca):
    Electrodomésticos.append({"objeto": objeto,"precio": precio, "lugar": lugar,"marca": marca})
    return True

registrarElectrodomésticos("Licuadora", 300, "Las Malvinas", "Oster")
registrarElectrodomésticos("Freidora de Aire", 1000, "Las Malvinas", "Takia")
registrarElectrodomésticos("Refrigeradora", 3900, "Cercado", "LG")
#print(Electrodomésticos)

LasMalvinas = 0
Cercado = 0
Otro = 0

for Electrodomestico in Electrodomésticos:
    if Electrodomestico["lugar"] == "Las Malvinas":
        LasMalvinas += 1
    elif Electrodomestico["lugar"] == "Cercado":
        Cercado += 1
    else:
        Otro += 1

print("Hay {} electroméstico(s) en el Cercado, {} electrodoméstico(s) en las Malvinas y {} electrodoméstico(s) en otro lugar".format(Cercado, LasMalvinas, Otro))

# if Electrodomésticos[0]["lugar"] == "Las Malvinas":
#     LasMalvinas += 1

# if Electrodomésticos[1]["lugar"] == "Las Malvinas":
#     LasMalvinas += 1

# if Electrodomésticos[2]["lugar"] == "Las Malvinas":
#     LasMalvinas += 1


# if Electrodomésticos[0]["lugar"] == "Cercado":
#     Cercado += 1

# if Electrodomésticos[1]["lugar"] == "Cercado":
#     Cercado  += 1

# if Electrodomésticos[2]["lugar"] == "Cercado":
#     Cercado  += 1

# print("Hay {} electroméstico(s) en el Cercado y {} electrodoméstico(s) en Las Malvinas".format(Cercado, LasMalvinas))


