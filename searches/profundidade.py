from models.grafo import Grafo

def busca_profundidade_rec(grafo:Grafo, origem:int, destino:int, visitados:list, arestas: list[tuple], plot: bool):
    visitados.append(origem)

    if origem == destino:
        return True
    
    for v in grafo.vertice_indice(origem).vizinhos:
        if v[0] not in visitados:
            if plot:
                arestas.append((origem, v[0]))
            if busca_profundidade_rec(grafo, v[0], destino, visitados, arestas, plot):
                return True
            
    return False


def busca_profundidade(grafo: Grafo, origem:int, destino:int, arestas=[], plot=False):
    visitados = []
    busca_profundidade_rec(grafo, origem, destino, visitados, arestas, plot)



