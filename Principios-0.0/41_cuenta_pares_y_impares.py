lista = [1, 2, 3, 5, 6, 7, 8, 9, 10]
pares = 0
impares = 0

for i in lista:
    if (i % 2 == 0):
        pares += 1
    else:
        impares += 1

print("La lista cuenta con ", pares, " numeros pares y ", impares, " numeros impares")