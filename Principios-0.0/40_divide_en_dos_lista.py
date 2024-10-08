general_list = [32, 5, 2, 6, 51, 52, 6, 3, 1, 4, 6, 8, 24, 73, 88, 12, 44, 5,  3, 6 , 7, 2 , 777, 62, 66]
general_list.sort()
lower_list = []
higher_list = []

user = int(input("Introduce el numero donde quieras partir la lista"))

for i in general_list:
    if i < user:
        lower_list.append(i)
    else:
        higher_list.append(i)
        
print("Lista menor ", lower_list)
print("Lista menor ", higher_list)