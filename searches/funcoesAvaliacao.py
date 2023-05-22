from math import sqrt


#Heuristicas

def heuristica_best_first(vertice_atual, vertice_destino):
    x_atual, y_atual = vertice_atual.x, vertice_atual.y
    x_destino, y_destino = vertice_destino.x, vertice_destino.y

    distancia = sqrt((x_atual - x_destino) ** 2 + (y_atual - y_destino) ** 2)

    return distancia

def heuristica_pessimista(vertice_atual, vertice_destino): 
    return heuristica_best_first(vertice_atual, vertice_destino) * 2

def heuristica_otimista(vertice_atual, vertice_destino): 
    return heuristica_best_first(vertice_atual, vertice_destino) / 2


#Funcoes sobre dados da rede

def info_rede_best_first(vizinho):
    return 0

def info_rede_A_estrela(vizinho):
    return vizinho[1]
