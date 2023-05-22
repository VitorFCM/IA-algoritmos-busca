from models.grafo import Grafo
from random import randrange
from dash import dcc, html
from dash.dependencies import Input, Output
from searches.profundidade import busca_profundidade
from searches.largura import busca_largura
import models.plot as mp
import dash
from auxiliar.tempo import mede_tempo

global g, app, origem, destino, caminho, arestas
app = dash.Dash(__name__)


@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_figure(n):
    index = n
    if n >= len(arestas):
        index = len(arestas) - 1

    return mp.update_live_plot(g, [
        ([origem], "Origem", "green"),
        ([destino], "Destino", "red"),
    ], [
                                   (arestas[:index + 1], "Percorrida", "black"),
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


# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def new_graph(n):
#     g = Grafo(n, p)


if __name__ == "__main__":

    g = Grafo(n_range=20, prob=0.1)

    origem = randrange(g.range)
    destino = randrange(g.range)
    while origem == destino:
        destino = randrange(g.range)

    arestas = [(origem, origem)]
    # busca_profundidade(g, origem, destino, arestas, True)
    busca_largura(g, origem, destino, arestas, True)
    print(arestas)

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

    ####AREA PARA VER TEMPOS DE EXECUCAO
    ##Paramentro eh a funcao a ser medido o tempo
    mede_tempo()
