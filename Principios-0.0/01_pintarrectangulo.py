anchura = int(input("Dime la anchura de rectángulo "))
altura = int(input("Dime la altura del rectangulo "))


#range(inicio, fin, incremento)
for i in range (altura):
    for h in range(anchura):
        print("*", end="")
    print()