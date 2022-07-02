edad_alljo = 20
edad_yo = 5

#OPERADORES ARITMÉTICOS
# RESTA
print(edad_alljo - edad_yo) 
# SUMA
print(edad_alljo + edad_yo)
# DIVISIÓN
print(edad_alljo / edad_yo)
# MULTIPLICACIÓN
print(edad_alljo * edad_yo) 
# MÓDULO, da el cociente entero de una divisón
print(edad_alljo // edad_yo) 

# mes="Junio"
# print ("""
# {}""".format(mes*5))
# print ("""
# {}""".format(mes)*5)

# print("{} - {}".format(edad_alljo,edad_yo))
# print("{}".format(edad_alljo - edad_yo))

#OPERADORES DE COMPARACIÓN
# > Mayor que
print(edad_alljo > edad_yo)
# > Menor que
print(edad_alljo < edad_yo)
# > Igual que
print(edad_alljo == edad_yo)
# > Diferente que
print(edad_alljo != edad_yo)
# > Mayor igual que
print(edad_alljo >= edad_yo)
# > Menor igual que
print(edad_alljo <= edad_yo)

#OPERADORES LÓGICOS
# and Y > basta con que una de las dos preposiciones sea F para que salga False
print(edad_yo > 20 and edad_alljo > edad_yo)
# or O > basta con que una de las dos preposiciones sea T para que salga True
print(edad_yo > 20 or edad_alljo > edad_yo)
# not NO >invierte resultado
print(not edad_alljo > edad_yo)

#OPERADORES DE ASIGNACIÓN
# = ASIGNACIÓN
edad = 50
# += INCREMENTO
edad += 1
print(edad)
# -= DECREMENTO
edad -= 1
print(edad)
# *= MULTIPLICAR
edad *=1
print(edad)

#Ejercicios
edad_eduardo = 18
edad_renato = 26
edad_laura = 35

print("¿Eduardo es mayor de edad?:", edad_eduardo >= 18)
print("¿Eduardo es mayor que Laura:", edad_eduardo > edad_laura)
print("¿Renato es mayor que Eduardo pero menor que Laura?:", edad_renato > edad_eduardo and edad_renato < edad_laura)
print("¿Laura puede ser mayor que renato o menor que eduardo?:", edad_laura > edad_renato or edad_laura < edad_eduardo)