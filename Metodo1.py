import numpy

import numpy as np

def nearestNeighbor(grafo):
    length = grafo.ordemGrafo()
    visitados = []
    cicloHamiltoniano = []
    vInicial = np.random.randint(1,length)
    v = vInicial
    while v not in visitados:
        #inicializando valores
        custo = 100000
        index = -1
        vizinhosV = grafo.listaAdj[v]
        for i in vizinhosV:
            #i é uma aresta de V, i[0] é o vértice vizinho e i[1] o custo da aresta
            if i[0] not in visitados and i[0] != v and i[1] < custo:
                custo = i[1]
                index = i[0]
        if custo == 100000 or index == -1:
            #se entrar nesse if significa que todos os vertices ja foram visitados
            break
        cicloHamiltoniano.append([v, index, int(i[1])])
        visitados.append(v)
        v = index
    return cicloHamiltoniano
    #cicloHamiltoniano/ rota devera ser escrita em arquivo
