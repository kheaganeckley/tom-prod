import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
import pandas as pd
from colorScheme import color




def update(occurances, slot):
    """
    docstring: todo
    """
   
    a =  slot['a'] + occurances
    b =  slot['b'] + 1
    
    return a,b


def sample(slot):
    """
    docstring: todo
    """
    return  np.random.gamma( slot['a'], slot['b'], 1)


def draw(slot):
    x = np.linspace(0,  40, 100)
    y = stat.gamma.pdf(x,  slot['a'],  slot['b'])
    title = 'prob of favourable outcome in {}'.format(slot['name'])
        
    trace = go.Scatter( x=x, y=y, marker= dict(
                color = color['trim']
    ))
    layout = go.Layout(xaxis= dict(title = 'reward'),
                           yaxis= dict(title = 'density'),
                           title= title, 
                           template='plotly_dark',
                           width= 400,
    
                       )
    data = [trace]

    fig =  go.Figure(data, layout)
    return fig