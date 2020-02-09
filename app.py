#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:18:47 2020

@author: kheagan
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from tom.thompson_smapling import tompson_sampler
from colorScheme import color
from setup import app






### css styles
style_graph_grid = dict(
    backgroundColor = color['background'],
    display = 'flex',
    flexDirection = 'row',
    alignItems = 'space-evenly',
    justifyContent = 'space-evenly', 
    width = '100%',   
    margin = '20px' 
)


style_line = dict(
    borderColor = color['trim']
)

style_layout = dict(
    backgroundColor = color['background'],
    color = color['text'],
    display = 'flex',
    flexDirection = 'column',
    alignItems = 'center',
    justifyContent = 'center'
)

style_button = dict(
    borderColor = color['trim'],
    color = color['trim']
)

style_input = dict(
    display = 'flex',
    flexDirection = 'column',
    alignItems = 'center'
)


tom = tompson_sampler()
previous_reset_n_clicks = 0


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
        html.H1(id='test'),
        html.Hr(style= style_line)
    ])



def input():
    return  html.Div([
       html.H3('Slect a slot by sampling one num from each posterior'),
       html.Button('Select slot', id = 'Button_to_select_slot', style= style_button),
       html.Br(),
       html.Br(),
       html.H3(id = 'selected_slot'),
       dcc.RadioItems(
        id='was_success',
        options=[
            dict( label = 'doubled your money',
                  value = 'True'),
            dict( label = 'lost your moeny',
                  value = 'False'),
        ],
        value= 'True'
        ),
        html.Button('SUBMIT', id='Button', style= style_button),
    ],
    style=style_input)

app.layout = html.Div([
   heading(),
   input(),
   plot_row()
],
style= style_layout)









#######################################################
##                  
##                    select a slot
##                      
######################################################
@app.callback(
              Output( 'selected_slot', 'children'),
               [Input('Button_to_select_slot', 'n_clicks')],
             )
def select_slot(n_clicks):
    selected_slot = tom.select_slot()
    print(selected_slot)
    return  selected_slot



#######################################################
##                 choose if you won or lost 
##                     update prior beliefs
##                       update graphs
######################################################
@app.callback(
              [
                Output('slot1', 'figure'), 
                Output('slot2', 'figure'),
                Output('slot3', 'figure'),
               ],
               [Input('Button', 'n_clicks'),],
               [State('was_success', 'value')]
             )
def pull_lever(n_clicks, was_success):
        if was_success == 'True':
                plots = tom.a_round(was_success = True)
        else:
            plots = tom.a_round(was_success = False)

        return plots[0], plots[1], plots[2]
    

if __name__ == '__main__':
    app.run_server(debug=True)
