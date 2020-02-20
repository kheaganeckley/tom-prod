import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
from colorScheme import color
from plotly.subplots import make_subplots


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
    

    predict_sample = np.random.choice(x,10000,True, y/sum(y))

    title = '{} mean predict sample {}'.format(slot['name'], round(np.mean(predict_sample),1))
        
   
   
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
    fig.update_xaxes(title_text="Expected outcome", row=2, col=1)

    fig.update_layout( title= title, 
                           template='plotly_dark',
                           width= 400,
                           showlegend = False
                           )
    return fig