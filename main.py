from Metodo1 import nearestNeighbor, twoOPT
from TP1.Grafo import Grafo
from leitorTSPLib import abreTSP

#nomeArq = input("Digite o nome do arquivo .tsp\n")
#nomeArq = "berlin52.tsp"
#Abre o arquivo.tsp e converte para o formato do tp1
#abreTSP(nomeArq)
#automaticamente abre o novo formato e cria o grafo
#g = Grafo.leArquivo(nomeArq.strip('.tsp')+".txt")
g = Grafo.leArquivo("d198.txt")


#print(g.imprimeGrafo())

nn = nearestNeighbor(g)
print("\nRota Nearest Neighbor:\n", nn[0],"\nCusto: ", nn[1])
rota2 = twoOPT(g, nn[0])
print("\nRota Otimizada 2-opt:\n",rota2[0], "\nCusto: ", rota2[1], "tempo(s)", rota2[2], "count sem melhoria", rota2[3])

