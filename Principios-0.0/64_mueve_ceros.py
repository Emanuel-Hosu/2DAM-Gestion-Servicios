lista = [3, 4, 1, 0, 9, 0, 1, 4, 2]

for i in lista:
    if i == 0:
        lista.remove(i)
        lista.append(i)

print(lista)