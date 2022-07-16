valor = int(input("Digite um número inteiro: "))
restosoma = 0

while valor != 0:
    restosoma += (valor % 10)
    valor = valor // 10

print(restosoma)
