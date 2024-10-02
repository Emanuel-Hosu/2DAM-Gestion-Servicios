usuario = int(input("Que nr de fibonacci quieres saber "))

a, b = 0, 1;
for i in range(usuario):
    print(a, end=" ")
    a, b = b, a + b
    
