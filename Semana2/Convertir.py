def RecibirAlumnos(*alumnos): #El * significa que ese parámetro será convertido a tuple y son infinitos
    print(type(alumnos))
    print(alumnos)


RecibirAlumnos("Rafael", "Amir", "Carlos", "Ricardo", "Sebastián")
RecibirAlumnos("Rafael", "Amir", "Carlos", "Ricardo", "Sebastián", "Samy", "Bruno")

sumatoria = lambda numero1, numero2: numero1 + numero2
respuesta = sumatoria(10,4)
print(respuesta)

multiplicacion = lambda valor: valor * 1.8
producto = multiplicacion(39)
print(producto)