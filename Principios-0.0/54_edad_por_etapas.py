# Niño (0-12 años)
# Adolescente (13-17 años)
# Adulto (18-64 años)
# Anciano (65+ años)

user = int(input("Indica tu edad: "))

match user:
    case user if 0 <= user <= 12:
        print("Es un niño")
    case user if 13 <= user <= 17:
        print("Es un adolescente")
    case user if 18 <= user <= 64:
        print("Es un adulto")
    case user if user >= 65:
        print("Es un anciano")
    case _:
        print("Edad no válida")
