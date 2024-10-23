lista = ["emi", "arturo", "alvaro", "juan"]

for i in lista:
    dic = {list(lista).index(i) : i}
    print(dic)