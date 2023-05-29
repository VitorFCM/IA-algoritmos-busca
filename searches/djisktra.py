from models.grafo import Grafo
from auxiliar.tempo import mede_tempo
from random import randrange


def recursive_djisktra(grafo: Grafo, atual: int, dest: int, func_heuristica, visitados: list[int], custos: list[int],
        caminhos: list[list[int]], arestas=[], plot=False):
    while True:
        visitados.append(atual)
        
        vertice_atual = grafo.vertice_indice(atual)
        if vertice_atual.vizinhos:
            # print(f'caminhos de {atual}: {grafo.vertice_indice(atual).vizinhos}')
            for a in vertice_atual.vizinhos:
                viz = a[0]
                peso = a[1]

                if (custos[viz] == -1) or (custos[viz] > (custos[atual] + peso)):
                    custos[viz] = custos[atual] + peso
                    caminhos[viz] = caminhos[atual].copy()
                    caminhos[viz].append(atual)

        next = -1
        next_peso = 999999999999
        for i in range(grafo.range):
            if i not in visitados:
                if (custos[i] != -1) and (custos[i] + func_heuristica(grafo.vertice_indice(i), grafo.vertice_indice(dest))< next_peso):
                    next_peso = custos[i]
                    next = i

        if plot and next != -1:
            if len(caminhos[next]) > 0:
                anterior = caminhos[next][len(caminhos[next]) - 1]
                arestas.append((anterior, next))

        if next == -1 or next == dest:
            if len(caminhos[dest]) > 0:
                caminhos[dest].append(dest)
            return custos[dest], caminhos[dest]

        atual = next


def busca_djisktra(grafo: Grafo, origem: int, dest: int, func_heuristica=lambda v1, v2: 0, arestas=[], plot=False):
    arestas.clear()
    arestas.append((origem, origem))
    visitados = []
    custos = [-1] * (grafo.range)  # -1 sendo considerado distância infinita
    caminhos = [[]] * (grafo.range)

    custos[origem] = 0

    # print(f'custos:{custos}')
    # print(f'caminhos:{caminhos}')

    custos, caminhos = recursive_djisktra(grafo, origem, dest, func_heuristica, visitados, custos, caminhos, arestas, plot)

    #print(f'arestas: {arestas}')
    #print(f'custos:{custos}')
    #print(f'caminhos:{caminhos}')

    return custos
