lista = [32, 5, 2, 6, 51, 52, 6, 3, 1, 4, 6, 8, 24, 73, 88, 12, 44, 5,  3, 6 , 7, 2 , 777, 62, 66]
lista_mayor = []

usuario = int(input("Indica un numero"))
for i in lista:
    if i >= usuario:
        lista_mayor.append(i)
        
print("La nueva lista seria: ", lista_mayor)