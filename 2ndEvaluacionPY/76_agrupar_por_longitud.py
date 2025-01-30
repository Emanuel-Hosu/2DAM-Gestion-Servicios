diccionario = {}
for palabra in lista:
    longitud = len(palabra)
    if longitud in diccionario:
        diccionario[longitud].append(palabra)
    else:
        diccionario[longitud] = [palabra]

