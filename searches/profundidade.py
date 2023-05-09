def busca_profundidade(G, origem, destino, arestas=[], debug=False):
    visitados = []
    busca_profundidade_rec(G, origem, destino, visitados, arestas, debug)


def busca_profundidade_rec(G, origem, destino, visitados, arestas: list[list], debug):
    if origem != destino:
        visitados.append(origem)
        for v in G.vertice_indice(origem).vizinhos:
            if v[0] not in visitados:
                if debug:
                    arestas.append(arestas[len(arestas) - 1].copy())
                    arestas[len(arestas) - 1].append((origem, v[0]))
                if busca_profundidade_rec(G, v[0], destino, visitados, arestas, debug):
                    return True
        return False
    else:
        return True
