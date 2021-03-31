#This function selects winning numbers. It rewrites incorrect choices until winning numbers are selected. It then displays the winning nums.

import random
from build_choice_list import *
from determine_if_choices_win import *

def selectWinningNums(gmDict, winningDict):	
	
	buildChoices(gmDict)
	winnerEval(winningDict)
	
	while not all_positions_satisfied:
		buildChoices(gmDict)
		winnerEval(winningDict)
		
		if winnerEval:
			print('All conditions satisfied!')
			break
		else:
			print('Continuing tests...')
			continue
			
#To-do list:
#A lot of things are working well!
#But, error seems to be that the procedure is not detecing legal choices. Need to diagnose this...tomorrow...
#Look into evaluating functions using loops?




		
	
	
	
