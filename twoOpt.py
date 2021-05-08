from time import perf_counter


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
    #pega o que está antes de i+1
    novaRota = rota[:i + 1]
    #inverte a ordem do que esta entre i+1 e j+1
    novaRota.extend(reversed(rota[i + 1:j + 1]))
    #coloca o que esta depois de j+1
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
        for i in range(n):
            for j in range(i + 2, n - 1):
                #pega os pesos das arestas para ver
                #se é possivel fazer a troca
                a = grafo.getPesoAresta(rota[i], rota[i + 1])
                b = grafo.getPesoAresta(rota[j], rota[j + 1])
                c = grafo.getPesoAresta(rota[i], rota[j])
                d = grafo.getPesoAresta(rota[i + 1], rota[j + 1])
                #se negativo, a+b tem um custo maior
                #que c+d, logo deve trocar as arestas
                #i,i+i e j,j+i com i,j e i+1,j+i
                delta = - a - b + c + d
                if delta < 0:
                    rota = trocaArestasTwoOPT(rota.copy(), i, j)
                    custo += delta
                    iteracao = 0

                tempo = (perf_counter() - tempoInicial)
        iteracao += 1

    return rota, custo
