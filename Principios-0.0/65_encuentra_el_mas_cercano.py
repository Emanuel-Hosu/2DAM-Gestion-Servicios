lista = [1, 2, 3, 4]
user = int(input("Introduce un número: "))

cercano = lista[0]

for i in lista:
    if (i - user) * (i - user) < (cercano - user) * (cercano - user):
        cercano = i

if cercano == user:
    print("El número está en la lista:", cercano)
else:
    print("El número más cercano es:", cercano)
