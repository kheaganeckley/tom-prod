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
import Tom.exponetial as exp
from stlye import style_button, style_graph_grid, style_line , style_layout, style_input, style_input_text
from setup import app


def plot_row():
    return html.Div([
        dcc.Graph('slot1_exp'),
        dcc.Graph('slot2_exp'),
        dcc.Graph('slot3_exp'),
    ],
     style = style_graph_grid)



def heading():
    return html.Div([
        html.H1('Waiting times between occarances of something'),
        #html.H1(id='test'),
        html.Hr(style= style_line)
    ])



def input():
    return  html.Div([
       html.H3('Select a slot by sampling one number from each posterior'),
       html.H5('we want smallest waiting time (thus the greatest rate)'),
       html.Button('Select slot', id = 'Button_to_select_slot_exp', style= style_button),
       html.H3(id = 'selected_slot_exp'),
       html.Br(),
       html.H4('Then comment on...'),
       dcc.Input(
        id= 'input_exp',
        placeholder='How long did you wait',
        type='text',
        style= style_input_text
        ),
       html.Button('SUBMIT', id='Button_exp', style= style_button),
    ],
    style=style_input)

layout = html.Div([
   dcc.Store(id='slots_exp'),
   dcc.Store(id='current_slot_exp'),
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
              Output('current_slot_exp', 'data'),
              [Input('Button_to_select_slot_exp', 'n_clicks')],
              [State('current_slot_exp', 'data'),
               State('slots_exp', 'data')]
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
    current_slot  = to.select_slot( slots , exp.sample)
    return current_slot 



#######################################################
##                 choose if you won or lost 
##                     update prior beliefs
##                       update graphs
######################################################
@app.callback(
               Output('slots_exp', 'data'),
               [Input('Button_exp', 'n_clicks'),],
               [State('input_exp', 'value'),
                State('current_slot_exp', 'data'),
                State('slots_exp', 'data'),
               ]
             )
def pull_lever(n_clicks, value, current_slot, slots): # add store 
        if n_clicks is None:
                raise PreventUpdate

        current_slot = current_slot or 'slot1'
        slots = slots or inititate_slots  
    
        #print(slots[currentslot])
       
        
        a,b = exp.update( float(value), slots[current_slot] )
        
        slots[current_slot]['a'] = a
        slots[current_slot]['b'] = b

        return slots
    




#use intermidate unpdates


#######################################################
##                  
##                    plots
##                      
######################################################
@app.callback(  [Output('slot1_exp', 'figure'), 
                 Output('slot2_exp', 'figure'),
                 Output('slot3_exp', 'figure')],
                [Input('slots_exp', 'modified_timestamp')],
                [State('slots_exp', 'data')])
def draw_plots(sl,  slots):
        if sl is None:
            raise PreventUpdate

        slots = slots or inititate_slots

        plots = []

        for slot in slots.values():
            plots.append(exp.draw(slot))

        return  plots[0], plots[1], plots[2]



#######################################################
##                  
##                    current slot out
##                      
######################################################
@app.callback(  Output( 'selected_slot_exp', 'children'),
                [Input('current_slot_exp', 'modified_timestamp')],
                [State('current_slot_exp', 'data')])
def slect_slot_display(cs, current_slot):
        if cs is None:
            raise PreventUpdate

        return  current_slot or 'slot1'








