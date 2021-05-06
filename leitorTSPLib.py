# Abre Arquivo
import math

def abreTSP(nomeArq):
    with open(nomeArq, 'r') as arqTSPLib:
        # Le o cabeçalho
        name = arqTSPLib.readline().strip().split(':')[1].split()[0] # NAME
        fileType = arqTSPLib.readline().strip().split()[1] # TYPE
        comment = arqTSPLib.readline().strip().split()[1:] # COMMENT
        dimension = arqTSPLib.readline().strip().split()[-1]# DIMENSION
        edgeWeightType = arqTSPLib.readline().strip().split()[1] # EDGE_WEIGHT_TYPE
        arqTSPLib.readline()

        # Lê a lista de vértices
        vertices = []
        n = int(dimension)
        for i in range(n):
            v,x,y = arqTSPLib.readline().strip().split()
            vertices.append([int(v), float(x), float(y)])
        # Fecha o arquivo
        arqTSPLib.close()

    with open(name+'.txt', 'w') as arq:
        arq.write(dimension+'\n')
        #calcula o peso e escreve no arquivo
        arestaEPeso = []
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                v1 = vertices[i]
                v2 = vertices[j]
                if (i != j):
                    xd = v2[1] - v1[1]
                    yd = v2[2] - v1[2]
                    dij = int(round(math.sqrt(xd * xd + yd * yd)))
                    #evita repetição das arestas
                    if not [v2[0], v1[0], dij] in arestaEPeso:
                        arestaEPeso.append([v1[0], v2[0], dij])
                        arq.write(f'{v1[0]} {v2[0]} {dij}\n')
                        print(f'{v1[0]} {v2[0]} {dij}')




