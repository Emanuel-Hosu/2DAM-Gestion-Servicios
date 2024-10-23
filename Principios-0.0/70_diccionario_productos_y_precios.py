productos = {
    "fairy": 13,
    "champu": 5,
    "cocacola": 1
}

user = input("Elige un producto ")

print(productos.get(user, "El producto no ha sido encontrado"), "€")