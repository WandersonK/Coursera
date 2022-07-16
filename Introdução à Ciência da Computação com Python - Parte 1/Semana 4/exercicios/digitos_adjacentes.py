numero = input("Digite um número inteiro: ")

i = len(numero)
verificar = 'não'

while i > 1:
    divisaointeira = int(numero) % 100
    # print("Div Int", divisaointeira)
    
    numero = int(numero) // 10
    # print("numero", numero)
    
    if divisaointeira // 10 == divisaointeira % 10:
        verificar = 'sim'
    i -= 1
    
print(verificar)