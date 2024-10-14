user = input("Inroduce un numero de 1 a 3 digitos: ")
tamanio = len(user)

match tamanio:
    case 3:
        print("Tenemos", user[0], " centenas, ", user[1], "decenas y ", ser[2], "unidad")
    case 2:
        print("Tenemos", user[0], "decenas ", user[1], "una unidad")
    case 1:
        print(user[0], "unidad")


