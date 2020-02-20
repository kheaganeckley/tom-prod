import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color
from plotly.subplots import make_subplots




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
    
    
    
    predict_sample =  np.random.choice(x,10000,True, y/sum(y))

    Mean_prediction = round(np.mean(predict_sample),1)
    
    title = 'The expected occurances is {} in {}'.format( Mean_prediction ,slot['name'])
        
    fig =make_subplots( rows=2, cols=1)

    trace = go.Scatter( x=x, y=y, marker= dict(
                color = color['trim']
    ))

    trace2 = go.Histogram( x= predict_sample,
    marker=dict(
        color = color['secound']
    )
    )

    fig.add_trace(trace, row=1, col=1)
    fig.add_trace(trace2, row=2, col=1)

    fig.update_xaxes(title_text="The occurance", row=1, col=1)
    fig.update_xaxes(title_text="Expected occurance", row=2, col=1)

    fig.update_layout( title= title, 
                           template='plotly_dark',
                           width= 400,
                           showlegend = False
                           )

    return fig