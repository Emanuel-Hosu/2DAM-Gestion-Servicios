lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
guardar = lista[0]
lista[0] = lista[-1]
lista[-1] = guardar

print(lista)