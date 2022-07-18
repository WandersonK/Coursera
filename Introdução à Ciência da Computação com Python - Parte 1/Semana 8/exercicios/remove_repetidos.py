def remove_repetidos(lista):
    lista_sem_repetidos = []
    
    for dado in lista:
        if dado not in lista_sem_repetidos:
            lista_sem_repetidos.append(dado)

    # print(sorted(lista_sem_repetidos))
    return sorted(lista_sem_repetidos)

lista = [1, 1, 1, 1, 1, 1, 1]
remove_repetidos(lista)