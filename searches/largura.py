from models.grafo import Grafo

def busca_largura_rec(Grafo:Grafo ,origem:int,destino:int,visitados:list,fila:list):
    # TODO: Falta registrar as arestas percorridas
    visitados.append(origem)

    if origem == destino:
        return [True,fila]
    
    for v in Grafo.vertice_indice(origem).vizinhos:
        if v[0] not in visitados:
            fila.append(v)
    
    return [False,fila]
    
def busca_largura(grafo:Grafo,origem:int,destino:int):
    visitados = []
    fila = [origem]
    status = False

    while (not fila) and (not status):
        prox = fila[0]
        fila.pop(0)
        status, fila = busca_largura_rec(grafo,origem,destino,visitados,fila)
    
    return status
