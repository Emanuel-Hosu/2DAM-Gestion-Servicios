lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mitad = len(lista)

if (mitad % 2 != 0):
    print(lista[int(mitad / 2)])
else:
    mitad_mitad = int(mitad/2)
    print (lista[mitad_mitad - 1], lista[mitad_mitad])
    