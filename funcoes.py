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
            

    

        


    


    

        


    

