import numpy as np
from math import inf

N = 10


def velocidade():
    pesos = prim()

    vel_med = (sum(pesos) // len(pesos))+1

    return vel_med


def prim():
    # Gera um grafo de matriz de adjacência
    G = np.random.randint(3, 10, (N, N))

    lista_de_nos = []

    for i in range(N):
        lista_de_nos.append(0)

    num_arestas = 0

    # escolhe o primeiro nó da lista como o inicial
    lista_de_nos[0] = True

    pesos_arestas = []

    while num_arestas < N - 1:

        minimo = inf
        a = 0
        b = 0
        for m in range(N):
            if lista_de_nos[m]:
                for n in range(N):
                    if (not lista_de_nos[n]) and G[m][n]:
                        # not in selected and there is an edge
                        if minimo > G[m][n]:
                            minimo = G[m][n]
                            a = m
                            b = n

        lista_de_nos[b] = True
        num_arestas += 1
        pesos_arestas.append(G[a][b])

    return pesos_arestas
