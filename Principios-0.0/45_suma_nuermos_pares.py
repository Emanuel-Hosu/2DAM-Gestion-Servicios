lista = [1, 2, 3, 5, 6, 7, 8, 9, 10]
sumar_pares = 0

for i in lista:
    if i % 2 == 0:
        sumar_pares += i
        
print(sumar_pares)