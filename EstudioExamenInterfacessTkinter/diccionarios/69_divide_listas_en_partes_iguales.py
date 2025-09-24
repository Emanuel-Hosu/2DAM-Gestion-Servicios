lista = [1, 2, 3, 4, 5, 6, 7]
divisor = 2

resultado = len(lista) // divisor
restante = len(lista) - resultado

print("Lista 1")
for i in range(0, resultado):
    print(lista[i])

print("Lista 2")
for i in range(restante - 1, len(lista)):
    print(lista[i])