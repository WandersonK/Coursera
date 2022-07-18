def maior_elemento(lista):
    
    lista.sort()
    # print(lista[-1])
    return lista[-1]
    

lista = [1, 5, 9, 80, 6, 100, -1, 33, 9, 85, 85]
maior_elemento(lista)