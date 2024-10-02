user = input('Introduce numeros hasta que escibas "fin" para terminar: ')
count = 0
new_list = []

while user != 'fin':
    new_list.append(int(user))
    user = input('Introduce numeros hasta que escibas "fin" para terminar: ')

for i in new_list:
    if i % 2 == 0:
        count += 1

print('Hay un total de ', count, ' pares en la lista')