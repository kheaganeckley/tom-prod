import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color


def update(x, n, slot):
    """
    docstring: todo
    """
    a = slot['a'] + x
    b = slot['b'] + n -x
    return a,b


def sample(slot):
    """
    docstring: todo
    """
    return  np.random.beta( slot['a'], slot['b'], 1 )


def draw(slot):
    x = np.linspace(0,  1, 100)
    y = stat.beta.pdf(x,  slot['a'],  slot['b'])
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