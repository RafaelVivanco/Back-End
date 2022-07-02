#las tuplas son colecciones de datos no editables
#las tuplas van entre ()
profesores = ("Eduardo", "Sabiduría Joaquín")

print(profesores[1])

#profesores[0] = "Raul" #no se podría pq en las tuplas no se puede modificar

#Sirven para dar la posición de un elemento
#En este primero si no encuentra sale 0
print(profesores.count("Eduardo"))
print(profesores.count("no hay"))
#En este primero si no encuentra sale error
print(profesores.index("Eduardo"))