palabra = "Truco Rumano"
palabra_splitted = palabra.split('');
count = 0

for i in range(len(palabra_splitted)):
    count += 1

print("La palabra ", palabra, " tiene ", count, " palabras")