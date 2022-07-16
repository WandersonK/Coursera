numero = input("Informe um número para conferir: ")

i = len(numero)

while i > 1:
    divisaointeira = int(numero) % 100
    # print("Div Int", divisaointeira)
    
    numero = int(numero) // 10
    # print("numero", numero)
    
    if divisaointeira // 10 == divisaointeira % 10:
        print(divisaointeira)
    i -= 1