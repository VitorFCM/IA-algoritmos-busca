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
## [0] list[tuple[int, int]]: lista de arestas
## [1] str: nome da aresta
## [2] str: cor da aresta
def update_live_plot(g: Grafo, vertices_list: list[tuple[list[int], str, str]],
                     edges_list: list[tuple[list[tuple[int, int]], str, str]]) -> go.Figure:
    fig = go.Figure()

    # ---------------------------- Desenha o grafo original ---------------------------- #
    edge_x, edge_y = edges(g)
    add_edge(fig, edge_x, edge_y, 'Não percorrida', '#999')
    node_x, node_y = vertices(g)
    add_vertex(fig, node_x, node_y, 'Não visitado', '#fff')
    # ---------------------------------------------------------------------------------- #

    vertices_from_edges = set()
    for e in edges_list:
        x = []
        y = []
        for i in e[0]:
            v1 = g.vertice_indice(i[0])
            v2 = g.vertice_indice(i[1])
            vertices_from_edges.add(i[0])
            vertices_from_edges.add(i[1])
            x.append(v1.x)
            y.append(v1.y)
            x.append(v2.x)
            y.append(v2.y)
            x.append(None)
            y.append(None)
        add_edge(fig, x, y, e[1], e[2])

    x_e = []
    y_e = []
    for v in vertices_from_edges:
        v1 = g.vertice_indice(v)
        x_e.append(v1.x)
        y_e.append(v1.y)
    add_vertex(fig, x_e, y_e, "Visitado", "gray")

    for v in vertices_list:
        x = []
        y = []
        for i in v[0]:
            v1 = g.vertice_indice(i)
            x.append(v1.x)
            y.append(v1.y)
        add_vertex(fig, x, y, v[1], v[2])

    fig.update_layout(template="simple_white")

    return fig


def plot_graph(g: Grafo) -> go.Figure:
    fig = go.Figure()

    edge_x, edge_y = edges(g)

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