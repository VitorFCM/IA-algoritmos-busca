from models.grafo import Grafo
from random import randrange, uniform
from dash import dcc, html
from dash.dependencies import Input, Output
import models.grafo as gf
import models.plot as mp
import plotly.graph_objects as go
import dash

app = dash.Dash()
g = Grafo(n_range=100)
passos = [[]]
origem = destino = 0

@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_figure(n):
    index = n
    if n >= len(passos):
        index = len(passos) - 1
    # print(f"Index :{index} List: {passos[index]}")
    return mp.update_grafo(g, g.vertice_indice(origem), g.vertice_indice(destino), passos[index])

@app.callback(
    [Output(component_id='interval-component', component_property='interval')],
    [Input('interval-refresh', 'value')])
def update_refresh_rate(value):
    return [value * 1000]
    
if __name__ == "__main__":

    g.gerar_vertices()
    g.gerar_arestas(0.05)
    
    origem = randrange(g.range)
    destino = randrange(g.range)
    while origem == destino:
        destino = randrange(g.range)

    gf.busca_profundidade(g, origem, destino, passos, True)

    app.layout = html.Div([
        html.H1('Rede Aleatória'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        ),
        html.Div(title='Delay (s)', children=[
        dcc.Slider(min=0.5, max=2, step=0.5, value=1, id='interval-refresh'
        ), 
    ])
    ])

    app.run(debug=True)
