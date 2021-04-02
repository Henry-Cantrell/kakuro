import random
from test_list import *
from gm_dictionary import *

def buildChoices(gmDict):
	
	#This func restricts the size of the choices list to 4 and also fills the choices list.

	for i in range(4):
		if len(gmDict['choices_list']) == 4:
			gmDict['choices_list'].pop(i)
			gmDict['choices_list'].append(random.randint(1, 9))
			print('Rewriting a filled illegal list...')
			print(gmDict['choices_list'])
		elif len(gmDict['choices_list']) != 4:
			gmDict['choices_list'].append(random.randint(1, 9))
			print('Filling an empty list...')


