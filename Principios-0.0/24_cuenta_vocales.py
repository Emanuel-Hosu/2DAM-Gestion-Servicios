cadena = "Emanuel"
vocales = ['A', 'E', "I", "O", "U"]
count = 0

for i in cadena.upper():
    if i in vocales:
        count += 1
        
print("La palabra tiene ", count)