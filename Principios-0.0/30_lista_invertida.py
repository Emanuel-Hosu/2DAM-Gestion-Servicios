lista = [32, 5, 2, 6, 51, 52, 6, 3, 1, 4, 6, 8, 24, 73, 88, 12, 44, 5, 3, 6, 7, 2, 777, 62, 66] 
lista_invertida = []

n = len(lista)
h = 0

while h < n:
    lista_invertida.append(lista[n - h - 1])
    h += 1

print("Lista invertida:", lista_invertida)
