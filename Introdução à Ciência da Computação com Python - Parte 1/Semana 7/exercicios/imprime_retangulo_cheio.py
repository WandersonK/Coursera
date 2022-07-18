largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while altura > 0:
    i = 0
    while largura > i:
        print("#", end="")
        i += 1
    
    print()
    altura -= 1
    