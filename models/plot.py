from models.grafo import Grafo
from models.vertice import Vertice
import plotly.graph_objects as go

def add_edge(fig: go.Figure, x: int, y: int, name: str, color):
    fig.add_trace(
        go.Scatter(
        name=name,
        x=x, y=y,
        line=dict(width=0.5, color=color),
        mode='lines')
    )

def add_vertex(fig: go.Figure, x: int, y: int, name: str, color):
    fig.add_trace(
        go.Scatter(
        name=name,
        x=x, y=y,
        mode='markers',
        hovertemplate='(%{x}, %{y})',
        marker=dict(
            # showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            # colorscale='YlGnBu',
            # reversescale=True,
            color=color,
            size=10,
            # colorbar=dict(
            #     thickness=15,
            #     title='Node Connections',
            #     xanchor='left',
            #     titleside='right'
            # ),
            line_width=1)
        )
    )

def update_grafo(g: Grafo, origem: Vertice, destino: Vertice, visitados) -> go.Figure:

    fig = go.Figure()

    edge_x = []
    edge_y = []
    edge_x_visitados = []
    edge_y_visitados = []

    for i in range(g.range):
        v1 = g.vertice_indice(i)
        for d in v1.vizinhos:
            if d[0] < i: pass
            v2 = g.vertice_indice(d[0])
            if i in visitados and d[0] in visitados:
                edge_x_visitados.append(v1.x)
                edge_y_visitados.append(v1.y)
                edge_x_visitados.append(v2.x)
                edge_y_visitados.append(v2.y)
                edge_x_visitados.append(None)
                edge_y_visitados.append(None)
            else:
                edge_x.append(v1.x)
                edge_y.append(v1.y)
                edge_x.append(v2.x)
                edge_y.append(v2.y)
                edge_x.append(None)
                edge_y.append(None)


    add_edge(fig, edge_x, edge_y, 'Não percorrida', '#999')
    add_edge(fig, edge_x_visitados, edge_y_visitados, 'Percorrida', '#000')

    node_x_visitado = []
    node_y_visitado = []
    node_x = []
    node_y = []

    for n in range(g.range):
        node = g.vertice_indice(n)
        if  n in visitados:
            node_x_visitado.append(node.x)
            node_y_visitado.append(node.y)
        else:
            node_x.append(node.x)
            node_y.append(node.y)

    add_vertex(fig, node_x, node_y, 'Não visitados', '#000')
    add_vertex(fig, node_x_visitado, node_y_visitado, 'Visitados', 'blue')
    add_vertex(fig, [origem.x], [origem.y], 'Origem', 'green')
    add_vertex(fig, [destino.x], [destino.y], 'Destino', 'red')
    
    return fig