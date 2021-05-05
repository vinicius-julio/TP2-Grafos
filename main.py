from TP1.Grafo import Grafo
from leitorTSPLib import abreTSP

nomeArq = input("Digite o nome do arquivo .tsp\n")

abreTSP(nomeArq)

g = Grafo.leArquivo(nomeArq.strip('.tsp')+".txt")
g.exibeInformacoes(1)
