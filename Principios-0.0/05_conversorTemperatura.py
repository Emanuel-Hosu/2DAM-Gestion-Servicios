usuario = int(input("De que quieres calcular de || 1. Farengeir a Celcius || 2. Celsius a Farengeir"))

if usuario == 1:
    farengeir = float(input("Introduce los farengeir"))    
    print("El conversor de farengeir a celsius es: ", (farengeir - 32) / 1.8)
elif usuario == 2:
    celsius = float(input("Introduce los celsius")) 
    print("El conversor de celsius a farengeir es: ", (celsius * 1.8) + 32)
else:
    print("Numero incorrecto")