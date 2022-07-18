def soma_elementos(lista):
    somatorio = 0
    
    for dado in lista:
        somatorio += dado
    
    # print(somatorio)
    return somatorio

lista = [20, 1, 1, 2, 1, 1, 10]
soma_elementos(lista)