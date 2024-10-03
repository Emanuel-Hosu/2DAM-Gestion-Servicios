num = int(input("Introduce un numero"))
lista_primos = []

for i in range(1, num):
    cont = 0
    for h in range(1, i):
        if(i % h == 0):
            cont += 2
            
    if(cont == 2):
        lista_primos.append(i)
        
        
print(lista_primos)

#resultado = n / 2
#resultado % 2 = 0
#no es primo