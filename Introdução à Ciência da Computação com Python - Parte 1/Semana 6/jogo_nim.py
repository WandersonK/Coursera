def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input(">>> "))
    
    valida_escolha = True
    
    while valida_escolha:
        
        if escolha == 1:
            valida_escolha = False
            partida()
            
        elif escolha == 2:
            valida_escolha = False
            campeonato()
        else:
            print()
            print("Oops! opção inválida! Tente de novo.")
            print()
            print("1 - para jogar uma partida isolada")
            print("2 - para jogar um campeonato")

            escolha = int(input(">>> "))
        
def computador_escolhe_jogada(n, m):
    i = 0
    pecas = 0
    
    while i < m:
        if n % (m + 1) != 0:
            n -= 1
            pecas += 1
        else:
            i = m
            
        i += 1
        
    if n < 1:
        print()
        print(f"O computador tirou {'uma peça' if pecas == 1 else str(pecas) + ' peças'}.")
        print("Fim do jogo! O computador ganhou!")
        # return 'cp'
    
    else:
        print()
        print(f"O computador tirou {'uma peça' if pecas == 1 else str(pecas) + ' peças'}.")
        print(f"Agora {'resta apenas uma peça' if n == 1 else 'restam ' + str(n) + ' peças'} no tabuleiro.")
        resultado = usuario_escolhe_jogada(n, m)
    return pecas
    return resultado
    
def usuario_escolhe_jogada(n, m):
    valida_jogada = True
    
    print()
    valor = int(input("Quantas peças você vai tirar? "))
    
    while valida_jogada:
        if valor <= m and valor > 0 and valor <= n:
            n -= valor
            valida_jogada = False
        else:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            valor = int(input("Quantas peças você vai tirar? "))
            
    
    if n < 1:
        print()
        print(f"Você tirou {'uma peça' if valor == 1 else str(valor) + ' peças'}.")
        print("Fim do jogo! Você ganhou!")
        return 'vc'
        
    else:
        print()
        print(f"Você tirou {'uma peça' if valor == 1 else str(valor) + ' peças'}.")
        print(f"Agora {'resta apenas uma peça' if n == 1 else 'restam ' + str(n) + ' peças'} no tabuleiro.")
        resultado = computador_escolhe_jogada (n, m)
    return resultado
    
def partida():
    
    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) != 0:
        print()
        print("Computador começa!")
        resultado = computador_escolhe_jogada(n, m)
    else:
        print()
        print("Você começa!")
        resultado = usuario_escolhe_jogada(n, m)
        
    return resultado
        
def campeonato():
    
    i = 1
    cp = 0
    vc = 0
    print("Voce escolheu um campeonato!")
    # print("Modo campeonato em Desenvolvimento!")
    
    while i <= 3:
        print()
        print(f"**** Rodada {i} ****")
        
        # resultado = partida()
        
        if partida() == 'cp':
            cp += 1
        else:
            vc += 1
        
        i += 1
    
    print(f"Placar: Você {vc} X {cp} Computador")
    
main()