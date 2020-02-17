#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:18:47 2020

@author: kheagan
"""





import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash
import json
from dash.exceptions import PreventUpdate
from seens import home, bernolli, possion
from componets import menu
from setup import app

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
#app.config.suppress_callback_exceptions = True


MenuArray = [
    dict(
        name = 'Bernolli',
        link = '/seens/bernolli'
    ),
       dict(
        name = 'Possion',
        link = '/seens/possion'
    ),
]


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    menu.menu(MenuArray),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    
    elif pathname == '/seens/bernolli':
        return bernolli.layout

    elif pathname == '/seens/possion':
        return possion.layout

    else:
        return '404'





if __name__ == '__main__':
    app.run_server(debug=True)
