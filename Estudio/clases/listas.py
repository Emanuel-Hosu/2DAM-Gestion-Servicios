mi_lista = [1, 2, 3]
#append agrega un elemento al array
mi_lista.append(3)
print("append(): ", mi_lista)
#remove elimina el elemento que indicas del array, con True equivale a 1 no va ademas de eliminar los valores repetidos
mi_lista.remove(True)
print("remove(): ", mi_lista)
#elimina y devuelve el ultimo elemento del array ademas de que si lo inidicas elimina ese
mi_lista.pop(0)
print("len() + pop(): ", len(mi_lista))
#Creo otro array para pruebas
mi_lista2 = [1, 2]
#extend agrega los elementos de otra lista al final
mi_lista2.extend(mi_lista)
print("extend(): ", mi_lista2)
#inser(indice, elemento) agrega el elemento en el índice indicado
mi_lista2.insert(1, "pepe")
mi_lista2.insert(2, "pepe")
print("insert(): ", mi_lista2)
#index(elem) devuelve el indice de la primera aparicion
print("index(): ", mi_lista2.index("pepe"))
#count() cuantas veces aparece
print("count(): ", mi_lista2.count("pepe"))
#sort() Tienen que ser del mismo tipo, sino da error. De menor a mayor
print("sort(): ", mi_lista.sort())
#reverse() Tienen que ser del mismo tipo, sino da error. De mayor a menor
#print("reverse(): ", mi_lista2.sort(reverse=True))

#clear(mi_lista) elimina todos los elementos de la lista
print("clear(): ", mi_lista.clear())
#copy() crea una copia del array
mi_lista3 = mi_lista2.copy()
print("copy(): ", mi_lista3)
#sublistas pregunta de examen
new_list = ["Hola mundo", 3, 4, "pepe"]
new_list[2:4] = ["hola", "pepa"]
print("sublistas(): ", new_list)
#operadores suma todos los operadores de una lista
operator_list1 = [1, 1, 1, 1]
operator_list2 = [1, 9, 3]
print("operadores: < ", operator_list1 < operator_list2)
print("operadores: != ", operator_list1 != operator_list2)
print("operadores: * ", operator_list1 * 3)
#iterar listas
iter_list=[5, 9, 10]
print("enumerate example 1: ")
for index, i in enumerate(iter_list):
    print(index, i)

print("enumerate example 2: ")
for index, i in enumerate('Hola Mundo'):
    print(index, i)
    
print("zip example 1: ")
zip_list1 = [1, 4, 2]
zip_list2 = ["Rock", "Emi", "Juan", "Paco"]
for l1, l2 in zip(zip_list1, zip_list2):
    print(l1, l2)
    
#Ejemplos
print("Examples")
exemple_list = [10, "Python", False, [4, 5, 6]]
print(exemple_list[0] + 5)
print(exemple_list[1].upper())
print(exemple_list[2] or True)
if "Python" in exemple_list:
    print("La palabra 'Puthon' esta en la lista")
exemple_list[3][0] = 100
print(exemple_list)
