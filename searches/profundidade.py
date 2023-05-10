from models.grafo import Grafo

def busca_profundidade_rec(grafo:Grafo, origem:int, destino:int, visitados:list, arestas: list[tuple], debug:bool):
    visitados.append(origem)

    if origem == destino:
        return True
    
    for v in grafo.vertice_indice(origem).vizinhos:
        if v[0] not in visitados:
            if debug:
                #arestas.append(arestas[len(arestas) - 1].copy())
                #arestas[len(arestas) - 1].append((origem, v[0]))
                arestas.append((origem, v[0]))
            if busca_profundidade_rec(grafo, v[0], destino, visitados, arestas, debug):
                return True
            
    return False


def busca_profundidade(grafo: Grafo, origem:int, destino:int, arestas=[], debug=False):
    visitados = []
    busca_profundidade_rec(grafo, origem, destino, visitados, arestas, debug)



