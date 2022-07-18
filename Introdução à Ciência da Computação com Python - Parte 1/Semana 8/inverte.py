def imprime_reverso(lista):
    
    for valor in lista:
        print(valor)

list = []

digito = 1
while digito != 0:
    digito = int(input())
    
    if digito != 0:
        list.append(digito)


list.reverse()
imprime_reverso(list)
# print(list)
