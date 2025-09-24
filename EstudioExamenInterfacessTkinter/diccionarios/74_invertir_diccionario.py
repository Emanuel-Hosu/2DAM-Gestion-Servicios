ciudades = {
    "Aranjuez": 28300,
    "La Montaña": 28301,
    "Pinto": 28400
}

ciudades_invertidas = {}

for clave, valor in ciudades.items(): 
    ciudades_invertidas[valor] = clave 

print(ciudades_invertidas)