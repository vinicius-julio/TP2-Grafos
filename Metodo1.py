from time import perf_counter
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
    return H, custo


def custoRota(grafo, rota):
    """
    Função que retorna o custo da rota
    informada
    """
    custo = 0
    for i in range(len(rota)-1):
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
    tempoInicial = perf_counter()
    tempo = 0
    n = len(rota)
    #custo da rota
    custo = custoRota(grafo, rota)

    iteracao = 0

    while tempo <= 180 and iteracao <= 10:
        melhoria = False

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
                #se negativo, a+b tem um custo maior
                #que c+d, logo deve trocar as arestas
                delta = - a - b + c + d
                if delta < 0:
                    #print(delta, i, j)
                    rota = trocaArestasTwoOPT(rota.copy(), i, j)
                    custo += delta
                    iteracao = 0

                tempo = (perf_counter() - tempoInicial)
        iteracao += 1

    return rota, custo, tempo, iteracao
