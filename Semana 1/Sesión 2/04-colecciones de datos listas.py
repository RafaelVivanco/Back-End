alumnos = ["JAVIER", "ALEJANDRO", "MIGUEL", "NOSE XD"]

otra = [1,10,"hola",True,1.5,None]

# Estas listas son colecciones de arreglos ordenados

variados = [1, [3,2,4]]
print(variados[1][1])

#Para crear una sublista virtual dentro de la lista inicial, se hace el [1:3] donde 1 es el inicial y 3 sería igual que decir hasta la posición >3
print(alumnos[1:3])
print(alumnos[-1])

#Cambia un elemento según su posición
alumnos[0] = "MARTIN"
print(alumnos)

#Agrega un elemento al final de la lista
alumnos.append("RAFAEL")
print(alumnos)

#Formas para agregar elementos a la lista
alumnos.extend(["LOCONAZO", "AQUINO", "DUXO" ])
print(alumnos)
alumnos += ["McDonalds, Kfc, Bembos"]
print(alumnos)

# Eliminar elemento de la lista según su posición
del alumnos [1]
print(alumnos)

# Elimina el elemento según su posición pero se puede contener en otra variable
alumno_eliminado = alumnos.pop(2)
print(alumnos)
print(alumno_eliminado)