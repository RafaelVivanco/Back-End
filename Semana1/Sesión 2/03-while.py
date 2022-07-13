contador_numeros = 1 
while contador_numeros > 6:
    numero = int(input("Escribe un número de la loltería"))
    if numero > 0 and numero < 100:
        contador_numeros += 1
        continue
    print("número invalido, escriba nuevamente")
