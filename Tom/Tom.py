"""
just some random methods

"""

def select_slot(slots, sample):    
     """
     docstring: you need to specify slots and the sampling method beta, ext
     """

     temp_current_sample = dict(
                              a = 0,
                              b = 0,
                              current_sample = 0,
                              name = 'dummy'
                           )

     for slot in slots.values():
            sampling = sample(slot)
            print('sample {} from {}'.format(sampling, slot['name']))
               

            if  sampling >  temp_current_sample['current_sample']:
                temp_current_sample = slot
                temp_current_sample['current_sample'] = sampling

     print('max sample is {} from {}'.format( temp_current_sample['current_sample'] ,temp_current_sample['name'] ))
     return temp_current_sample['name']

    
def draw_posteriors_of_slots(slots, draw):
      """
      docstring: you need to specify slots and the drawing plots method will be diffrent 
      """

      plots = []
      for slot in slots.values():
            plots.append(draw(slot))
      return plots


