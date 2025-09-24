exam1 = {
    "Emi": 3,
    "Arturo": 4,
    "Enma": 5
}

exam2 = {
    "Emi": 5,
    "Arturo": 5,
    "Enma": 2
}

bests = {}

for key, value in exam1.items():
    if (value > exam2.get(key)):
        bests[key] = value
    else:
        bests[key] = exam2.get(key)

print(bests)