import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color
from plotly.subplots import make_subplots


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


def draw(slot, n):
    x = np.linspace(0,  1, 100)
    y = stat.beta.pdf(x,  slot['a'],  slot['b'])
    title = 'prob of favourable outcome in {}'.format(slot['name'])
        
    predict_sample =  n*np.random.choice(x, 10000, True, y/sum(y))

    Mean_prediction = round(np.mean(predict_sample),1)
    
    title = 'The expected successful trials is {} in {}'.format( Mean_prediction ,slot['name'])
        
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

    fig.update_xaxes(title_text="The probablity of success", row=1, col=1)
    fig.update_xaxes(title_text="Expected successful trails", row=2, col=1)

    fig.update_layout( title= title, 
                           template='plotly_dark',
                           width= 400,
                           showlegend = False
                           )

    return fig