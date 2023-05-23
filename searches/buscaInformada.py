def busca_informada(grafo, start_node, goal_node, func_heuristica, func_info_rede):
    visited = []

    #Ao inves de uma tupla, virou uma lista de 3 elementos, o ultimo eh o custo para chegar naquele vertice.
    # stack = [[valor_heuristica, index_vertice, custo_vertice]]
    stack = [[func_heuristica(grafo.vertice_indice(start_node), grafo.vertice_indice(goal_node)), start_node, 0]]
    custo = 0

    while stack:
        stack.sort(reverse=True)

        current_priority, current_node, current_cost = stack.pop()

        custo += current_cost
        if current_node == goal_node:
            print("Caminho encontrado!")
            return custo

        visited.append(current_node)

        for neighbor in grafo.vertice_indice(current_node).vizinhos:
            if neighbor[0] not in visited:
                priority = func_heuristica(grafo.vertice_indice(neighbor[0]), grafo.vertice_indice(goal_node)) + func_info_rede(neighbor)
                stack.append([priority, neighbor[0], neighbor[1]])

    print("Caminho não encontrado.")
    return -1

