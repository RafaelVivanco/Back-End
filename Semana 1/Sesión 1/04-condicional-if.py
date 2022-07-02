edad_joel = 35

if edad_joel >=18 :
    print("Entra noma papai")
else:
    print("No, ahí nomas")

edad_marin = 5
if edad_marin >= 65:
    print("jubilado hdp")
elif edad_marin >= 18:
    print("eres mayor de edad")
elif edad_marin >=0:
    print("eres menor de edad")
else:
    print("edad imposible no me huevees")

# Para que se agrege un valor a las variables
data = int(input("Ingresa cuanto ganas al mes: "))
print(type(data))

dato = str(input("Ingresa el nombre de tu abuelo paterno: "))
print(type(dato))

talla = str(input("Ingresa tu talla de polo: ")).lower() #.lower() transforma el string a minúscula

if talla == "xl":
    print("esta talla llegará para fines de mes")
elif talla == "l" or "m":
    print(input("Ingesa el color del polo: "))
elif talla == "s":
    print("Solo hay color Morado")
else:
    print("la talla es incorrecta")