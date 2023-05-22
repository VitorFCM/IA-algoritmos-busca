import time
####AREA PARA VER TEMPOS DE EXECUCAO


def mede_tempo(func):

    inicio = time.time()

    # Codigo de Busca

    aux = func

    ##
    fim = time.time()

    tempo = fim - inicio

    print(f"O tempo de execucao foi de {tempo} segundos")
    return tempo