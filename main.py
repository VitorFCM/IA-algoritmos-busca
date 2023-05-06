from models.grafo import Grafo
from random import randrange
from dash import dcc, html
from dash.dependencies import Input, Output
from searches.profundidade import busca_profundidade
import models.plot as mp
import dash

global g, app, origem, destino, passos
app = dash.Dash(__name__)

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

@app.callback(
    [
        Output('button', 'children'),
        Output('interval-component', 'disabled')
    ],
    Input('button', 'n_clicks'),
)
def update_interval(n):
    if n % 2 == 0:
        return 'Play', True
    else:
        return 'Pause', False

    
if __name__ == "__main__":

    g = Grafo(n_range=20, prob=0.5)
    passos = [[]]

    origem = randrange(g.range)
    destino = randrange(g.range)
    while origem == destino:
        destino = randrange(g.range)

    busca_profundidade(g, origem, destino, passos, True)

    app.layout = html.Div([
        html.H1('Rede Aleatória'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0,
            disabled=True
        ),
        html.Div(title='Delay (s)', children=[
        dcc.Slider(
            min=0.5, 
            max=2, 
            step=0.5, 
            value=1, 
            id='interval-refresh',
            className="rc-slider"
        ),
        html.Button(children='Play', id='button', n_clicks=0) 
    ])
    ], style=dict(textAlign='center'))

    app.run(debug=True)
