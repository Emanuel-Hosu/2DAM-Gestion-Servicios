listaClase = {
    "Emi": [7, 5, 7, 10],
    "Arturo": [5, 6, 8, 8],
    "Enma": [8, 5, 6, 5]
}

promedio = {}

for key, value in listaClase.items():
    resultado = 0
    for i in range(0, len(value)):
        resultado += value[i]
    promedio[key] = resultado / len(value)

print(promedio)