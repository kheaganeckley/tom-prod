import plotly.express as pxt
import scipy.stats as stat
from tom.slot import slot

class tompson_sampler():
    """
    docstring: a tomson sampler
    """
    def __init__(self, a1 =1.0, b1 =1.0, a2 =1.0, b2 =1.0, a3 =1.0, b3=1.0):
        
        self.slot1 = slot(a1 , b1, 'slot 1')
        self.slot2 = slot(a2 , b2, 'slot 2')
        self.slot3 = slot(a3 , b3, 'slot 3')
       
    def array_of_slots(self):
        return [self.slot1,  self.slot2, self.slot3 ]
    
    def select_slot(self):
        
        array_of_slots = self.array_of_slots()
        slot_with_maxed_sample_posterior = array_of_slots[0]
        
        for slot in array_of_slots:
            
            if slot.sample_posterior_beta(1) >  slot_with_maxed_sample_posterior.current_sample:
                slot_with_maxed_sample_posterior = slot
                slot.current_sample = slot.sample_posterior_beta(1)
            print('sample {} from {}'.format(slot.current_sample, slot.name))
               
            
        print('max sample currently is {} from {}'.format(slot_with_maxed_sample_posterior.current_sample,
                                                          slot_with_maxed_sample_posterior.name))
        return slot_with_maxed_sample_posterior
    
    
    def pull_lever(self, was_success, slot):   
        if was_success is True: # add 1 to a in beta (the loc parm
            slot.a += 1
        
        else:  ## if was not sucess add 1 to b in beta (the sale parm) 
            slot.b += 1
    
    def a_round(self, was_success):
        slected_slot = self.select_slot()
        self.pull_lever(was_success, slected_slot)
        for slot in self.array_of_slots():
            print('{} posterior is beta ( {} , {} )'.format(slot.name, slot.a, slot.b))
        self.draw_posteriors_of_slots()
            
    def draw_posteriors_of_slots(self):
        plots = []
        for slot in self.array_of_slots():
            plots.append(slot.draw())
        return plots
    