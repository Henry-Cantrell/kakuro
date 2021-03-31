#Execute the program from this file. 

from gm_dictionary import *
from generate_legal_positions import *
from winning_nums_test import *
from winning_conds_dict import *

def gameFlow(gmDict, winningConditionsDict):
	legalPositionsSelect(gmDict)
	selectWinningNums(gmDict, winningConditionsDict, )
	
gameFlow(game_master_dict, winningConditionsDict)
	



	
