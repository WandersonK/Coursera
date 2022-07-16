qtd = int(input("Informe quantos números a calcular: "))
produto = 1

while qtd > 0:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    qtd -= 1

print("A multiplicação dos valores digitados é:", produto)
