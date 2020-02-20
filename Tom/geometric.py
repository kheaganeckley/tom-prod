import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color




def update(failures, slot):
    """
    docstring: todo
    """
   
    a =  slot['a'] + 1
    b =  slot['b'] + failures -1
    
    return a,b


def sample(slot):
    """
    docstring: todo
    """
    a = slot['a']
    b = slot['b']
    
    return  np.random.beta(a,b, 1)


def draw(slot):
    x = np.linspace(0,  10, 100)
    
    a = slot['a']
    b = slot['b']

    y = stat.beta.pdf(x,  a=a, scale =b)
  
    Mean_prediction = round(np.mean(1/np.random.choice(x,10000,True, y/sum(y))))

    title = 'Expected failures time is {} from {}'.format(Mean_prediction, slot['name'])
        
    trace = go.Scatter( x=x, y=y, marker= dict(
                color = color['trim']
    ))
    layout = go.Layout(xaxis= dict(title = 'The rate'),
                           yaxis= dict(title = 'density'),
                           title= title, 
                           template='plotly_dark',
                           width= 400,
    
                       )
    data = [trace]

    fig =  go.Figure(data, layout)
    return fig