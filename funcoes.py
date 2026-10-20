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

    

        


    

