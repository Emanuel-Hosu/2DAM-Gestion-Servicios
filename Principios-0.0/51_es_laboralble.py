user = input("Introduce un día");

match user:
    case "Lunes":
        print("Es laborable")
    case "Martes":
        print("Es laborable")
    case "Miercoles":
        print("Es laborable")
    case "Jueves":
        print("Es laborable")
    case "Viernes":
        print("Es laborable")
    case "Sabado":
        print("No es laborable")
    case "Domingo":
        print("No es laborable")
    case _:
        print("La entrada no es válida")