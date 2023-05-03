import plotly.graph_objects as go

def add_edge(fig, x, y, color):
    fig.add_trace(
        go.Scatter(
        x=x, y=y,
        line=dict(width=0.5, color=color),
        hoverinfo='none',
        mode='lines')
    )

def add_vertex(fig, x, y, color):
    fig.add_trace(
        go.Scatter(
        x=x, y=y,
        mode='markers',
        hoverinfo='text',
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
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=1)
        )
    )

def update_grafo(g):

    fig = go.Figure()

    edge_x = []
    edge_y = []
    for i in range(g.range):
        v1 = g.vertice_indice(i)
        for d in v1.vizinhos:
            if d[0] < i: pass
            edge_x.append(v1.x)
            edge_y.append(v1.y)
            v2 = g.vertice_indice(d[0]) 
            edge_x.append(v2.x)
            edge_y.append(v2.y)
            edge_x.append(None)
            edge_y.append(None)


    add_edge(fig, edge_x, edge_y, '#999')

    node_x_visitado = []
    node_y_visitado = []
    node_x = []
    node_y = []

    for node in g.vertices:
        if not node.visitado:
            node_x.append(node.x)
            node_y.append(node.y)
        else:
            node_x_visitado.append(node.x)
            node_y_visitado.append(node.y)

    add_vertex(fig, node_x, node_y, '#000')
    add_vertex(fig, node_x_visitado, node_y_visitado, '#298')
    
    return fig