valor = int(input("Informe um número: "))
restosoma = 0

while valor != 0:
    restosoma += (valor % 10)
    valor = valor // 10

print("A soma dos números é:", restosoma)
