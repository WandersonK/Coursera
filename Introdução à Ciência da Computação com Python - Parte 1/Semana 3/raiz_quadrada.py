import math

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

delta = (b) ** 2 - 4 * (a) * (c)

if delta > 0:
    bhaskara_x1 = (-(b) + math.sqrt(delta)) / (2 * (a))
    bhaskara_x2 = (-(b) - math.sqrt(delta)) / (2 * (a))
    
    print(f"Delta ({delta}) maior que zero.")
    print("X1 =", bhaskara_x1)
    print("X2 =", bhaskara_x2)
    
elif delta == 0:
    bhaskara_x = (-(b) + math.sqrt(delta)) / (2 * (a))
    
    print("Delta igual a zero.")
    print("X =", bhaskara_x)

else:
    print(f"Delta ({delta}) negativo.")