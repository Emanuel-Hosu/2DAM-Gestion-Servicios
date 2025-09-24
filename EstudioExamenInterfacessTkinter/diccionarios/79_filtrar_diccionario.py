empleados = {
    "Casi": 61,
    "Emi": 20,
    "Alejandro": 31,
    "Paco": 18
}

mayoresATreinta = {}

for key, value in empleados.items():
    if (value > 30):
        mayoresATreinta[key] = value

print(mayoresATreinta)