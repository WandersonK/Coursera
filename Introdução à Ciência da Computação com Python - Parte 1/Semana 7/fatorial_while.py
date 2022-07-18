def fatorial(num):
    i = 1
    while num >= 1:
        i *= num
        num -= 1
    return i

escolha = True
while escolha:
    num = int(input("Infome um nº para fatorial: "))
    print(fatorial(num))
    