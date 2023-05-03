from models.grafo import Grafo
from random import randrange, uniform
import models.plot as mp
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash()
g = Grafo(n_range=100)
g.gerar_vertices()
g.gerar_arestas(0.05)

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_figure(n):
    for vertex in g.vertices:
        p = uniform(0, 1)
        if (p > 0.5):
            vertex.visitado = True
        else:
            vertex.visitado = False
    
    return mp.update_grafo(g)
    
if __name__ == "__main__":

    app.layout = html.Div([
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])

    app.run_server(debug=True)
