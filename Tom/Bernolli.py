import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
import pandas as pd
from colorScheme import color

###dfd
def update(was_success, slot):
    """
    docstring: todo
    """
    print('before update a={} and b={}'.format(slot['a'],slot['b']))
    print('was success {}'.format(was_success))
    #local varibles
    a = slot['a']
    b = slot['b']

    if was_success == 'True': # add 1 to a in beta (the loc parm
            a = a  + 1
        
    else:  ## if was not sucess add 1 to b in beta (the sale parm) 
            b = b  + 1
    
    print('After update a={} and b={}'.format(slot['a'],slot['b']))
 

    return a,b


def sample(slot):
    """
    docstring: todo
    """
    return  np.random.beta( slot['a'], slot['b'], 1)[0]


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