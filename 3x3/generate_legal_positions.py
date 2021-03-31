#This function generates legal positions according to a simple algo.

import random

def legalPositionsSelect(gm_dict):
	
	#A while loop picks numbers from the legal range and assigns them to gm_dict's positional list.
	
	i = 0
	
	while i < 4:
		gm_dict['positional_list'].append(random.randint(1,17))
		i += 1
		
