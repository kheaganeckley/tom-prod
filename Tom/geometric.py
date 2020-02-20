import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color
from plotly.subplots import make_subplots



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
    x = np.linspace(0,  1, 100)
    
    a = slot['a']
    b = slot['b']

    y = stat.beta.pdf(x, a, b)

    predictive_dist = 1/np.random.choice(x,10000,True, y/sum(y))

    Mean_prediction = round(np.mean(predictive_dist))

    title = 'Expected failures is {} before... from {}'.format(Mean_prediction, slot['name'])
        

    fig =make_subplots( rows=2, cols=1)

    trace = go.Scatter( x=x, y=y, marker= dict(
                color = color['trim']
    ))

    trace2 = go.Histogram( x =predictive_dist,
    marker=dict(
        color = color['secound']
    )
    )

    fig.add_trace(trace, row=1, col=1)
    fig.add_trace(trace2, row=2, col=1)

    fig.update_xaxes(title_text="The probablity of success", row=1, col=1)
    fig.update_xaxes(title_text="failures before first success ", row=2, col=1)

    fig.update_layout( title= title, 
                           template='plotly_dark',
                           width= 400,
                           showlegend = False
                           )

    return fig