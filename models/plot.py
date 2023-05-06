from models.grafo import Grafo
from models.vertice import Vertice
import plotly.graph_objects as go


def edges(g: Grafo):
    edge_x = []
    edge_y = []

    for i in range(g.range):
        v1 = g.vertice_indice(i)
        for d in v1.vizinhos:
            if d[0] < i:
                continue
            v2 = g.vertice_indice(d[0])
            edge_x.append(v1.x)
            edge_y.append(v1.y)
            edge_x.append(v2.x)
            edge_y.append(v2.y)
            edge_x.append(None)
            edge_y.append(None)

    return edge_x, edge_y


def vertices(g: Grafo):
    node_x = []
    node_y = []

    for n in range(g.range):
        node = g.vertice_indice(n)
        node_x.append(node.x)
        node_y.append(node.y)

    return node_x, node_y


def add_edge(fig: go.Figure, x, y, name: str, color):
    fig.add_trace(
        go.Scatter(
            name=name,
            x=x, y=y,
            line=dict(width=0.5, color=color),
            mode='lines')
    )


def add_vertex(fig: go.Figure, x, y, name: str, color):
    fig.add_trace(
        go.Scatter(
            name=name,
            x=x, y=y,
            mode='markers',
            hovertemplate='(%{x}, %{y})',
            marker=dict(
                # showscale=True,
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
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


## [0] list[int]: lista de vertices
## [1] str: nome do vértice
## [2] str: cor do vértice
## [3] str: nome da aresta
## [4] str: cor da aresta que une os vértices
def update_live_plot(g: Grafo, v: list[tuple[list[int], str, str, str, str]]) -> go.Figure:
    fig = go.Figure()

    edge_x, edge_y = edges(g)
    add_edge(fig, edge_x, edge_y, 'Não percorrida', '#999')

    node_x, node_y = vertices(g)
    add_vertex(fig, node_x, node_y, 'Não visitados', '#fff')

    for l in v:
        x = []
        y = []
        for i in l[0]:
            v1 = g.vertice_indice(i)
            x.append(v1.x)
            y.append(v1.y)
            # if i > 0 and i % 2 == 0:
            #     x.append(None)
            #     y.append(None)

        # if len(x) > 1:
            # add_edge(fig, x, y, l[3], l[4])
        add_vertex(fig, x, y, l[1], l[2])

    fig.update_layout(template="simple_white")

    return fig


def plot_graph(g: Grafo) -> go.Figure:
    fig = go.Figure()

    edge_x, edge_y = edges(g)
    # node_x, node_y = vertices(g)

    node_x = []
    node_y = []
    neighbors = []

    for n in range(g.range):
        node = g.vertice_indice(n)
        node_x.append(node.x)
        node_y.append(node.y)
        neighbors.append(len(node.vizinhos))

    fig.add_trace(
        go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color="gray"),
            mode='lines')
    )

    fig.update_layout(template="simple_white")

    fig.add_trace(
        go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            marker=dict(
                # showscale=True,
                # colorscale options
                # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
                # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
                # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
                colorscale='Gray',
                reversescale=True,
                color=neighbors,
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Número de arestas',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=1),
            hovertemplate='Coordenadas: (%{x}, %{y}) - Arestas: %{marker.color}',
        )
    )

    fig.update_layout(title="Número de Arestas por Vértice", showlegend=False)

    return fig


def update_grafo(g: Grafo, origem: Vertice, destino: Vertice, caminho, visitados) -> go.Figure:
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

    node_x_caminho = []
    node_y_caminho = []
    node_x_visitado = []
    node_y_visitado = []
    node_x = []
    node_y = []

    for n in range(g.range):
        node = g.vertice_indice(n)
        if n in visitados:
            node_x_visitado.append(node.x)
            node_y_visitado.append(node.y)
        if n in caminho:
            node_x_caminho.append(node.x)
            node_y_caminho.append(node.y)
        else:
            node_x.append(node.x)
            node_y.append(node.y)

    add_vertex(fig, node_x, node_y, 'Não visitados', '#fff')
    add_vertex(fig, node_x_visitado, node_y_visitado, 'Visitados', 'gray')
    add_vertex(fig, node_x_caminho, node_y_caminho, 'Caminho', 'black')
    add_vertex(fig, [origem.x], [origem.y], 'Origem', 'green')
    add_vertex(fig, [destino.x], [destino.y], 'Destino', 'red')

    fig.update_layout(template="simple_white")

    return fig
