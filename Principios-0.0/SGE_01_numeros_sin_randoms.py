# Pedimos los datos al usuario
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))
cantidad = int(input("¿Cuántos números desea generar? "))

# Lista para guardar los números
numeros = []

# Generamos los números de forma simple
while len(numeros) < cantidad:
    for numero in range(minimo, maximo + 1):
        if len(numeros) < cantidad and numero not in numeros:
            numeros.append(numero)

# Mezclamos los números de forma simple
for i in range(len(numeros)):
    posicion = i + (71 * i + 31) % (len(numeros) - i)
    if posicion >= len(numeros):
        posicion = i
    numeros[i], numeros[posicion] = numeros[posicion], numeros[i]

print(f"Números generados: {numeros}")