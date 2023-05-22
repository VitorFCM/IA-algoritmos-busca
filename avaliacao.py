from models.grafo import Grafo
from searches.buscaInformada import busca_informada
from searches.funcoesAvaliacao import *

#todo: colocar todos os algoritmos aqui para realizar o teste de desempenho

if __name__ == "__main__":
    #grafo = models.grafo.Grafo(n_range = 10,)
    # Criar um grafo
    n_range = 10  # Número de vértices no grafo
    prob = 0.05  # Probabilidade de geração de aresta entre dois vértices
    grafo = Grafo(n_range, prob)

    start_node = 0
    goal_node = 5

    found = busca_informada(grafo, start_node, goal_node, heuristica_best_first, info_rede_best_first)
    if found:
        print("Caminho encontrado!")
    else:
        print("Caminho não encontrado.")
