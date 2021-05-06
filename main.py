from Metodo1 import nearestNeighbor
from TP1.Grafo import Grafo
from leitorTSPLib import abreTSP

#nomeArq = input("Digite o nome do arquivo .tsp\n")

#abreTSP(nomeArq)

#g = Grafo.leArquivo(nomeArq.strip('.tsp')+".txt")
g = Grafo.leArquivo("berlin52.txt")

#print(g.imprimeGrafo())
print(nearestNeighbor(g))
