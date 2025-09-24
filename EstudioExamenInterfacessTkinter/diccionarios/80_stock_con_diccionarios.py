inventroy = {
    "Kebabs": 20,
    "Cocacola": 25,
    "Patatas": 24 
}

while True:
    print("1. Ver inventario\n2. Añadir producto\n3. Quitar producto\n4. Update product")
    user = input()
    if (user == "1"):
        for key, value in inventroy.items():
            print("Nombre ", key, " - stock ", value)
    elif (user == "2"):
        key = ""
        value = -1
        print("Please insert name")
        key = input()
        print("Please insert stock")
        value = int(input())
        inventroy.setdefault(key, value)
        print("SUCCESFUL product added to stock")
    elif (user == "3"):
        key = ""
        print("Please insert the key you want to delete")
        key = input()
        inventroy.pop(key)
        print("Succesful product errased")
    elif (user == "4"):
        key = ""
        print("Please inseert the name you want to update")
        key = input()
        print(inventroy.get(key))
        stock = -1
        print("Please insert the new stock")
        stock = int(input())
        inventroy[key] = stock
        print("Stock updated")