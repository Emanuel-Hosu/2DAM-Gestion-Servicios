#Crea un diccionario donde las claves sean nombres de estudiantes y los valores sean listas de 
#asistencia (donde 'P' es presente y 'A' es ausente). Luego, pide al usuario que ingrese el 
#nombre de un estudiante y devuelve su lista de asistencia.

alumnos = {
    "Emi": "p",
    "Alvaro": "a",
    "Pache": "a",
    "Arturito": "p"
}

user = input(f"Introduce un nombre {alumnos.keys()}")

print(alumnos.get(user, "El usuario no esta en la lista"))