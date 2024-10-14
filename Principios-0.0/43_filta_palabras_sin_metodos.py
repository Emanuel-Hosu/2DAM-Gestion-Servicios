user = input("Inserta la letra que queras cambiar")
palabras = ["sol", "luna", "mar", "estrella", "cielo"]  

for i in palabras:
    if i[0] == user:
        print(i)