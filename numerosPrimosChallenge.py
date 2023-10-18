def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

# Generar una lista de números primos entre 1 y 250
primos = [numero for numero in range(1, 251) if es_primo(numero)]

# Almacenar los números primos en el archivo results.txt
with open("results.txt", "w") as archivo:
    for primo in primos:
        archivo.write(str(primo) + "\n")

# Mostrar los números primos en la consola
for primo in primos:
    print(primo)