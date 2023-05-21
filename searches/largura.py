from models.grafo import Grafo


def busca_largura_rec(grafo: Grafo, origem: int, destino: int, visitados: list, fila: list, arestas: list, plot: bool):
    # TODO: Falta registrar as arestas percorridas
    visitados.append(origem)

    if origem == destino:
        return True, fila

    for v in grafo.vertice_indice(origem).vizinhos:
        if v[0] not in visitados:
            fila.append(v[0])
            if plot:
                arestas.append((origem, v[0]))
                if v[0] == destino:
                    return True, fila

    return False, fila


def busca_largura(grafo: Grafo, origem: int, destino: int, arestas=[], plot=False):
    visitados = []
    fila = [origem]
    status = False

    while fila and (not status):
        prox = fila[0]
        fila.pop(0)
        (status, fila) = busca_largura_rec(grafo, prox, destino, visitados, fila, arestas, plot)

    return status
