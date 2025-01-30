estudiantes_calificaciones = {
    "Juan": [85, 90, 78],
    "María": [92, 88, 95],
    "Pedro": [75, 80, 72],
    "Ana": [88, 84, 91]
}

promedios = {estudiante: sum(calificaciones) / len(calificaciones) for estudiante, calificaciones in estudiantes_calificaciones.items()}

for estudiante, promedio in promedios.items():
    print(f"{estudiante}: {promedio:.2f}")