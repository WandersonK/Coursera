n = int(input("Informe n: "))
k = int(input("Informe k: "))

def fatorial(num_fatorial):
    i = 1
    while num_fatorial > 0:
        i *= num_fatorial
        num_fatorial -= 1
    return i

print(fatorial(n) / (fatorial(k)*(fatorial(n - k))))
