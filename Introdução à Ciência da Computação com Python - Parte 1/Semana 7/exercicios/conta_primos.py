def calcula_sequencia(num_verifica):
    verificado_por = 1
    resultPrimo = 0
    
    while verificado_por <= num_verifica:
        if num_verifica % verificado_por == 0:
            resultPrimo += 1
        verificado_por += 1
    
    return resultPrimo

def n_primos(n):
    num_verifica = 1
    qtd_primos = 0
    
    while num_verifica <= n:
        if calcula_sequencia(num_verifica) == 2:
            qtd_primos += 1
    
        num_verifica += 1
    # print(qtd_primos)
    return qtd_primos

n_primos (int(input()))