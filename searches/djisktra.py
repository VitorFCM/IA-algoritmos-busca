from models.grafo import Grafo
from auxiliar.tempo import mede_tempo
from random import randrange

def recursive_djisktra(grafo:Grafo,atual:int,dest:int,visitados:list[int],custos:list[int],caminhos:list[list[int]]):
    while True:
        visitados.append(atual)
        
        if grafo.vertice_indice(atual).vizinhos:
            # print(f'caminhos de {atual}: {grafo.vertice_indice(atual).vizinhos}')
            for a in grafo.vertice_indice(atual).vizinhos:
                viz = a[0]
                peso = a[1]

                if (custos[viz] == -1) or (custos[viz] > (custos[atual] + peso)):
                    custos[viz] = custos[atual] + peso
                    caminhos[viz] = caminhos[atual].copy()
                    caminhos[viz].append(atual)
        
        next = -1
        next_peso = 999999999999
        for i in range(grafo.range):
            if (i) not in visitados:
                if (custos[i] != -1) and (custos[i] < next_peso):
                    next_peso = custos[i]
                    next = i

        if next == -1:
            if len(caminhos[dest]) > 0:
                caminhos[dest].append(dest)
            return custos[dest], caminhos[dest]
        
        atual = next

      

def busca_djisktra(grafo:Grafo,origem:int,dest:int):
    visitados  = []
    custos = [-1] * (grafo.range) # -1 sendo considerado distância infinita
    caminhos =  [[]] * (grafo.range)


    custos[origem] = 0

    # print(f'custos:{custos}')
    # print(f'caminhos:{caminhos}')

    custos, caminhos = recursive_djisktra(grafo,origem,dest,visitados,custos,caminhos)

    print(f'custos:{custos}')
    print(f'caminhos:{caminhos}')


if __name__ == '__main__':
    g = Grafo(n_range=2000, prob=0.2)
    mede_tempo(busca_djisktra,g,1,19)