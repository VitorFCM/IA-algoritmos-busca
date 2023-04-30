from vertice import Vertice 
from random import randrange

def cria_vertices(n):
    vertices = []
    coordenadas_usadas = {}
    for i in range(n):
        while(True):
            x = randrange(n + 1)
            y = randrange(n + 1)
            if(not x in coordenadas_usadas):
                coordenadas_usadas[x] = set({y})
                vertices.append(Vertice(x, y))
                break
            elif(not y in coordenadas_usadas[x]):
                coordenadas_usadas[x].add(y)
                vertices.append(Vertice(x, y))
                break

    return vertices
