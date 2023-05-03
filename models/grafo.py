from models.vertice import Vertice 
from random import randrange, uniform
from math import sqrt

class Grafo:
    def __init__(self, n_range):
        self.vertices = []
        self.range = n_range

    def vertice_indice(self, indice):
        if indice < 0 or indice >= self.range:
            print("Indice fora dos limites")
        return self.vertices[indice]

    def gerar_vertices(self):
        coords_usadas = []

        i = 0
        while i < self.range: 
            # Gera coordenadas aleatórias no plano
            x = randrange(self.range + 1)
            y = randrange(self.range + 1)
            coords = {'x':x,'y':y}

            # Se ao acaso gerar um par de coordenadas ja preenchidas, apenas repete o passo atual
            if (coords in coords_usadas):
                continue
            
            # Registra a nova coordenada e gera um vertice naquela posição
            coords_usadas.append(coords)
            self.vertices.append(Vertice(coords['x'],coords['y']))
            i+=1
    
    def gerar_arestas(self,p):
        # Percorre todos os pares de vertices possiveis
        for v1 in range(self.range):
            for v2 in range(v1 + 1,self.range):
                chance = uniform(0,1) # Gera um valor aleatório entre 0 e 1
                if chance <= p: # Se o valor estiver dentre o percentual determinado, gera uma aresta.
                    vert1 = self.vertices[v1]
                    vert2 = self.vertices[v2]
                    peso = sqrt((vert1.x - vert2.x)**2 + (vert1.y - vert2.y)**2)

                    vert1.vizinhos.append((v2,peso))
                    vert2.vizinhos.append((v1,peso))

def busca_profundidade(G, origem, destino, passos=[], debug=False):
    visitados = []
    busca_profundidade_rec(G, origem, destino, visitados, passos, debug)

def busca_profundidade_rec(G, origem, destino, visitados, passos, debug):
    if origem != destino:
        visitados.append(origem)
        if debug == True:
            passos.append(visitados.copy())
        for v in G.vertice_indice(origem).vizinhos:
            if v[0] not in visitados:
                if busca_profundidade_rec(G, v[0], destino, visitados, passos, debug) == True:
                    return True;
        return False
    else:
        return True