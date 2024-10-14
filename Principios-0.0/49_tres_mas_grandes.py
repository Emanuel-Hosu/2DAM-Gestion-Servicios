numeros = [10, 30, 15, 2, 45, 60, 5, 100, 35]
top3 = []


numeros.sort()
numeros.reverse()

for i in range(3):
    top3.append(numeros[i])
    
print(top3)