import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color




def update(waiting_time, slot):
    """
    docstring: todo
    """
   

    a =  slot['a'] + 1
    b =  slot['b'] + waiting_time
    



    return a,b


def sample(slot):
    """
    docstring: todo
    """
    a = slot['a']
    b = slot['b']
    scale = 1/b
    shape = a
    
    return  np.random.gamma( shape, scale, 1)


def draw(slot):
    x = np.linspace(0,  10, 100)
    
    a = slot['a']
    b = slot['b']
    scale = 1/b
    shape = a

    y = stat.gamma.pdf(x,  a= shape, scale =scale)
  
    MLE = round(np.mean(1/np.random.choice(x,10000,True, y/sum(y))))

    title = 'Expected waiting time is {} from {}'.format(MLE, slot['name'])
        
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