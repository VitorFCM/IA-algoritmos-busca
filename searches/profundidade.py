def busca_profundidade(G, origem, destino, passos=[], debug=False):
    visitados = []
    busca_profundidade_rec(G, origem, destino, visitados, passos, debug)

def busca_profundidade_rec(G, origem, destino, visitados, passos, debug):
    if origem != destino:
        visitados.append(origem)
        if debug == True:
            passos.append(visitados.copy())
        for v in G.vertice_indice(origem).vizinhos:
            if v[0] not in visitados:
                if busca_profundidade_rec(G, v[0], destino, visitados, passos, debug) == True:
                    return True;
        return False
    else:
        return True
