user = int(input('Introduce numeros hasta que escibas "fin" para terminar: '))
list1 = []
new_list = []

while user != 'fin':
    list1.append(int(user))
    user = input('Introduce numeros hasta que escibas "fin" para terminar: ')

for i in list1:
    if i > 0:
        new_list.append(i)
        

print('list1a final sin numeros negativos: ', new_list)