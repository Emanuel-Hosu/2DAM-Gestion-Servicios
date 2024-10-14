lista = [-2, 10, 4, 20, 55, 12, 66, -5412]
comporbador = False

for i in lista:
    if i > 0:
        comporbador = True
    else:
        comporbador = False
        break
    
if comporbador == True:
    print("No hay numeros negativos en la lista")
else:
    print("ALERTA, HAY NEGATIVOS EN LA LISTA")