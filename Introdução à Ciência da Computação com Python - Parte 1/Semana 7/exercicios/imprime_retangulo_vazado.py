largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

maior_altura = altura

while altura > 0:
    i = 0
    while largura > i:
        if altura == 1 or altura == maior_altura or i == 0 or i == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
        i += 1
    
    print()
    altura -= 1
    