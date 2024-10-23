alumno = {
    "nombre": "Emi",
    "edad": 20
}

#Segunda forma de crear un diccionario
alumno2 = ([
    ("nombre", "Emi"),
    ("edad", 20),
])

print(f"Mi array antes de modificar {alumno['nombre']}")

#alumno["nombre"] = "Alvaro"
#alumno["curso"] = "2 DAM"
#print(alumno)

#Para imprimir solo las key:
#for i in alumno:
#    print(i)

#Para imprimir solo los valores
#for i in alumno:
#    print(alumno[i])

#Si queremos imprimir key y valor
#for i,j in alumno.items():
#    print(i, j)

#Para eleminar el diccionario usamos clear()
#Ejemplo alumno.clear()

#get() nos permite conultar los vlaores de una key
#sintaxis get(<key>, ['default])
#print(alumno.get('aaaa', 'Llave no encontrada'))

#metodo keys() devuelve una lista con todas las llaves
#print(alumno.keys())

#metodo values() devuelve todos los valores del diccionario
#print(alumno.values())

#metodo pop() elimina el valor de la key pasada por parametro <- Este hay que repasarlo
#print(alumno.pop('nombre'))

#metodo para eliminar el primer key value del diccionario
#alumno.popitem()

#metodo update(<obk>) updatea todos los claves valores y añade las que no estan
alumno2 = {
    "nombre": "Alvaro",
    "edad": 33,
    "Curso": '2 de Infantil'
}

alumno.update(alumno2)

print(alumno)

