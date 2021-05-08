from time import perf_counter
import numpy as np
import random
def gera_ciclo(inicio, fim, tam):
    ciclo = random.sample(range(inicio, fim + 1), tam)
    return ciclo
def custoRota(grafo, rota):
    """
    Função que retorna o custo da rota
    informada
    """
    custo = 0
    for i in range(len(rota)-1):
        custo += grafo.getPesoAresta(rota[i], rota[i+1])
    return custo

def mais_distante(matriz,ciclo_inicial):
    length = matriz.ordemGrafo()

    visitados = []
    H = []
    vInicial = np.random.randint(1, length)
    v = vInicial
    # v = 1
    
    
    while v not in visitados:
        distancia_vertice = -1
        custo = 1000000
        vertice = -1
        index = -1

        for linha in range(1, length):
            if not linha in ciclo_inicial:
                for coluna in range(0, len(matriz.listaAdj[linha])):
                    if coluna in ciclo_inicial:
                        if matriz.listaAdj[linha][coluna][1] > distancia_vertice:
                            distancia_vertice = matriz.listaAdj[linha][coluna][1]
                            vertice = linha

        
        H.append(v)
        vizinhosV = matriz.listaAdj[vertice]
        for i in vizinhosV:
            #i é uma aresta de V, i[0] é o vértice vizinho e i[1] o custo da aresta
            if i[0] not in visitados and i[0] != v and i[1] < custo:
                custo = i[1]
                index = i[0]
        if custo == 100000 or index == -1:
            #se entrar nesse if significa que todos os vertices ja foram visitados
            break
        visitados.append(v)
        v = index
    custo = custoRota(matriz, H)
    return H, custo



