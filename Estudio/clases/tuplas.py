tupla = (3, 4, 5)

logintud = len(tupla)

if logintud == 1:
    print(f'Un solo numero {tupla}')
elif logintud == 2:
    print(f"La suma de los numeros es: {tupla[0] + tupla[1]}")
elif logintud == 3:
    print(f"Producto de la tupla: {tupla[0] * tupla[1] * tupla[2]}")
else:
    print("La tupla tiene mas de tres items")