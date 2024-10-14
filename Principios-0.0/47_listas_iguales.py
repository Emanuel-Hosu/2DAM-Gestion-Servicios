lista = ['sol', 'joker','sol', 'sol']
list2 = ['sol', 'joker','sol', 'sol']
comprobador = False

h = 0

for i in lista:
    if i == list2[h]:
        comprobador = True
    else:
        comprobador = False
        break
        
    h += 1
    
if comprobador == True:
    print("Listas iguales")
else:
    print("Las listas no son iguales")