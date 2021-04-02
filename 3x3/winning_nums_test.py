#This function selects winning numbers. It rewrites incorrect choices until winning numbers are selected. 

import random
from build_choice_list import *
from determine_if_choices_win import *

def selectWinningNums(gmDict, winningDict):	
	
	if winnerEval(winningDict):
		print('Winner!')
	else:
		while not winnerEval(winningDict):
			buildChoices(gmDict)

			if winnerEval(winningDict):
				print('All conditions satisfied!')
				break
			else:
				print('Continuing tests...')
				continue


			


		
	
	
	
