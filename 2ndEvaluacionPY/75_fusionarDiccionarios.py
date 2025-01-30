calificaciones_matematicas = {
    'Juan': 85,
    'Ana': 92,
    'Luis': 78,
    'Marta': 89
}

calificaciones_ciencias = {
    'Juan': 90,
    'Ana': 88,
    'Luis': 84,
    'Marta': 91
}

calificaciones_combinadas = {}
for estudiante in calificaciones_matematicas:
    calificaciones_combinadas[estudiante] = {
        'Matemáticas': calificaciones_matematicas[estudiante],
        'Ciencias': calificaciones_ciencias[estudiante],

    }

print(calificaciones_combinadas)