from models.grafo import Grafo

def busca_profundidade_rec(grafo:Grafo, origem:int, destino:int, visitados:list, arestas: list[tuple], plot: bool):
    visitados.append(origem)

    if origem == destino:
        return 0
    
    for v in grafo.vertice_indice(origem).vizinhos:
        if v[0] not in visitados:
            if plot:
                arestas.append((origem, v[0]))
            
            result = busca_profundidade_rec(grafo, v[0], destino, visitados, arestas, plot)
            if result != -1:
                return v[1] + result 
            
    return -1


def busca_profundidade(grafo: Grafo, origem:int, destino:int, arestas=[], plot=False):
    visitados = []
    arestas.clear()
    arestas.append((origem, origem))
    return busca_profundidade_rec(grafo, origem, destino, visitados, arestas, plot)



