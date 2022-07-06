def RecibirAlumnos(*alumnos): #El * significa que ese parámetro será convertido a tuple y son infinitos
    print(type(alumnos))
    print(alumnos)


RecibirAlumnos("Rafael", "Amir", "Carlos", "Ricardo", "Sebastián")
RecibirAlumnos("Rafael", "Amir", "Carlos", "Ricardo", "Sebastián", "Samy", "Bruno")