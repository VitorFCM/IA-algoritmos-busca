from models.grafo import Grafo
from auxiliar.tempo import mede_tempo
from auxiliar.grafico import gera_grafico
from searches.bestFirst import best_first
from searches.funcoesAvaliacao import *
from searches.profundidade import busca_profundidade
from searches.largura import busca_largura
from searches.dijkstra import busca_dijkstra
from random import randrange
import sys

if __name__ == "__main__":

    # Foi necessario aumentar o maximo de profundidade da recursao
    # pois para 2000 vertices a busca em profundidade ultrapassava o limite
    sys.setrecursionlimit(10000)

    valores_p = [0.05, 0.025, 0.01]
    n_testes = 10
    algos = ["Profundidade", "Largura", "Best-First", "A*", "Dijkstra"]

    for p in valores_p:
        
        grafo = Grafo(2000, p)
        
        valores_tempo = [0.0, 0.0, 0.0, 0.0, 0.0]
        valores_custo = [0.0, 0.0, 0.0, 0.0, 0.0]

        for i in range(n_testes):

            origem = randrange(grafo.range)
            destino = randrange(grafo.range)
            while origem == destino or best_first(grafo, origem, destino, heuristica_best_first) == -1:
                destino = randrange(grafo.range)

            #Busca em profundidade
            tempo, custo = mede_tempo(busca_profundidade, grafo, origem, destino)
            valores_tempo[0] += tempo
            valores_custo[0] += custo

            #Busca em largura
            tempo, custo = mede_tempo(busca_largura, grafo, origem, destino)
            valores_tempo[1] += tempo
            valores_custo[1] += custo

            #Best first
            tempo, custo = mede_tempo(best_first, grafo, origem, destino, heuristica_best_first)
            valores_tempo[2] += tempo
            valores_custo[2] += custo

            #A*
            tempo, custo = mede_tempo(busca_dijkstra, grafo, origem, destino, heuristica_best_first)
            valores_tempo[3] += tempo
            valores_custo[3] += custo

            #Dijkstra
            tempo, custo = mede_tempo(busca_dijkstra, grafo, origem, destino)
            valores_tempo[4] += tempo
            valores_custo[4] += custo

        
        medias_tempo = map(lambda total : total/n_testes, valores_tempo)
        medias_tempo = list(medias_tempo)

        medias_custo = map(lambda total : total/n_testes, valores_custo)
        medias_custo = list(medias_custo)

        print("Para " + str(p*100) + "%:")
        for a in range(len(algos)):
            print(algos[a] + " - tempo: " + str(medias_tempo[a]) + " custo: " + str(medias_custo[a]))

        print()


        gera_grafico(valores_y=medias_custo, titulo="Custos - n=2000 p=" + str(p*100) + "%")
        gera_grafico(valores_y=medias_tempo, titulo="Tempos - n=2000 p=" + str(p*100) + "%")
        


