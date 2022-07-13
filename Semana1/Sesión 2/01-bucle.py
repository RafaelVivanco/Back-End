
# frase_motivadora = "Al que madruga, encuentra todo cerrado"
# contador = 0

# for caracter in frase_motivadora:
#     if caracter == "n":
#         contador += 1 #es como decir: contador = contador + 1

# print("hay {} letras n".format(contador))

# for valor in range(10):
#     print(valor)

# for valor in range(3,7):
#     print(valor)

# for valor in range(3,7,1):
#     print(valor)

na  = [10,30,12,17,24,67]
contador_pares: 0
contador_2: 0
# % MUESTRA EL RESIDUO DE LA DIVISIÓN => 10%2 = 0
# / MUESTRA EL COCIENTE DE LA DIVISÓN => 10/2 = 5
for number in na:
    if number%2 == 0:
        contador_pares += 1
    if number%3 == 0:
        print(number)
        contador_2 += 1

print("hay {} números pares y {} múltiplos de 3")

for valor in range(0,10000):
    if valor == 600:
        print("El usuario fue encontrado")
        break
#CONTINUE omite lo de abajo en la primera ronda
for valor in range(0,20):
    if(valor == 5):
        print("El usuario fue encontrado")
        continue
    print(valor)


for valor in range(0,20):
    pass

