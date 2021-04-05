#This function generates legal positions according to a simple algo.

import random

def legalPositionsSelect(gm_dict):

	def checkSolvability(gm_dict):
		if gm_dict['positional_list'][1] - gm_dict['positional_list'][3] == gm_dict['positional_list'][0] - gm_dict['positional_list'][2]:
			gm_dict['positional_list'][1], gm_dict['positional_list'][3] = gm_dict['positional_list'][3], gm_dict['positional_list'][1]
			return True
		else:
			return False

	#While loop checks the board for solvability using above procedure and either continues or regenerates.
	
	n = 0

	while n < 1:
		if checkSolvability(gm_dict):
			print('Solvability test passed in generate_legal_positions. See the board below: ')
			print(gm_dict['positional_list'])
			break
		else:
			print('Solvability test failed in generate_legal_positions.')
			for i in range (1,4):
				gm_dict['positional_list'].pop(i)
				gm_dict['positional_list'].append(random.randint(3,17))	

	


