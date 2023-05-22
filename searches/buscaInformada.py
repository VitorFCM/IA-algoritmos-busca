def busca_informada(grafo, start_node, goal_node, func_heuristica, func_info_rede):
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
            if neighbor[0] not in visited:
                priority = func_heuristica(grafo.vertice_indice(neighbor[0]), grafo.vertice_indice(goal_node)) + func_info_rede(neighbor)
                stack.append((priority, neighbor[0]))

    print("Caminho não encontrado.")

