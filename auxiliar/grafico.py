import matplotlib.pyplot as plt

def gera_grafico(
        valores_y, 
        valores_x=["Profundidade", "Largura", "Best-First", "A*", "Dijkstra"], 
        titulo=None, 
        xlabel=None, 
        ylabel=None):

    plt.bar(valores_x, valores_y, color ='maroon',
        width = 0.3)

    if titulo != None:
        plt.title(titulo)
    else:
        titulo = "Sem titulo"
        

    if xlabel != None:
        plt.xlabel(xlabel)

    if ylabel != None:
        plt.ylabel(ylabel)

    #todo: criar pasta para salvar as imagens
    #plt.savefig("figuras/" + str(titulo) + ".png")
    plt.show()

    return

