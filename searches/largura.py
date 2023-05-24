from models.grafo import Grafo


def busca_largura_rec(grafo: Grafo, origem: tuple, destino: int, visitados: list, fila: list, arestas: list, plot: bool):
    # TODO: Falta registrar as arestas percorridas
    visitados.append(origem)

    if origem[0] == destino:
        return origem[1], fila

    for v in grafo.vertice_indice(origem[0]).vizinhos:
        if v[0] not in visitados:
            fila.append((v[0], origem[1] + v[1]))
            if plot:
                arestas.append((origem, v[0]))
                if v[0] == destino:
                    return origem[1] + v[1], fila

    return -1, fila


def busca_largura(grafo: Grafo, origem: int, destino: int, arestas=[], plot=False):
    visitados = []
    fila = [(origem, 0)]
    status = -1
    arestas.clear()
    arestas.append((origem, origem))
    while fila and status == -1:
        prox = fila[0]
        fila.pop(0)
        (status, fila) = busca_largura_rec(grafo, prox, destino, visitados, fila, arestas, plot)

    return status
