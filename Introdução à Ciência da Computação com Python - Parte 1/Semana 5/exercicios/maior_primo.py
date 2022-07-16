def calcula_sequencia(num_verifica):
    verificado_por = 1
    resultPrimo = 0
    
    while verificado_por <= num_verifica:
        if num_verifica % verificado_por == 0:
            resultPrimo += 1
        verificado_por += 1
    
    return resultPrimo

def maior_primo(n):
    num_verifica = 1
    
    while num_verifica <= n:
        if calcula_sequencia(num_verifica) == 2:
            ePrimo = num_verifica
    
        num_verifica += 1
    
    return ePrimo

maior_primo(int(input()))