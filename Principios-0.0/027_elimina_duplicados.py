lista = [3, 5, 4, 2, 3, 5, 9, 3]

n = len(lista)
for i in range(n):
    for h in range(n - 1):
        if lista[h] > lista[h + 1]: 
            lista[h], lista[h + 1] = lista[h + 1], lista[h]

lista_unica = []

for h in range(n - 1):
    if lista[h] != lista[h + 1]:
            lista_unica.append(lista[h])
        

print("Lista ordenada:", lista_unica)
