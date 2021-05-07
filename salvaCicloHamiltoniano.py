def salvaCiclo(grafo, rota, nomeArq):
    '''
    Salva o Ciclo Hamiltoniano (rota)
    no formato utilizado pela biblioteca
    :param grafo: 
    :param rota: 
    :return: 
    '''
    with open("Resultados/"+nomeArq, 'w') as arq:
        arq.write(f'{len(rota)}\n')
        for i in range(len(rota) - 1):
            v1 = rota[i]
            v2 = rota[i+1]
            custo = grafo.getPesoAresta(rota[i], rota[i + 1])
            arq.write(f'{v1} {v2} {custo}\n')
        print(f'\nCiclo salvo em /Resultados/{nomeArq}\n')
