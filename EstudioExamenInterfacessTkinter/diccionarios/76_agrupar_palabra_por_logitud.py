palabras = ["Paco", "Manzana", "Kirby", "Emi", "Juan", "Gengary"]


maxLen = len(palabras[0])
for palabra in palabras:
    if len(palabra) > maxLen:
        maxLen = len(palabra)

minLen = len(palabras[0])
for palabra in palabras:
    if len(palabra) < minLen:
        minLen = len(palabra)

diccionario = {}

for i in range(minLen, maxLen + 1):
    arrayPalabras = []
    for palabra in palabras:
        if len(palabra) == i:
            arrayPalabras.append(palabra)

    diccionario[i] = arrayPalabras

print(diccionario)