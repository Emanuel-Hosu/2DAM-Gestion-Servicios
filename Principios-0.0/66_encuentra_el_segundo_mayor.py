lista = [3, 10, 4, 2, 5, 9]

max_nr = lista[0]

for i in lista:
    if max_nr < i:
        max_nr = i

segundo_mayor = lista[0]

for i in lista:
    if i > segundo_mayor & i < max_nr:
        segundo_mayor = i

print(segundo_mayor)
