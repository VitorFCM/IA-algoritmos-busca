from models.grafo import Grafo
from auxiliar.tempo import mede_tempo
from random import randrange
import sys

from searches.profundidade import busca_profundidade
from searches.largura import busca_largura


#todo: colocar todos os algoritmos aqui para realizar o teste de desempenho

if __name__ == "__main__":

    # Foi necessario aumentar o maximo de profundidade da recursao
    # pois para 2000 vertices a busca em profundidade ultrapassava o limite
    sys.setrecursionlimit(10000)

    valores_p = [0.05, 0.025, 0.01]
    valores_tempo = [0.0, 0.0, 0.0, 0.0]
    n_testes = 10

    for p in valores_p:
        
        grafo = Grafo(2000, p)
        print(grafo.range)
        
        for i in range(n_testes):

            origem = randrange(grafo.range)
            destino = randrange(grafo.range)
            while origem == destino:
                destino = randrange(grafo.range)

            print("Origem: " + str(origem) + " destino: " + str(destino))

            valores_tempo[0] += mede_tempo(busca_profundidade(grafo, origem, destino))
            valores_tempo[1] += mede_tempo(busca_largura(grafo, origem, destino))

        
        medias_tempo = map(lambda total : total/n_testes, valores_tempo)
        medias_tempo = list(medias_tempo)
        print(medias_tempo)

    #found = busca_informada(grafo, start_node, goal_node, heuristica_best_first, info_rede_best_first)
    #if found:
    #    print("Caminho encontrado!")
    #else:
    #    print("Caminho não encontrado.")
