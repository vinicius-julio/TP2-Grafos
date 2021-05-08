from numpy import mean, std

from Metodo1 import nearestNeighbor, twoOPT
from TP1.Grafo import Grafo
from leitorTSPLib import abreTSP
from salvaCicloHamiltoniano import salvaCiclo
from Metodo1 import nearestNeighbor, twoOPT
from metodo2 import mais_distante, gera_ciclo

#Abre o arquivo.tsp e converte para o formato do tp1

abreTSP("berlin52.tsp")
abreTSP("ch130.tsp")
abreTSP("d198.tsp")
g1 = Grafo.leArquivo("berlin52.txt")
g2 = Grafo.leArquivo("ch130.txt")
g3 = Grafo.leArquivo("d198.txt")
'''

print(''-----------------------------------
#Método 1: Nearest Neighbor + 2-Opt
-----------------------------------'')
print(
    "Instância: berlin52\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    nn = nearestNeighbor(g1)
    twoOpt = twoOPT(g1, nn[0])
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
salvaCiclo(g1, cicloMelhorCusto, 'berlin52/CicloMetodo1.txt')
print("----------------------------------------------------")

print(
    "Instância: ch130\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    nn = nearestNeighbor(g2)
    twoOpt = twoOPT(g2, nn[0])
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
salvaCiclo(g2, cicloMelhorCusto, 'ch130/CicloMetodo1.txt')
print("----------------------------------------------------")

print(
    "Instância: d198\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    nn = nearestNeighbor(g3)
    twoOpt = twoOPT(g3, nn[0])
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
salvaCiclo(g3, cicloMelhorCusto, 'd198/CicloMetodo1.txt')
print("----------------------------------------------------")

'''

print('''-----------------------------------
Método 2: Vertice mais distante + 2-Opt
-----------------------------------
''')
print(
    "Instância: berlin52\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    #seu codigo
    ciclo_inicial = gera_ciclo(1, g1.ordemGrafo(),3)
    nn = mais_distante(g1,ciclo_inicial)
    twoOpt = twoOPT(g1, nn[0])
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
salvaCiclo(g1, cicloMelhorCusto, 'berlin52/CicloMetodo2.txt')
print("----------------------------------------------------")

print(
    "Instância: ch130\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    #seu codigo
    ciclo_inicial = gera_ciclo(1, g2.ordemGrafo(),3)
    nn = mais_distante(g2,ciclo_inicial)
    twoOpt = twoOPT(g2, nn[0])
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
salvaCiclo(g2, cicloMelhorCusto, 'ch130/CicloMetodo2.txt')
print("----------------------------------------------------")

print(
    "Instância: d198\n"
)
listaCustos = []
listaCiclos = []
for i in range(30):
    #seu codigo
    nn = mais_distante(g3,ciclo_inicial)
    twoOpt = twoOPT(g3, nn[0])
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
salvaCiclo(g3, cicloMelhorCusto, 'd198/CicloMetodo2.txt')
print("----------------------------------------------------")

