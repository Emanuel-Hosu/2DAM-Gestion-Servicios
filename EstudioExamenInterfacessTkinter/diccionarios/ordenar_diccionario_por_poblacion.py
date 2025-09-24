poblacion = {
    "China": 300000,
    "Vaticano": 230,
    "Rumania": 2000,
    "España": 33333,
    
}

poblaciones = []

poblacion_ordenada = {}

for key, value in poblacion.items():
    poblaciones.append([key, value])

poblaciones.sort()

for poblacion in poblaciones:
    poblacion_ordenada[poblacion[0]] = poblacion[1]

print(poblacion_ordenada)