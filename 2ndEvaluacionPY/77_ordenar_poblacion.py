paises_poblacion = {
    "China": 1444216107,
    "India": 1393409038,
    "Estados Unidos": 331893745,
    "Indonesia": 276361783,
    "Pakistán": 225199937,
    "Brasil": 213993437,
    "Nigeria": 211400708,
    "Bangladesh": 166303498,
    "Rusia": 145912025,
    "México": 130262216
}

paises_ordenados = dict(sorted(paises_poblacion.items(), key=lambda item: item[1], reverse=True))

for pais, poblacion in paises_ordenados.items():
    print(f"{pais}: {poblacion}")