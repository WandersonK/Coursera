import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = (b) ** 2 - 4 * (a) * (c)

def raiz1():
    return (-(b) + math.sqrt(delta)) / (2 * (a))

def raiz2():
    return (-(b) - math.sqrt(delta)) / (2 * (a))

if delta > 0:
    if raiz1() > raiz2():
        maiorx = raiz1()
        menorx = raiz2()
    else:
        maiorx = raiz2()
        menorx = raiz1()
    
    print(f"as raízes da equação são {menorx} e {maiorx}")
    
elif delta == 0:
    print("a raiz desta equação é", raiz1())

else:
    print("esta equação não possui raízes reais")
