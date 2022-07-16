def vogal(testa_vogal):
    vogais = ['a', 'e', 'i', 'o', 'u']
    i = 0
    verif = False
    
    while i < len(vogais):
        if testa_vogal.lower() == vogais[i]:
            verif = True
        
        i+= 1

    return verif

vogal(input())