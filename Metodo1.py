import numpy

import numpy as np

def nearestNeighbor(grafo):
    length = grafo.ordemGrafo()
    visitados = []
    H = []
    H1 = []
    vInicial = np.random.randint(1,length)
    v = vInicial
    # v = 1
    while v not in visitados:
        H.append(v)
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
        H1.append([v, index, custo])
        visitados.append(v)
        v = index
    custo = custoRota(grafo, H)
    return H,custo
    #cicloHamiltoniano/ rota devera ser escrita em arquivo


def custoRota(grafo, rota):
    """
    Method to return length of a tour given
    all tour edges are part of graph
    args:
        tour: List of nodes of graph
    return:
        tourlen: int/float
            Length of tour. If any edges is
            missing, returns zero.
    """
    custo = 0
    for i in range(len(rota)-1):
        '''vizinhosI = grafo.listaAdj[rota[i]]
        for j in range(len(vizinhosI)):
            if (vizinhosI[j][0] == rota[i+1]):
                custo += vizinhosI[j][1]'''
        custo += grafo.getPesoAresta(rota[i], rota[i+1])
    return custo


def trocaArestasTwoOPT(rota, i, j):
    """
    Função para trocar duas arestas e trocar com
    a que cruza.
    """
    novaRota = rota[:i + 1]
    novaRota.extend(reversed(rota[i + 1:j + 1]))
    novaRota.extend(rota[j + 1:])

    return novaRota

def twoOPT(grafo, rota):
    """
    Funcao cria nova rota usando 2OPT
    args:
        rota: Lista dos vertices formando a
            rota nao otimizada
    return:
        rota: Lista dos vertices formando a
            rota 2-optima
        custo: int/float
            custo da 2-optima rota
    """
    n = len(rota)

    # length of provided tour
    custo = custoRota(grafo, rota)

    # tracking improvement in tour
    improved = True

    while improved:
        improved = False

        for i in range(n):
            for j in range(i + 2, n - 1):
                #pega os pesos das arestas para ver
                #se é possivel fazer a troca
                a = grafo.getPesoAresta(rota[i], rota[i + 1])
                b = grafo.getPesoAresta(rota[j], rota[j + 1])
                c = grafo.getPesoAresta(rota[i], rota[j])
                d = grafo.getPesoAresta(rota[i + 1], rota[j + 1])

                # benefit from swapping i,i+1 and j,j+1
                # with i,j and i+1,j+1
                delta = - a - b + c + d
                if delta < 0:
                    #print(delta, i, j)
                    rota = trocaArestasTwoOPT(rota.copy(), i, j)
                    custo += delta
                    improved = True

    return rota, custo
