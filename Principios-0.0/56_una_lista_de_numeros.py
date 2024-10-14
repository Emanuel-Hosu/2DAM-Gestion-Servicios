lista = [3, 5, 2, 1, 56, 2]

tamanio = len(lista)
match tamanio:
    case 0:
        print("La lista esta vacia")
    case 1:
        print("La lista tiene un elemento")
    case tamanio if tamanio > 1:
        print("La lista tiene varios elementos, la lista tiene ", tamanio, "elementos")
    
        