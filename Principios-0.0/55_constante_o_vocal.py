letra = input("introduce un caracter")

consonantes = ["q","w","e","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
vocales = ["a", "e", "i", "o", "u"]

match letra:
    case letra if letra in vocales:
        print("La letra es una vocal")
    case letra if letra in consonantes:
        print("La letra es una consonante")
    case _:
        print("La letra es un cacater especial")