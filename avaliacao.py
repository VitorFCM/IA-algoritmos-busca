from models.grafo import Grafo
from auxiliar.tempo import mede_tempo
from auxiliar.grafico import gera_grafico
from searches.buscaInformada import busca_informada
from searches.funcoesAvaliacao import *
from searches.profundidade import busca_profundidade
from searches.largura import busca_largura
from random import randrange
import sys

if __name__ == "__main__":

    # Foi necessario aumentar o maximo de profundidade da recursao
    # pois para 2000 vertices a busca em profundidade ultrapassava o limite
    sys.setrecursionlimit(10000)

    valores_p = [0.05, 0.025, 0.01]
    valores_tempo = [0.0, 0.0, 0.0, 0.0]
    valores_custo = [0.0, 0.0, 0.0, 0.0]
    n_testes = 10

    for p in valores_p:
        
        grafo = Grafo(2000, p)
        
        for i in range(n_testes):

            origem = randrange(grafo.range)
            destino = randrange(grafo.range)
            while origem == destino or busca_informada(grafo, origem, destino, heuristica_best_first, info_rede_best_first) == -1:
                destino = randrange(grafo.range)

            #Busca em profundidade
            tempo, custo = mede_tempo(busca_profundidade(grafo, origem, destino))
            valores_tempo[0] += tempo
            valores_custo[0] += custo

            #Busca em largura
            #todo

            #Best first
            tempo, custo = mede_tempo(busca_informada(grafo, origem, destino, heuristica_best_first, info_rede_best_first))
            valores_tempo[2] += tempo
            valores_custo[2] += custo

            #A*
            tempo, custo = mede_tempo(busca_informada(grafo, origem, destino, heuristica_otimista, info_rede_A_estrela))
            valores_tempo[3] += tempo
            valores_custo[3] += custo

        
        medias_tempo = map(lambda total : total/n_testes, valores_tempo)
        medias_tempo = list(medias_tempo)

        medias_custo = map(lambda total : total/n_testes, valores_custo)
        medias_custo = list(medias_custo)

        gera_grafico(valores_y=medias_tempo, titulo="Tempos - n=2000 p=" + str(p*100) + "%")
        gera_grafico(valores_y=medias_custo, titulo="Custos - n=2000 p=" + str(p*100) + "%")

