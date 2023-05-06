class Vertice:
    """
    classe que define um vértice do grafo criado
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vizinhos = []
