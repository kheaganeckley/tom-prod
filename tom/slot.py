import plotly.express as pxt
import scipy.stats as stat
import numpy as np


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
        x = np.linspace(start = 0, end = 1,steps =  100)
        y = stat.beta.pdf(x, self.a, self.b)
        title = 'Our current belif in probablity of an favourable out come in {}'.format(self.name)
        fig = pxt.line( x = x, y = y, title = title, template='plotly_dark')
        return fig
    