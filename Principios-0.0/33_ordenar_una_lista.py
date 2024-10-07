lista = [3, 2, 1, 5, 2, 1, 56, 6, 7, 8, 2, 7, 1]
guardar = 0

for i in range(0, len(lista)):
    for j in range(0, i):
        if (lista[i] > lista[j]):
            guardar = lista[i]
            lista[i] = lista[j]
            lista[j] = guardar
            
lista.reverse()
  
print(lista)
