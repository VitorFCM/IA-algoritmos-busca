from models.grafo import Grafo
from random import randrange
from dash import dcc, html, ctx
from dash.dependencies import Input, Output
from searches.profundidade import busca_profundidade
from searches.largura import busca_largura
from searches.djisktra import busca_djisktra
from searches.buscaInformada import busca_informada
from searches.funcoesAvaliacao import *
import models.plot as mp
import dash

global g, app, paused, origem, destino, caminho, arestas

app = dash.Dash(__name__)


def update_plot(n):
    index = n
    if n >= len(arestas):
        index = len(arestas) - 1
    elif n < 0:
        index = 0

    return mp.update_live_plot(g, [
        ([origem], "Origem", "green"),
        ([destino], "Destino", "red"),
    ], [(arestas[:index + 1], "Percorrida", "black")])


@app.callback(
    [Output(component_id='interval-component', component_property='interval'),
     Input('interval-refresh', 'value')]
)
def update_refresh_rate(value):
    return [value * 1000]


# @app.callback(
#     Output('interval-component', 'disabled', allow_duplicate=True),
#     Input('interval-component', 'n_intervals'),
#     prevent_initial_call=True,
# )
# def stop_update(n):
#     if n >= len(arestas):
#         return True
#     else:
#         return False


@app.callback(Output('live-update-graph', 'figure'),
              Input('interval-component', 'n_intervals'),
              )
def update_figure(n):
    return update_plot(n)


@app.callback(
    Output('interval-component', 'disabled'),
    Output('interval-component', 'n_intervals', allow_duplicate=True),
    Input('play', 'n_clicks'),
    Input('pause', 'n_clicks'),
    Input('next', 'n_clicks'),
    Input('previous', 'n_clicks'),
    Input('interval-component', 'n_intervals'),
    Input('interval-component', 'disabled'),
    prevent_initial_call=True,
)
def button_press(play_b, pause_b, next_b, previous_b, n_intervals, disabled):
    index = n_intervals
    if "play" == ctx.triggered_id:
        return False, index
    elif "pause" == ctx.triggered_id:
        return True, index
    elif "next" == ctx.triggered_id:
        index = n_intervals + 1
        return True, index
    elif "previous" == ctx.triggered_id:
        index = n_intervals - 1
        return True, index
    return disabled, n_intervals


@app.callback(
    Output('interval-component', 'n_intervals'),
    Input('search-dropdown', 'value'),
)
def select_search(value):
    if value == 'Busca em Profundidade':
        busca_profundidade(g, origem, destino, arestas, True)
        return 0
    elif value == 'Busca em Largura':
        busca_largura(g, origem, destino, arestas, True)
        return 0
    elif value == 'Djisktra':
        busca_djisktra(g, origem, destino, arestas, True)
        return 0
    elif value == 'Busca Best First':
        busca_informada(g, origem, destino, heuristica_best_first, info_rede_best_first, arestas, True)
        return 0
    elif value == 'Busca A*':
        busca_informada(g, origem, destino, heuristica_otimista, info_rede_A_estrela, arestas, True)
        return 0


if __name__ == "__main__":

    g = Grafo(n_range=50, prob=0.1)

    origem = randrange(g.range)
    destino = randrange(g.range)
    while origem == destino:
        destino = randrange(g.range)

    arestas = []
    # busca_profundidade(g, origem, destino, arestas, True)
    # busca_largura(g, origem, destino, arestas, True)

    app.layout = html.Div([
        dcc.Interval(
            id='interval-component',
            interval=1 * 1000,  # in milliseconds
            n_intervals=0,
            disabled=True
        ),
        html.H1('Rede Aleatória'),
        dcc.Graph(id='live-update-graph'),
        html.Div(children=[
            dcc.Dropdown(['Busca em Profundidade', 'Busca em Largura', 'Busca Best First', 'Busca A*', 'Djisktra'],
                         'Busca em Profundidade',
                         id='search-dropdown'),
        ]),
        html.Br(),
        html.Div(children=[
            dcc.Slider(
                min=0.5,
                max=2,
                step=0.5,
                value=1,
                id='interval-refresh',
                className="rc-slider"
            ),
            html.Div(children=[
                html.Button(children='↶', id='previous', n_clicks=0)
            ], style={'width': '5%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Button('Play', id='play', n_clicks=0)
            ], style={'display': 'inline-block'}),
            html.Div(children=[
                html.Button('Pause', id='pause', n_clicks=0)
            ], style={'display': 'inline-block'}),
            html.Div(children=[
                html.Button(children='↷', id='next', n_clicks=0)
            ], style={'width': '5%', 'display': 'inline-block'}),
        ], style={'width': '50%', 'display': 'inline-block'}),

        dcc.Graph(figure=mp.plot_graph(g))
    ], style=dict(textAlign='center'))

    app.run(debug=True)

