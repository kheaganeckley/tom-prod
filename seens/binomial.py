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
import json
from dash.exceptions import PreventUpdate
import Tom.Tom as to 
import Tom.Binomial as bin
from stlye import style_button, style_graph_grid, style_line , style_layout, style_input, style_input_text
from setup import app


def plot_row():
    return html.Div([
        dcc.Graph('slot1_bin'),
        dcc.Graph('slot2_bin'),
        dcc.Graph('slot3_bin'),
    ],
     style = style_graph_grid)



def heading():
    return html.Div([
        html.H1('Proportional data'),
        #html.H1(id='test'),
        html.Hr(style= style_line)
    ])



def input():
    return  html.Div([
       html.H3('Select a slot by sampling one number from each posterior'),
       html.Button('Select slot', id = 'Button_to_select_slot_bin', style= style_button),
       html.H3(id = 'selected_slot_bin'),
       html.Br(),
       html.H4('Then comment on...'),
       dcc.Input(
        id= 'input_bin_success',
        placeholder='How many success',
        type='text',
        style= style_input_text
        ),
          dcc.Input(
        id= 'input_bin_trials',
        placeholder='How many trials',
        type='text',
        style= style_input_text
        ),
       html.Button('SUBMIT', id='Button_bin', style= style_button),
    ],
    style=style_input)

layout = html.Div([
   dcc.Store(id='n'),
   dcc.Store(id='slots_bin'),
   dcc.Store(id='current_slot_bin'),
   heading(),
   input(),
   plot_row()
],
style= style_layout)




initialise_n = 0

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
              Output('current_slot_bin', 'data'),
              [Input('Button_to_select_slot_bin', 'n_clicks')],
              [State('current_slot_bin', 'data'),
               State('slots_bin', 'data')]
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
    current_slot  = to.select_slot( slots , bin.sample)
    return current_slot 



#######################################################
##                 choose if you won or lost 
##                     update prior beliefs
##                       update graphs
######################################################
@app.callback(
               [Output('slots_bin', 'data'),
                Output('n', 'data')
               ],
               [Input('Button_bin', 'n_clicks'),],
               [State('input_bin_success', 'value'),
                State('input_bin_trials', 'value'),
                State('current_slot_bin', 'data'),
                State('slots_bin', 'data'),
               ]
             )
def pull_lever(n_clicks, success, trials, current_slot, slots): # add store 
        if n_clicks is None:
                raise PreventUpdate

        current_slot = current_slot or 'slot1'
        slots = slots or inititate_slots  
        n = initialise_n or int(trials)
        #print(slots[currentslot])
       
        
        a,b = bin.update( int(success), int(trials), slots[current_slot] )
        
        slots[current_slot]['a'] = a
        slots[current_slot]['b'] = b

        return slots, n    




#use intermidate unpdates


#######################################################
##                  
##                    plots
##                      
######################################################
@app.callback(  [Output('slot1_bin', 'figure'), 
                 Output('slot2_bin', 'figure'),
                 Output('slot3_bin', 'figure')],
                [Input('slots_bin', 'modified_timestamp')],
                [State('slots_bin', 'data'),
                 State('n', 'data')
                ])
def draw_plots(sl,  slots, n):
        if sl is None:
            raise PreventUpdate

        slots = slots or inititate_slots
        n = initialise_n or n

        plots = []

        for slot in slots.values():
            plots.append(bin.draw(slot, n))

        return  plots[0], plots[1], plots[2]



#######################################################
##                  
##                    current slot out
##                      
######################################################
@app.callback(  Output( 'selected_slot_bin', 'children'),
                [Input('current_slot_bin', 'modified_timestamp')],
                [State('current_slot_bin', 'data')])
def slect_slot_display(cs, current_slot):
        if cs is None:
            raise PreventUpdate

        return  current_slot or 'slot1'








