import plotly.express as pxt
import scipy.stats as stat
from tom.slot import slot

print('tom works')

class tompson_sampler():
    """
    docstring: a tomson sampler
    """

    def __init__(self, a1 =1.0, b1 =1.0, a2 =1.0, b2 =1.0, a3 =1.0, b3=1.0):        
        self.slot1 = slot(a1 , b1, 'slot 1')
        self.slot2 = slot(a2 , b2, 'slot 2')
        self.slot3 = slot(a3 , b3, 'slot 3')
        self.selected_slot = slot(1 , 1, 'initialise with dummy nonsense')


    def array_of_slots(self):
        return [self.slot1,  self.slot2, self.slot3 ]
    

    def select_slot(self):    
        self.selected_slot.current_sample = 0 

        for slot in self.array_of_slots():
            sample_from_beta = slot.sample_posterior_beta(1)
            if  sample_from_beta >  self.selected_slot.current_sample:
                self.selected_slot = slot
                self.selected_slot.current_sample = sample_from_beta
            print('sample {} from {}'.format(sample_from_beta, slot.name))
               
        print('max sample currently is {} from {}'.format(self.selected_slot.current_sample , self.selected_slot.name))
        return self.selected_slot.name

    
    def pull_lever(self, was_success, slot):   
        if was_success is True: # add 1 to a in beta (the loc parm
            slot.a += 1
        
        else:  ## if was not sucess add 1 to b in beta (the sale parm) 
            slot.b += 1
    

    def draw_posteriors_of_slots(self):
        plots = []
        for slot in self.array_of_slots():
            plots.append(slot.draw())
        return plots
    

    def a_round(self, was_success):
        self.pull_lever(was_success, self.selected_slot )
        for slot in self.array_of_slots():
            print('{} posterior is beta ( {} , {} )'.format(slot.name, slot.a, slot.b)) 
        return self.draw_posteriors_of_slots()



    