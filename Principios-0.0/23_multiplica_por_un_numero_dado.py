list1 = [1, 2]
user = int(input("Intrduce el numero por el que deseas multiplicar"))
result = 0
list2 = []

for i in list1:
    list2.append(i * user)
    
print("El resultado final es: ", list2)