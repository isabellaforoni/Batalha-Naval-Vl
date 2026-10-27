from funcoes import define_posicoes, preenche_frota, posicao_valida
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     
navios = {
    "porta-aviões": [4, 1],
    "navio-tanque": [3, 2],
    "contratorpedeiro": [2, 3],
    "submarino": [1, 4],
}

for nome,infos in navios.items():
    tam=infos[0]
    qnt=infos[1]
    for i in range(qnt):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tam}")

    valida=0

    while valida==0:
        linha=int(input("Linha:"))
        coluna=int(input("Coluna:"))

        if nome=="submarino":
            orientacao='horizontal'
        else:
            escolha=int(input("[1] Vertical [2] Horizontal >"))
            if escolha==1:
                orientacao='vertical'
            else:
                orientacao='horizontal'
        if posicao_valida(frota,linha,coluna,orientacao,tam):
            posicoes=define_posicoes(linha,coluna,orientacao,tam)
            frota= preenche_frota(frota,nome,linha,coluna,orientacao,tam)
            valida=1
        else:
            print(f'Esta posição não está válida!')
print(frota)

