#This function generates legal positions according to a simple algo.

import random

def legalPositionsSelect(gm_dict):
	
	#A while loop picks numbers from the legal range, calculates solvability and then assigns them to gm_dict's positional list.

	def checkSolvability(gm_dict):
		if gm_dict['positional_list'][1] - gm_dict['positional_list'][3] == gm_dict['positional_list'][0] - gm_dict['positional_list'][2]:
			return True
		else:
			return False

	#Another while loop checks the board for solvability using above procedure and either continues or regenerates.

	i = 0
	
	while i < 4:
		if checkSolvability(gm_dict):
			print('Solvability test passed in generate_legal_positions.')
			print(gm_dict['positional_list'])
			break
		else:
			print('Solvability test failed in generate_legal_positions.')
			for i in range (1,4):
				gm_dict['positional_list'].pop(i)
				gm_dict['positional_list'].append(random.randint(3,17))			

