usuario = int(input("Introduce el numero para hacer el factorial "))
resultado = 1;

for i in range(1, usuario + 1):
    resultado *= i
    
print("El factorial de su numero es: ", resultado)