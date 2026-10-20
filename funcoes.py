def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    for i in range(tamanho):
        if orientacao=="vertical":
            lista.append([linha+i,coluna])
        else:
            lista.append([linha,coluna+i])
    return lista



        


    

