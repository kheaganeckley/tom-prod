#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:18:47 2020

@author: kheagan
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
#from tom.thompson_smapling import tompson_sampler

#from setup import app

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True




### css styles
style_graph_grid = dict(
    backgroundColor = 'black',
    display = 'flex',
    flexDirection = 'row',
    alignItems = 'center',
    justifyContent = 'center'    
)

style_line = dict(
    color = 'black'
)

style_layout = dict(
    display = 'flex',
    flexDirection = 'column',
    alignItems = 'center',
    justifyContent = 'center'
)



#tom = tompson_sampler()

#### dash componets serving as react componet wrapper 
def plot_row():
    return html.Div([
        dcc.Graph('slot1'),
        dcc.Graph('slot2'),
        dcc.Graph('slot3'),
    ],
     style = style_graph_grid)


def heading():
    return html.Div([
        html.H1('Thompson sampling to solve multi bandit promblem'),
        html.Hr(style= style_line)
    ])


def pull_lever_input():
    return  html.Div([
    dcc.RadioItems(
        id='was_success',
        options=[
            dict( label = 'You played a slot machine and doubled your money',
                  value = 'True'),
            dict( label = 'lost your moeny',
                  value = 'Flase'),
        ],
         value= 'True'
        ),
        html.Button('SUBMIT', id=''),
    ])

app.layout = html.Div([
    heading(),
    pull_lever_input(),
    plot_row()
],
style= style_layout)


@app.callback(
               [Output('slot1', 'figure'), 
                Output('slot2', 'figure'),
                Output('slot3', 'figure')],
               [Input('SUBMIT', 'n_clicks')],
              [State('was_success', 'value')]
            )
def play_a_round(n_clicks, was_success):
    
   print(n_clicks)
   print(was_success)
   if was_success is 'True':
       plots = tom.tom.a_round(was_success = True)
   else:
       plots = tom.tom.a_round(was_success = False)

   return plots[0], plots[1], plots[2]

if __name__ == '__main__':
    app.run_server(debug=True)