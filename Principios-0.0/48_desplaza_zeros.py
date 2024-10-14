numeros = [0, 1, 0, 3, 12, 0, 5]
numeros2 = []

for i in numeros[:]:
    if i != 0:
        numeros2.append(i)
        numeros.remove(i)
        
numeros2.extend(numeros)

print(numeros2)
