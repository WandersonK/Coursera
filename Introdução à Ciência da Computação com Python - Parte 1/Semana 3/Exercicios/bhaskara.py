import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = (b) ** 2 - 4 * (a) * (c)

if delta > 0:
    bhaskara_x1 = (-(b) + math.sqrt(delta)) / (2 * (a))
    bhaskara_x2 = (-(b) - math.sqrt(delta)) / (2 * (a))
    if bhaskara_x1 > bhaskara_x2:
        maiorx = bhaskara_x1
        menorx = bhaskara_x2
    else:
        maiorx = bhaskara_x2
        menorx = bhaskara_x1
    
    print(f"as raízes da equação são {menorx} e {maiorx}")
    
elif delta == 0:
    bhaskara_x = (-(b) + math.sqrt(delta)) / (2 * (a))
    
    print("a raiz desta equação é", bhaskara_x)

else:
    print("esta equação não possui raízes reais")