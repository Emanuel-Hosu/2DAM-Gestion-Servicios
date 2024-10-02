import random

numero_random = random.randint(1, 10)
intentos = 0
trys = 0

print("Adivina el numero secreto entre 1 y 10")

while True:
    intento = int(input("Adivina el numero: "))
    trys = 1
    
    if intento == numero_random:
        print("FELICIDADES ADIVINASTE EL NUMERO EN ", trys, " INTENTOS")
        break
    elif intento < numero_random:
        trys += 1
        print("Demasiado bajo. Intenta de nuevo")
    elif intento > numero_random:
        trys += 1
        print("Demasiado alto intentalo otra vez")