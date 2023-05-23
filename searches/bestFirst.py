import models.grafo
from models.grafo import Grafo
from models.vertice import Vertice
from random import randrange, uniform
from math import sqrt



# Definir função heurística para o Best-First
def heuristica(vertice_atual, vertice_destino):
    x_atual, y_atual = vertice_atual.x, vertice_atual.y
    x_destino, y_destino = vertice_destino.x, vertice_destino.y

    distancia = sqrt((x_atual - x_destino) ** 2 + (y_atual - y_destino) ** 2)

    return distancia

def busca_best_first(grafo: Grafo, start_node: int, goal_node: int, arestas=[], plot=False):
    arestas.clear()
    arestas.append((start_node, start_node))
    visited = []
    stack = [(heuristica(grafo.vertice_indice(start_node), grafo.vertice_indice(goal_node)), start_node)]
    aux = []

    while stack:
        stack.sort(reverse=True)
        current_priority, current_node = stack.pop()

        if plot:
            for (prev, prox) in aux:
                if prox == current_node:
                    arestas.append((prev, prox))

        if current_node == goal_node:
            print("Caminho encontrado!")
            return True

        visited.append(current_node)

        for neighbor, _ in grafo.vertice_indice(current_node).vizinhos:
            if neighbor not in visited:
                if plot:
                    aux.append((current_node, neighbor))
                priority = heuristica(grafo.vertice_indice(neighbor), grafo.vertice_indice(goal_node))
                stack.append((priority, neighbor))

    print("Caminho não encontrado.")



if __name__ == '__main__':

    #grafo = models.grafo.Grafo(n_range = 10,)
    # Criar um grafo
    n_range = 10  # Número de vértices no grafo
    prob = 0.5  # Probabilidade de geração de aresta entre dois vértices
    grafo = Grafo(n_range, prob)

    start_node = 0
    goal_node = 5

    found = busca_best_first(grafo,start_node,goal_node,visitados=[])
    if found:
        print("Caminho encontrado!")
    else:
        print("Caminho não encontrado.")
