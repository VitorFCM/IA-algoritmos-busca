from funcoesAvaliacao import *

def busca_heuristica(grafo, start_node, goal_node, func_heuristica, func_info_rede):
    visited = []
    stack = [(func_heuristica(grafo.vertice_indice(start_node), grafo.vertice_indice(goal_node)), start_node)]

    while stack:
        stack.sort(reverse=True)
        current_priority, current_node = stack.pop()

        if current_node == goal_node:
            print("Caminho encontrado!")
            return True

        visited.append(current_node)

        for neighbor in grafo.vertice_indice(current_node).vizinhos:
            if neighbor not in visited:
                priority = func_heuristica(grafo.vertice_indice(neighbor[0]), grafo.vertice_indice(goal_node)) + func_info_rede(neighbor)
                stack.append((priority, neighbor[0]))

    print("Caminho não encontrado.")



if __name__ == '__main__':

    #grafo = models.grafo.Grafo(n_range = 10,)
    # Criar um grafo
    n_range = 10  # Número de vértices no grafo
    prob = 0.5  # Probabilidade de geração de aresta entre dois vértices
    grafo = Grafo(n_range, prob)

    start_node = 0
    goal_node = 5

    found = busca_heuristica(grafo, start_node, goal_node, heuristica_best_first, info_rede_best_first)
    if found:
        print("Caminho encontrado!")
    else:
        print("Caminho não encontrado.")
