lista = [3, 2, 1, 5, 2, 1, 56, 6, 7, 8, 2, 7, 1, 1]

lista.sort()

guardado = 0
counter = 1
nr_max = lista[0]

for i in range(1, len(lista) - 1):
    if lista[i] == lista[i + 1]:
        counter += 1
    else:
        if counter > guardado:
            guardado = counter
            nr_max = lista[i]
            counter = 0
            
print("El numero mas repetido es: ", nr_max)
    
