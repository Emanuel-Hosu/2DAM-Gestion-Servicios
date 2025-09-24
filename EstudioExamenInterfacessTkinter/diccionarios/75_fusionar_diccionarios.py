mates = {
    "Emi": 4,
    "Arturo": 10,
    "Alvaro": 7
}

ciencias = {
    "Emi": 9,
    "Arturo": 5,
    "Alvaro": 6
}

arrayAsignaturas = []

combinado = {}

for key, value in mates.items():
    arrayAsignaturas.append(["Mates: ", value])

index = 0
for key, value in ciencias.items():
    arrayAsignaturas[index] += ["Ciencias", value]
    index += 1

i = 0
for key, value in mates.items():
    combinado[key] = arrayAsignaturas[i]
    i += 1

print(combinado)