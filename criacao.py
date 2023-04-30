from vertice import Vertice 
from random import randrange, uniform
from math import sqrt

def peso_aresta(v1, v2):
    return sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

def cria_grafo(n, p):
    vertices = []

    if(p < 0 or p > 1):
        print("A probabilidade 'p' precisa estar entre 0 e 1")
        return vertices

    cria_vertices(n, vertices)

    for indice_v1 in range(n):
        for indice_v2 in range(indice_v1 + 1, n):
            chance = uniform(0, 1)
            if(chance < p):
                v1 = vertices[indice_v1]
                v2 = vertices[indice_v2]
                
                peso = peso_aresta(v1, v2)

                v1.vizinhos.append((indice_v2, peso))
                v2.vizinhos.append((indice_v1, peso))

    return vertices

def cria_vertices(n, vertices):
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
