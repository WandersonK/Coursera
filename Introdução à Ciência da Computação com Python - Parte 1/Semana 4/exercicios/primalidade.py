n = int(input("Digite um número inteiro: "))

i = 1
primo = 0

while n >= i:
    if n % i == 0:
        primo += 1
        
    i += 1
    
if primo == 2:
    print("primo")
else:
    print("não primo")
