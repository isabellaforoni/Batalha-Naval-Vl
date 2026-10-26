def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    for i in range(tamanho):
        if orientacao=="vertical":
            lista.append([linha+i,coluna])
        else:
            lista.append([linha,coluna+i])
    return lista

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    lista= define_posicoes(linha,coluna,orientacao,tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(lista)
    else:
        frota[nome_navio]= [lista]
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

def posiciona_frota(frota):
    grid=[
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for navios in frota.values():
        for posicao in navios:
            for linha,coluna in posicao:
                grid[linha][coluna]=1
    return grid
            
def afundados(frota,tabuleiro):
    soma=0
    for embarcacoes in frota.values():
        for embarcacao in embarcacoes:
            acertos=0
            for linha,coluna in embarcacao:
                if tabuleiro[linha][coluna]=='X':
                    acertos+=1
            if acertos ==len(embarcacao):
                soma+=1
    return soma
                
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes_novas= define_posicoes(linha,coluna,orientacao,tamanho)
    for linha_nova,coluna_nova in posicoes_novas:
        if linha_nova>=10 or linha_nova<0:
            return False
        if coluna_nova>=10 or coluna_nova<0:
            return False

        for navios in frota.values():
            for navio in navios:
                if [linha_nova,coluna_nova] in navio:
                    return False
    return True
    
    



    

    

        


    


    

        


    

