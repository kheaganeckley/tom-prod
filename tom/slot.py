import plotly.express as pxt
import plotly.graph_objects as go
import scipy.stats as stat
import numpy as np
import pandas as pd
from colorScheme import color

print('slot works')

class slot():
    """
    docstring: each slot object has a posterior distribution and vector of paramters a and b
    """
    def __init__(self, a, b, name, current_sample = 0):
        self.a = a
        self.b = b
        self.name = name
        self.current_sample = current_sample
    
    def sample_posterior_beta(self, number):  
        a = np.array(self.a)
        b = np.array(self.b)
        return  np.random.beta(a,b,1)
    
    def draw(self):
        x = np.linspace(0,  1, 100)
        y = stat.beta.pdf(x, self.a, self.b)
        title = 'prob of favourable outcome in {}'.format(self.name)
        
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
    