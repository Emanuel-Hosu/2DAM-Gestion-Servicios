lista = [1, 2, 3, 3]
lista2 = [0] * len(lista)
counter = 0
position = 0

for i in lista:
    for j in lista:
        if i == j:
            counter += 1
    
    if i not in lista2:
        lista2[position] = i
        print(i, ":", counter)
        position += 1
    
    counter = 0
    
#print(lista2)