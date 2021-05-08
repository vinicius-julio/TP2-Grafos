from numpy import mean, std
from Metodo1 import nearestNeighbor
from TP1.Grafo import Grafo
from leitorTSPLib import abreTSP
from salvaCicloHamiltoniano import salvaCiclo
from twoOpt import twoOPT



#menu

opcao = 1
while (opcao!=0):
    nomeArq = input("Digite o nome do arquivo .tsp: ")
    abreTSP(nomeArq)
    g = Grafo.leArquivo(nomeArq.strip("tsp")+"txt")
    opMetodo = 1
    while(opMetodo!=0):
        print("Escolha o Método:")
        print("1 - Nearest Neighbor + 2-opt")
        print("2 - Vertice Mais Distante + 2-opt")
        print("0 - Voltar")
        opMetodo = int(input())
        if(opMetodo==1):
            print("-----------------------------------")
            print("Método 1: Nearest Neighbor + 2-Opt")
            print("-----------------------------------")
            print("Escolha o tipo de teste:")
            print("1 - Testar uma vez")
            print("2 - Testar 30x e exibir estatísticas")
            print("0 - Voltar")
            opTeste = int(input())
            if (opTeste == 1):
                m = nearestNeighbor(g)
                twoOpt = twoOPT(g, m[0])
                print("Custo: ", twoOpt[1])
                salvaCiclo(g, twoOpt[0], nomeArq.strip(".tsp")+'/CicloMetodo1.txt')

            if (opTeste == 2):
                listaCustos = []
                listaCiclos = []
                for i in range(30):
                    m = nearestNeighbor(g)
                    twoOpt = twoOPT(g, m[0])
                    custo = twoOpt[1]
                    ciclo = twoOpt[0]

                    listaCustos.append(custo)
                    listaCiclos.append(ciclo)

                melhorCusto = min(listaCustos)
                iMelhorCusto = listaCustos.index(melhorCusto)
                cicloMelhorCusto = listaCiclos[iMelhorCusto]

                piorCusto = max(listaCustos)
                mediaCusto = round(mean(listaCustos), 6)
                dpCusto = round(std(listaCustos), 6)
                print("Melhor Custo:", melhorCusto)
                print("Pior Custo:", piorCusto)
                print("Média do Custo:", mediaCusto)
                print("Desvio Padrão do Custo:", dpCusto)
                salvaCiclo(g, cicloMelhorCusto, nomeArq.strip(".tsp")+'/CicloMetodo1.txt')
                print("----------------------------------------------------")

        elif (opMetodo == 2):
            print("-----------------------------------")
            print("Método 1: Vértice mais distante + 2-Opt")
            print("-----------------------------------")
            print("Escolha o tipo de teste:")
            print("1 - Testar uma vez")
            print("2 - Testar 30x e exibir estatísticas")
            print("0 - Voltar")
            opTeste = input()
            if (opTeste == 1):
                m = nearestNeighbor(g)
                twoOpt = twoOPT(g, m[0])
                print("Custo: ", twoOpt[1])
                salvaCiclo(g, twoOpt[0], nomeArq.strip(".tsp")+'/CicloMetodo2.txt')

            if (opTeste == 2):
                listaCustos = []
                listaCiclos = []
                for i in range(30):
                    m = nearestNeighbor(g)
                    twoOpt = twoOPT(g, m[0])
                    custo = twoOpt[1]
                    ciclo = twoOpt[0]

                    listaCustos.append(custo)
                    listaCiclos.append(ciclo)

                melhorCusto = min(listaCustos)
                iMelhorCusto = listaCustos.index(melhorCusto)
                cicloMelhorCusto = listaCiclos[iMelhorCusto]

                piorCusto = max(listaCustos)
                mediaCusto = round(mean(listaCustos), 6)
                dpCusto = round(std(listaCustos), 6)
                print("Melhor Custo:", melhorCusto)
                print("Pior Custo:", piorCusto)
                print("Média do Custo:", mediaCusto)
                print("Desvio Padrão do Custo:", dpCusto)
                salvaCiclo(g, cicloMelhorCusto, nomeArq.strip(".tsp")+'/CicloMetodo2.txt')
                print("----------------------------------------------------")
