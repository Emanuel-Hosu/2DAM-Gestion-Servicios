user = int(input("Hasta donde quiueres sumar los numeros"))
resultado = 0

for i in range(1, user + 1):
    resultado += i

print("El resultado de su sumatorio es: ", resultado)