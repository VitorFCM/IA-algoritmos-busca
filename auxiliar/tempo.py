import time
####AREA PARA VER TEMPOS DE EXECUCAO


def mede_tempo(func,*args):

    print('Iniciando cronometro.')
    inicio = time.time()

    # Codigo de Busca

    aux = func(*args)

    ##
    fim = time.time()

    tempo = fim - inicio

    print(f"O tempo de execucao foi de {tempo} segundos")
    return tempo