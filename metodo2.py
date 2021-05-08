from time import perf_counter
import numpy as np
def pega_pares(lista):
    pares = []
    for i in range(len(lista)-1):
        pares.append([lista[i], lista[i+1]])
    pares.append([lista[-1], lista[0]])
    
    return pares
def custo_total(matriz, lista):
    custo = 0
    
    pares = pega_pares(lista)
    for n in pares:
        a = n[0] - 1
        b = n[1] - 1
        custo = matriz[a][b] + custo

    return custo
def mais_distante(matriz):
    ciclo_inicial=[]
    length = matriz.ordemGrafo()
    for i in range(3):
        ciclo_inicial.append(np.random.randint(1, length))

    # Transformando para o equivalente (ie. Vetor iniciando em 0)
    ciclo_inicial = [x - 1 for x in ciclo_inicial]
    
    while len(ciclo_inicial) < length:
        distancia_vertice = -1
        custo = 1000000
        vertice = -1

        for linha in range(0, length):
            if not linha in ciclo_inicial:
                for coluna in range(0, length):
                    if coluna in ciclo_inicial:
                        if matriz[linha][coluna] > distancia_vertice:
                            distancia_vertice = matriz[linha][coluna]
                            vertice = linha

        

        pares = pega_pares(ciclo_inicial)
        for aresta in pares:
            calculo_custo = (matriz[vertice][aresta[0]] + matriz[vertice][aresta[1]] - matriz[aresta[0]][aresta[1]])
            if  calculo_custo < custo:
                novo_ciclo = list(ciclo_inicial)
                custo = calculo_custo
                novo_ciclo.insert((ciclo_inicial.index(aresta[0]) + 1), vertice)

        passos = list(novo_ciclo)
        passos = [x + 1 for x in passos]
        ciclo_inicial = list(novo_ciclo)

    ciclo_inicial = [x + 1 for x in ciclo_inicial]

   
    ciclo_final = list(ciclo_inicial)
    ciclo_final.append(ciclo_final[0])
    custo = custo_total(matriz, ciclo_inicial)
    

    return (ciclo_final, custo)


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
