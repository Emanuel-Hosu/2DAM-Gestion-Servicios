lista = ['sol', 'joker','joker', 'sol']
mitad = int(len(lista) / 2);
compobador = False

i = 0
n = 0

while(i <= mitad - 1):
    n -= 1
    i += 1

    if lista[i - 1] == lista[n]:
        compobador = True
    else:
        compobador = False
        
if (compobador == True):
    print("La lista es polindroma")
else:
    print("La lista no es polidroma")