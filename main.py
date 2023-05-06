from models.grafo import Grafo
from random import randrange, uniform
from dash import dcc, html
from dash.dependencies import Input, Output
import models.grafo as gf
import models.plot as mp
import plotly.graph_objects as go
import dash

global g, app, origem, destino, caminho, passos
app = dash.Dash(__name__)


@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_figure(n):
    index = n
    if n >= len(passos):
        index = len(passos) - 1
    # print(f"Index :{index} List: {passos[index]}")
    # return mp.update_grafo(g, g.vertice_indice(origem), g.vertice_indice(destino), caminho[index], passos[index])
    return mp.update_live_plot(g, [
        (passos[index], "Visitados", "gray", "Percorrida", "black"),
        ([origem], "Origem", "green", "", "white"),
        ([destino], "Destino", "red", "", "white"),
    ])


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

    g = Grafo(n_range=50)
    caminho = [[]]
    passos = [[]]

    g.gerar_vertices()
    g.gerar_arestas(0.05)

    origem = randrange(g.range)
    destino = randrange(g.range)
    while origem == destino:
        destino = randrange(g.range)

    gf.busca_profundidade(g, origem, destino, caminho, passos, True)

    app.layout = html.Div([
        html.H1('Rede Aleatória'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
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
        ]),
        dcc.Graph(figure=mp.plot_graph(g))
    ], style=dict(textAlign='center'))

    app.run(debug=True)
