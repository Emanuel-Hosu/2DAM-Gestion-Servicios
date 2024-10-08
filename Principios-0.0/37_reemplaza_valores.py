lista = []
usuario = 0

while usuario != -1:
    usuario = int(input("Crea la lista || Introduce -1 para salir "))
    
    if usuario != -1:
        lista.append(usuario)
        
remplazar = int(input("Introduce el numero que desas reemplazar"))

if remplazar not in lista:
    print("El numero no existe en la lista")
    
remplazador = int(input("Introduce el numero por el que lo quieras reemplazar"))

for i in lista:
    if i == remplazar:
        i = remplazador
        
print(lista)