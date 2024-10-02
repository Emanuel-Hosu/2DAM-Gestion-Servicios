lista = []  # Lista vacía para almacenar los datos
h = 0;
while True:
    entrada = input("Introduce un número o palabra (escribe 'fin' para terminar): ")
   
    if entrada.lower() == "fin":  # Si el usuario escribe 'fin', se termina el bucle
        break
   
    lista.append(entrada)  # Agrega la entrada a la lista

print("El primer elemento es: ", lista[0], "|| Y el último elemento es ", lista[-1])