numero_verificar = int(input("Entre com o número: "))

if numero_verificar % 3 == 0 and numero_verificar % 5 == 0:
    print("FizzBuzz")
else:
    print(numero_verificar)