qtd = int(input("Informe quantos números a calcular: "))
soma = 0

while qtd > 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    qtd -= 1

print("A soma dos valores digitados é:", soma)
