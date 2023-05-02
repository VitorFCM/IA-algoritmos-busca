from models.grafo import Grafo

if __name__ == "__main__":
    g = Grafo(n_range=5)
    g.gerar_vertices()
    g.gerar_arestas(0.5)

    for v in g.vertices:
        print(f'({v.x} , {v.y}) : {v.vizinhos}')

    
