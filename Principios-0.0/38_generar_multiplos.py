x = int(input("Indicame un numero "))
y = int(input("Cuantos multiplos quieres de x ")) 
resultado = 0

for i in range(0, y):
    resultado += x

print(resultado)

