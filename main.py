from models.grafo import Grafo
import plotly.graph_objects as go

if __name__ == "__main__":
    g = Grafo(n_range=10)
    g.gerar_vertices()
    g.gerar_arestas(0.05)

    #for v in g.vertices:
    #    print(f'({v.x} , {v.y}) : {v.vizinhos}')
    
    edge_x = []
    edge_y = []
    for i in range(10):
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



    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in g.vertices:
        node_x.append(node.x)
        node_y.append(node.y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=['#188'],
            size=10,
            line_width=2)
        )

    node_trace.marker["color"] = ['#800' for i in range(8)]
        
    fig = go.Figure(data=[edge_trace, node_trace],
         layout=go.Layout(
            title='<br>Network graph made with Python',
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20,l=5,r=5,t=40),
            annotations=[ dict(
                text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                showarrow=False,
                xref="paper", yref="paper",
                x=0.005, y=-0.002 ) ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
            )

    import dash
    from dash import dcc
    from dash import html
    from dash import State, Output, Input


    app = dash.Dash()
    app.layout = html.Div([
        dcc.RadioItems(
            options=[
                {"label": "Bar", "value": 1},
                {"label": "Line", "value": 0},
            ],
            value=1,
            id="fig-type",
        ),
        html.Div(
            dcc.Graph(figure=fig, id="line-graph"),
            id="graph",
        ),
    ])

    @app.callback(
        Output("graph", "children"),
        [Input("fig-type", "value")],
        [State("line-graph", "figure")],
    )
    def toggle_modebar(i, fig):
        print(i)
        if(i == 0):
            node_trace.marker["color"] = ['#800' for j in range(8)]
        else:
            node_trace.marker["color"] = ['#188' for j in range(8)]

            
        fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
        return dcc.Graph(id="line-graph", figure=fig if fig else {})


    app.run_server(debug=True, use_reloader=False)
    #fig.show()

