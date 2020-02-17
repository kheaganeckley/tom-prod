#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:18:47 2020

@author: kheagan
"""


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from colorScheme import color
import dash
from app import app
import json
from dash.exceptions import PreventUpdate
import TomV2.Tom as to 
import TomV2.Bernolli as ber
from stlye import style_button, style_graph_grid, style_line , style_layout, style_input



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
#app.config.suppress_callback_exceptions = True



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
        #html.H1(id='test'),
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
   dcc.Store(id='slots'),
   dcc.Store(id='current_slot'),
   heading(),
   input(),
   plot_row()
],
style= style_layout)






inititate_slots = dict(
                slot1 = dict(
                    a = 1,
                    b = 1,
                    current_sample = 0,
                    name = 'slot1'
                ),
                slot2 = dict(
                    a = 1,
                    b = 1,
                    current_sample = 0,
                    name = 'slot2'
                ),
                slot3 = dict(
                    a = 1,
                    b = 1,
                    current_sample = 0,
                    name = 'slot3'
                )
            )




#######################################################
##                  
##                    store update
##                      
######################################################
@app.callback(
              Output('current_slot', 'data'),
              [Input('Button_to_select_slot', 'n_clicks')],
              [State('current_slot', 'data'),
               State('slots', 'data')]
             )
def slect_slot(n_clicks, current_slot, slots):
    if n_clicks is None:
            # prevent the None callbacks is important with the store component.
            # you don't want to update the store for nothing.
            raise PreventUpdate

        # Give a default data dict with 0 clicks if there's no data.    
    current_slot = current_slot or 'slot1'
    slots = slots or inititate_slots

    #update current slot 
    current_slot  = to.select_slot( slots , ber.sample)
    return current_slot 



#######################################################
##                 choose if you won or lost 
##                     update prior beliefs
##                       update graphs
######################################################
@app.callback(
               Output('slots', 'data'),
               [Input('Button', 'n_clicks'),],
               [State('was_success', 'value'),
                State('current_slot', 'data'),
                State('slots', 'data')
               ]
             )
def pull_lever(n_clicks, was_success, current_slot, slots): # add store 
        if n_clicks is None:
                raise PreventUpdate

        current_slot = current_slot or 'slot1'
        slots = slots or inititate_slots  
    
        #print(slots[currentslot])
       

        a,b = ber.update( was_success, slots[current_slot] )
        
        slots[current_slot]['a'] = a
        slots[current_slot]['b'] = b

        return slots
    




#use intermidate unpdates


#######################################################
##                  
##                    plots
##                      
######################################################
@app.callback(  [Output('slot1', 'figure'), 
                 Output('slot2', 'figure'),
                 Output('slot3', 'figure')],
                [Input('slots', 'modified_timestamp')],
                [State('slots', 'data')])
def draw_plots(sl,  slots):
        if sl is None:
            raise PreventUpdate

        slots = slots or inititate_slots

        plots = []

        for slot in slots.values():
            plots.append(ber.draw(slot))

        return  plots[0], plots[1], plots[2]



#######################################################
##                  
##                    current slot out
##                      
######################################################
@app.callback(  Output( 'selected_slot', 'children'),
                [Input('current_slot', 'modified_timestamp')],
                [State('current_slot', 'data')])
def slect_slot_display(cs, current_slot):
        if cs is None:
            raise PreventUpdate

        return  current_slot or 'slot1'





if __name__ == '__main__':
    app.run_server(debug=True)
