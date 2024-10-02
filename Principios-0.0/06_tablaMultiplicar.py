multiplicador = int(input("Introduce un multiplicador "))
final = int(input("Hasta donde multiplicamos "))

for i in range(1, final + 1):
    resultado = i * multiplicador;
    print(multiplicador, " x ", i, " = ", resultado)


    